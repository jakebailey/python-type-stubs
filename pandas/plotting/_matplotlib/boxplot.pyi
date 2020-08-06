#from collections import namedtuple
#from pandas.core.dtypes.common import is_dict_like as is_dict_like
#from pandas.core.dtypes.generic import ABCSeries as ABCSeries
#from pandas.core.dtypes.missing import remove_na_arraylike as remove_na_arraylike
#from pandas.io.formats.printing import pprint_thing as pprint_thing
from pandas.plotting._matplotlib.core import LinePlot as LinePlot
# , MPLPlot as MPLPlot
from typing import Any, NamedTuple, Optional

class BoxPlot(LinePlot):
    class BoxPlot(NamedTuple):
        ax: Any
        lines: Any

    BP = BoxPlot

    return_type: Any = ...
    def __init__(self, data: Any, return_type: str = ..., **kwargs: Any) -> None: ...
    def maybe_color_bp(self, bp: Any) -> None: ...
    @property
    def orientation(self): ...
    @property
    def result(self): ...

def boxplot(data: Any, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., **kwds: Any): ...
def boxplot_frame(self, column: Optional[Any] = ..., by: Optional[Any] = ..., ax: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., return_type: Optional[Any] = ..., **kwds: Any): ...
def boxplot_frame_groupby(grouped: Any, subplots: bool = ..., column: Optional[Any] = ..., fontsize: Optional[Any] = ..., rot: int = ..., grid: bool = ..., ax: Optional[Any] = ..., figsize: Optional[Any] = ..., layout: Optional[Any] = ..., sharex: bool = ..., sharey: bool = ..., **kwds: Any): ...