from typing import Optional, Dict, Any, List, Type, Tuple, Union

import os
from webbrowser import get

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

class AnyPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "any"

  def _prep_read_passphrase(self, context: PassphraseContext) -> Tuple[PassphraseResolver, PassphraseContext]:
    context = self.clone_context(context)
    merge_standard_resolvers: bool = self.get_context_value('merge_standard_resolvers', context, True)
    context['merge_standard_resolvers'] = False
    resolvers: Dict[str, PassphraseResolver] = self.get_context_value('resolvers', context)
    if resolvers is None:
      resolvers: Dict[str, PassphraseResolver] = {}
      context['resolvers'] = resolvers
    resolver_classes: Optional[Union[
         Dict[str, Type[PassphraseResolver]],
         List[Union[
               Type[PassphraseResolver],
               Tuple[str, Type[PassphraseResolver]]
              ]]
          ]] = self.get_context_value('resolver_classes', context)
    if not resolver_classes is None:
      if isinstance(resolver_classes, dict):
        resolver_classes = list(resolver_classes.items())

      resolver_classes: List[Union[Type[PassphraseResolver], Tuple[str, Type[PassphraseResolver]]]]

      for entry in resolver_classes:
        if isinstance(entry, tuple):
          scheme, resolver_class = entry
        else:
          resolver_class = entry
          scheme = resolver_class.passphrase_scheme

        if not scheme is None:
          if not scheme in resolvers:
            resolvers[scheme] = resolver_class(self._base_context)

    if merge_standard_resolvers:
      from .standard_resolvers import standard_resolver_classes
      for resolver_class in standard_resolver_classes:
        scheme = resolver_class.passphrase_scheme
        if not scheme is None:
          if not scheme in resolvers:
            resolvers[scheme] = resolver_class(self._base_context)

    auto_inline: bool = self.get_context_value('auto_inline', context, False)
    descriptor: Optional[str] = self.get_context_value('descriptor', context)
    if descriptor is None or descriptor == '':
      scheme = ''
      subdescriptor = descriptor
    else:
      parts = descriptor.split(':', 1)
      if len(parts) > 1:
        scheme, subdescriptor = parts
        auto_inline = False
      else:
        scheme = ''
        subdescriptor = descriptor
    if scheme == '':
      if not auto_inline:
        raise ValueError("Explicit scheme is required in passphrase descriptor; e.g., \"<scheme>:<scheme-data>\"")
      scheme = "inline"
    if not scheme in resolvers:
      raise ValueError(f"Invalid scheme \"{scheme}\" in passphrase descriptor")
    resolver = resolvers[scheme]
    context['descriptor'] = subdescriptor
    return resolver, context


  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    resolver, context = self._prep_read_passphrase(context)
    result = resolver.read_passphrase(context)
    return result

  async def async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    resolver, context = self._prep_read_passphrase(context)
    result = await resolver.async_read_passphrase(context)
    return result
