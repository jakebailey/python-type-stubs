from typing import Any

from matplotlib.cm import ScalarMappable

class ContourLabeler:
    ...

class ContourSet(ScalarMappable, ContourLabeler):
    ...

class QuadContourSet(ContourSet):
    ...


def __getattr__(name: str) -> Any: ...  # incomplete
