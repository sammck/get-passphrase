from typing import Optional, Tuple

from ..resolver import PassphraseResolver, PassphraseContext, Passphrase

import keyring
from keyring.backend import KeyringBackend
from keyring.core import load_keyring

class KeyringPassphraseResolver(PassphraseResolver):
  passphrase_scheme: Optional[str] = "keyring"

  def normalize_service_key(self, context: PassphraseContext) -> Tuple[str, str]:
    default_service_name = self.get_context_value('keyring_default_service_name', context)
    default_key_name = self.get_context_value('keyring_default_key_name', context)
    descriptor = self.get_context_value('descriptor', context)
    if descriptor is None or descriptor == '':
      service_name = default_service_name
      key_name = default_key_name
    else:
      service_key_delimiter: Optional[str] = self.get_context_value('keyring_service_key_delimiter', context)
      if service_key_delimiter is None:
        service_key_delimiter = self.get_context_value('keyring_default_service_key_delimiter', context)
      if service_key_delimiter is None:
        service_key_delimiter = ','
      parts = descriptor.split(service_key_delimiter, 1)
      if len(parts) > 1:
        service_name, key_name = parts
      else:
        service_name = ''
        key_name = parts[0]
      if service_name is None or service_name == '':
        service_name = default_service_name
      if key_name is None or key_name == '':
        key_name = default_key_name
    if service_name is None:
      service_name = ''
    if key_name is None:
      key_name = ''
    service_name_prefix = self.get_context_value('keyring_service_name_prefix', context)
    if not service_name_prefix is None:
      service_name = service_name_prefix + service_name
    if service_name is None or service_name == '':
      raise ValueError("Empty service name in keyring passphrase descriptor")
    key_name_prefix = self.get_context_value('keyring_key_name_prefix', context)
    if not key_name_prefix is None:
      key_name = key_name_prefix + key_name
    if key_name is None or key_name == '':
      raise ValueError("Empty key name in keyring passphrase descriptor")

    return (service_name, key_name)

  def read_passphrase(self, context: PassphraseContext) -> Passphrase:
    service_name, key_name = self.normalize_service_key(context)
    key_ring = self.get_context_value("keyring", context)
    if key_ring is None:
      keyring_name: Optional[str] = self.get_context_value('keyring-name', context)
      if keyring_name is None or keyring_name == '':
        key_ring = keyring.get_keyring()
      else:
        key_ring = load_keyring(keyring_name)
      

    passphrase = key_ring.get_password(service_name, key_name)
    return self.normalize_passphrase(passphrase, context)
