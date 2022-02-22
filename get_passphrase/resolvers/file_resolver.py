from typing import Optional

import os

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class FilePassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "file"

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    pathname = self.get_context_value('descriptor', context)
    base_dir = self.get_context_value('base_dir', context, '.')
    if pathname is None or pathname == "":
      raise ValueError(f"Invalid empty filename in passphrase meta")
    pathname = os.path.join(base_dir, pathname)

    passphrase: Optional[str] = None
    try:
      with open(pathname, encoding=self.get_context_value('encoding', context, 'utf-8')) as f:
        # we read only the first line, since a passphrase cannot contain newlines.
        passphrase = f.readline().rstrip('\n\r')  # we leave trailing whitespace, a legitimate passphrase character
    except FileNotFoundError:
      pass

    return self.normalize_passphrase(passphrase, context)
