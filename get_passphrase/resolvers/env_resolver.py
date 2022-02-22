from typing import Optional, Dict

import os

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class EnvPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "env"

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    passphrase: Optional[str] = None
    env_var = self.get_context_value('descriptor', context)
    if env_var is None or env_var == '':
      env_var = self.get_context_value('default_env_var', context)
    if not env_var is None and env_var != '':
      env = self.get_context_value('env', context)
      if env is None:
        # WARNING: This is not threadsafe if anyone is calling setenv
        env = dict(os.environ)
      passphrase = env.get(env_var, None)
    return self.normalize_passphrase(passphrase, context)

  async def async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    return self.read_passphrase(context)
