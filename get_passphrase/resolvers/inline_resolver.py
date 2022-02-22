from typing import Optional

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class InlinePassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "pass"

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    passphrase: Optional[str] = self.get_context_value('descriptor', context)
    return self.normalize_passphrase(passphrase, context)

  async def async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    return self.read_passphrase(context)

