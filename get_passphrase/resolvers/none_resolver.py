from typing import Optional
from .fixed_resolver import FixedPassphraseResolver, Passphrase, PassphraseContext

class NonePassphraseResolver(FixedPassphraseResolver):
  passphrase_scheme: Optional[str] = "none"
  allow_bare_passphrase_scheme: bool = True

  def __init__(self, base_context: Optional[PassphraseContext]=None):
    super().__init__(base_context)
    self._base_context['fixed_passphrase'] = None
