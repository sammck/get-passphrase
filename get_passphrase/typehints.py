#!/usr/bin/env python3

import datetime

from typing import (
    Dict,
    Union,
    Any,
    List,
    Optional,
    Callable,
    Awaitable,
    NewType,
    AsyncIterable,
    AsyncGenerator,
    AsyncContextManager,
    AsyncIterator,
    Tuple,
    Type,
    Set,
    TypeVar,
    TYPE_CHECKING,
    FrozenSet,
    Coroutine,
    Generator,
    Iterable,
    Iterator,
  )

NoneType = type(None)

JSONType = Union[str, int, float, bool, NoneType, Dict[str, Any], List[Any]]

JSONDictType = Dict[str, JSONType]
