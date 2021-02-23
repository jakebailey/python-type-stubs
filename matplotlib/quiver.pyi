from typing import Any

from matplotlib.artist import Artist
from matplotlib.collections import PolyCollection


class Barbs(PolyCollection):
    ...

class Quiver(PolyCollection):
    ...

class QuiverKey(Artist):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
