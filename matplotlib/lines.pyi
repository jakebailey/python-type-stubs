from typing import Any, Optional

from matplotlib._typing import ArrayLike
from matplotlib.colors import _ColorLike
from matplotlib.markers import MarkerStyle

class Line2D:
    def __init__(
        self,
        xdata: ArrayLike,
        ydata: ArrayLike,
        linewidth: Optional[float] = ...,
        linestyle=None,
        color: Optional[_ColorLike] = ...,
        marker: Optional[MarkerStyle] = ...,
        markersize: Optional[float] = ...,
        markeredgewidth=None,
        markeredgecolor: Optional[_ColorLike] = ...,
        markerfacecolor: Optional[_ColorLike] = ...,
        markerfacecoloralt: Optional[_ColorLike] = ...,
        fillstyle=None,
        antialiased=None,
        dash_capstyle=None,
        solid_capstyle=None,
        dash_joinstyle=None,
        solid_joinstyle=None,
        pickradius: float = ...,
        drawstyle=None,
        markevery=None,
        **kwargs: Any,
    ) -> None: ...



def __getattr__(name: str) -> Any: ...  # incomplete
