from typing import Any


class Widget:
    ...

class SubplotTool(Widget):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
