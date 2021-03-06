import time
from functools import wraps as wraps
from typing import Any, Optional

MAX_WAIT: Any

def capture(fut: Any, tb: Any) -> None: ...
def getargspec(func: Any): ...
def visible_attrs(obj: Any, attrs: Optional[Any] = ...): ...
def find_ordinal(pos_num: Any): ...
def to_ordinal(pos_num: Any): ...
def get_callback_name(cb: Any): ...
now = time.monotonic

class cached_property:
    func: Any = ...
    def __init__(self, func: Any) -> None: ...
    def __get__(self, obj: Any, cls: Any): ...
