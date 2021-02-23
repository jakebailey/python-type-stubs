from typing import Any


class ColorbarBase:
    ...

class Colorbar(ColorbarBase):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
