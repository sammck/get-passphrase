from typing import Optional

import os

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class FdPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "fd"

  _closed: bool = False

  NEWLINE = ord('\n')
  RETURN = ord('\r')

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    fd_s = self.get_context_value('descriptor', context)
    if fd_s is None or fd_s == "":
      fd = self.get_context_value('default_fd', context)
    else:
      try:
        fd = int(fd_s)
      except ValueError:
        raise ValueError(f"Invalid file descriptor \"{fd_s}\" in passphrase meta")

    if fd is None:
      raise ValueError(f"Invalid empty file descriptor in passphrase meta")

    buff: bytes = b''
    while True:
      # read one character at a time so that caller can continue reading from next line
      b = os.read(fd, 1)
      if len(b) == 0 or b[0] == self.NEWLINE:
        break
      if b[0] != self.RETURN:
        buff += b
    passphrase = buff.decode(self.get_context_value('encoding', context, 'utf-8'))
    close_after_read: bool = self.get_context_value("close_after_read", context, False)
    if close_after_read:
      os.close(fd)
      self._closed = True
    return self.normalize_passphrase(passphrase, context)

  @property
  def is_closed(self) -> bool:
    return self._closed
