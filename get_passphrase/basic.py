from typing import Optional, Union, List

from .resolvers import AnyPassphraseResolver
from .resolvers import InlinePassphraseResolver

from .passphrase import Passphrase
from .resolver import PassphraseContext, PassphraseResolver

def resolve_passphrase(
      descriptors: Optional[Union[List[Union[Passphrase, str]], Passphrase, str]],
      context: Optional[PassphraseContext]=None,
      auto_inline: bool=False,
      require: bool=True,
    ) -> Passphrase:

  if not isinstance(descriptors, list):
    descriptors = [ descriptors ]

  passphrase = Passphrase(None)

  for descriptor in descriptors:
    if isinstance(descriptor, Passphrase):
      passphrease = descriptor
    else:
      if context is None:
        context = PassphraseResolver.create_context()
      else:
        context = PassphraseResolver.clone_context(context)
      context['auto_inline'] = auto_inline
      context['descriptor'] = descriptor
      resolver = AnyPassphraseResolver(context)
      passphrase = resolver.read_passphrase(context)
      
      passphrase = Passphrase(passphrase)
    if not passphrase.get_cleartext() is None:
      break

  if require and passphrase.get_cleartext() is None:
    raise ValueError("Unable to resolve passphrase; a passphrase is required")

  return passphrase

async def async_resolve_passphrase(
      descriptors: Optional[Union[List[Union[Passphrase, str]], Passphrase, str]],
      context: Optional[PassphraseContext]=None,
      auto_inline: bool=False,
      require: bool=True,
    ) -> Passphrase:

  if not isinstance(descriptors, list):
    descriptors = [ descriptors ]

  passphrase = Passphrase(None)

  for descriptor in descriptors:
    if isinstance(descriptor, Passphrase):
      passphrease = descriptor
    else:
      if context is None:
        context = PassphraseResolver.create_context()
      else:
        context = PassphraseResolver.clone_context(context)
      context['auto_inline'] = auto_inline
      context['descriptor'] = descriptor
      resolver = AnyPassphraseResolver(context)
      passphrase = await resolver.read_passphrase(context)
      
      passphrase = Passphrase(passphrase)
    if not passphrase.get_cleartext() is None:
      break

  if require and passphrase.get_cleartext() is None:
    raise ValueError("Unable to resolve passphrase; a passphrase is required")

  return passphrase

