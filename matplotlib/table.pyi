from typing import Any

from matplotlib.artist import Artist


class Table(Artist):
    ...

def __getattr__(name: str) -> Any: ...  # incomplete
