
from typing import List, Type
from ..resolver import PassphraseResolver

from .fixed_resolver import FixedPassphraseResolver
from .empty_resolver import EmptyPassphraseResolver
from .none_resolver import NonePassphraseResolver
from .inline_resolver import InlinePassphraseResolver
from .env_resolver import EnvPassphraseResolver
from .fd_resolver import FdPassphraseResolver
from .stdin_resolver import StdinPassphraseResolver
from .file_resolver import FilePassphraseResolver
from .getpass_resolver import GetpassPassphraseResolver
from .keyring_resolver import KeyringPassphraseResolver
from .any_resolver import AnyPassphraseResolver


standard_resolver_classes: List[Type[PassphraseResolver]] = [
    FixedPassphraseResolver,
    EmptyPassphraseResolver,
    NonePassphraseResolver,
    InlinePassphraseResolver,
    EnvPassphraseResolver,
    FdPassphraseResolver,
    StdinPassphraseResolver,
    FilePassphraseResolver,
    GetpassPassphraseResolver,
    KeyringPassphraseResolver,
    AnyPassphraseResolver,
 ]
