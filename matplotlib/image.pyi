from typing import Any


class _ImageBase:
    ...

class FigureImage(_ImageBase):
    ...

class AxesImage(_ImageBase):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
