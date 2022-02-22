from typing import Optional, TextIO

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

import getpass

class GetpassPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "prompt"
  allow_bare_passphrase_scheme: bool = True

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    prompt: Optional[str] = self.get_context_value('descriptor', context)
    if prompt is None or prompt == '':
      prompt = self.get_context_value('default_prompt', context)
    if prompt is None or prompt == '':
      prompt = 'Password: '
    prompt_stream: Optional[TextIO] = self.get_context_value('prompt_stream', context)
    passphrase = getpass.getpass(prompt=prompt, stream=prompt_stream)
    return self.normalize_passphrase(passphrase, context)
