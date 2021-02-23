from typing import Any

from matplotlib.artist import Artist


class Text(Artist):
    ...

class Annotation(Text):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
