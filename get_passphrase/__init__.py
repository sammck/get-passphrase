import importlib.metadata
__version__ =  importlib.metadata.version("get-passphrase") #  '0.1.0'

from .basic import resolve_passphrase, async_resolve_passphrase
from .resolver import PassphraseResolver, PassphraseContext
from .passphrase import Passphrase
