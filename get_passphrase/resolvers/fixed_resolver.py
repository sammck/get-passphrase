from typing import Optional, Union

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class FixedPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = None
  allow_bare_passphrase_scheme: bool = True

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    passphrase: Optional[Union[Passphrase, str]] = self.get_context_value('fixed_passphrase', context)
    return self.normalize_passphrase(passphrase, context)

  async def async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    return self.read_passphrase(context)

