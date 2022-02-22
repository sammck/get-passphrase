from typing import Optional

import sys

from .fd_resolver import FdPassphraseResolver
from ..resolver import PassphraseContext

class StdinPassphraseResolver(FdPassphraseResolver):
  passphrase_scheme: Optional[str] = "stdin"
  allow_bare_passphrase_scheme: bool = True

  def __init__(self, base_context: Optional[PassphraseContext]=None):
    super().__init__(base_context)
    self._base_context['default_fd'] = sys.stdin.fileno()
