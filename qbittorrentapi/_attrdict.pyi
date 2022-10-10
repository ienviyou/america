from abc import ABCMeta
from typing import Any
from typing import Dict
from typing import Mapping
from typing import MutableMapping
from typing import Text
from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")
KWARGS = Any

def merge(left: Mapping[Any, Any], right: Mapping[Any, Any]) -> Dict[Any, Any]: ...

class Attr(Mapping[K, V], metaclass=ABCMeta):
    def __call__(self, key: Any) -> Any: ...
    def __getattr__(self, key: Any) -> Any: ...
    def __add__(self, other: Mapping[Any, Any]) -> Attr[Any, Any]: ...
    def __radd__(self, other: Mapping[Any, Any]) -> Attr[Any, Any]: ...

class MutableAttr(Attr[K, V], MutableMapping[K, V], metaclass=ABCMeta):
    def __setattr__(self, key: Any, value: Any) -> None: ...
    def __delattr__(self, key: Any, force: bool = ...) -> None: ...

class AttrDict(Dict[K, V], MutableAttr[K, V]):
    def __init__(self, *args: Mapping[Text, Any], **kwargs: KWARGS) -> None: ...
