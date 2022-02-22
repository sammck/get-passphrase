from typing import Optional, Dict, Any, Union, TypeVar

import asyncio
from concurrent.futures import ThreadPoolExecutor

from .passphrase import Passphrase
from .util import full_type

PassphraseContext = Dict[str, Any]


class PassphraseResolver:
  passphrase_scheme: Optional[str] = None
  allow_bare_passphrase_scheme: bool = False

  _base_context: PassphraseContext

  def __init__(self, base_context: Optional[PassphraseContext]=None):
    if base_context is None:
      base_context = self.create_context()
    else:
      base_context = self.clone_context(base_context)
    self._base_context = base_context

  @classmethod
  def create_context(self) -> PassphraseContext:
    return {}

  @classmethod
  def clone_context(self, context: PassphraseContext) -> PassphraseContext:
    return dict(context)

  @classmethod  
  def merge_contexts(self, *contexts: PassphraseContext) -> PassphraseContext:
    new_context = self.create_context()
    for context in contexts:
      new_context.update(context)
    return new_context

  def get_base_context_value(self, key: str, default: Any=None) -> Any:
    result: Any = default
    if key in self._base_context:
      result = self._base_context[key]
    return result

  def get_context_value(self, key: str, context: Optional[PassphraseContext], default: Any=None) -> Any:
    if not context is None and key in context:
      result = context[key]
    else:
      result = self.get_base_context_value(key, default)
    return result

  def get_none_value(self, context: Optional[PassphraseContext]) -> Optional[str]:
    return self.get_context_value("none_value", None)

  def normalize_passphrase(self, passphrase: Optional[Union[str, Passphrase]], context: Optional[PassphraseContext]=None) -> Passphrase:
    if not isinstance(passphrase, Passphrase):
      none_value = self.get_none_value(context)
      if passphrase == none_value:
        passphrase = None
      passphrase = Passphrase(passphrase)
    return passphrase

  def wrap_async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(self.async_read_passphrase(context))    

  async def wrap_sync_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    with ThreadPoolExecutor(1, "AsyncReadPassphrase") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, lambda: self.read_passphrase(context))

  # methods overridden by subclasses:
  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    raise NotImplementedError(f"{full_type(self)} does not implement read_pasphrase")

  async def async_read_passphrase(self, context: PassphraseContext) -> Passphrase:
    return self.wrap_sync_read_passphrase()
