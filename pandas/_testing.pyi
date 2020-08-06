#from pandas import Categorical as Categorical, CategoricalIndex as CategoricalIndex, DataFrame as DataFrame, DatetimeIndex as DatetimeIndex, Index as Index, IntervalIndex as IntervalIndex, MultiIndex as MultiIndex, RangeIndex as RangeIndex, Series as Series, bdate_range as bdate_range
#from pandas._config.localization import can_set_locale as can_set_locale, get_locales as get_locales, set_locale as set_locale
from core.arrays.categorical import Categorical
from core.frame import DataFrame
from core.indexes.base import Index
from core.series import Series
from pandas._typing import FilePathOrBuffer as FilePathOrBuffer, FrameOrSeries as FrameOrSeries
#from pandas.core.algorithms import take_1d as take_1d
#from pandas.core.arrays import DatetimeArray as DatetimeArray, ExtensionArray as ExtensionArray, IntervalArray as IntervalArray, PeriodArray as PeriodArray, TimedeltaArray as TimedeltaArray, period_array as period_array
#from pandas.core.dtypes.common import is_bool as is_bool, is_categorical_dtype as is_categorical_dtype, is_datetime64_dtype as is_datetime64_dtype, is_datetime64tz_dtype as is_datetime64tz_dtype, is_extension_array_dtype as is_extension_array_dtype, is_interval_dtype as is_interval_dtype, is_list_like as is_list_like, is_number as is_number, is_period_dtype as is_period_dtype, is_sequence as is_sequence, is_timedelta64_dtype as is_timedelta64_dtype, needs_i8_conversion as needs_i8_conversion
#from pandas.core.dtypes.missing import array_equivalent as array_equivalent
#from pandas.io.common import urlopen as urlopen
#from pandas.io.formats.printing import pprint_thing as pprint_thing
from typing import Any, List, Optional, Union

lzma: Any
N: int
K: int

def set_testing_mode() -> None: ...
def reset_testing_mode() -> None: ...
def reset_display_options() -> None: ...
def round_trip_pickle(obj: Any, path: Optional[FilePathOrBuffer]=...) -> FrameOrSeries: ...
def round_trip_pathlib(writer: Any, reader: Any, path: Optional[str]=...) -> Any: ...
def round_trip_localpath(writer: Any, reader: Any, path: Optional[str]=...) -> Any: ...
def decompress_file(path: Any, compression: Any) -> None: ...
def write_to_compressed(compression: Any, path: Any, data: Any, dest: str = ...) -> None: ...
def assert_almost_equal(left: Any, right: Any, check_dtype: Union[bool, str]=..., check_less_precise: Union[bool, int]=..., **kwargs: Any) -> Any: ...
def assert_dict_equal(left: Any, right: Any, compare_keys: bool=...) -> Any: ...
def randbool(size: Any=..., p: float=...) -> Any: ...

RANDS_CHARS: Any
RANDU_CHARS: Any

def rands_array(nchars: Any, size: Any, dtype: str = ...): ...
def randu_array(nchars: Any, size: Any, dtype: str = ...): ...
def rands(nchars: Any): ...
def randu(nchars: Any): ...
def close(fignum: Optional[Any] = ...) -> None: ...
def ensure_clean(filename: Optional[Any] = ..., return_filelike: bool = ...) -> None: ...
def ensure_clean_dir() -> None: ...
def ensure_safe_environment_variables() -> None: ...
def equalContents(arr1: Any, arr2: Any) -> bool: ...
def assert_index_equal(left: Index[Any], right: Index[Any]) -> None: ...
def assert_class_equal(left: Any, right: Any, exact: Union[bool, str]=..., obj: Any=...) -> Any: ...
def assert_attr_equal(attr: Any, left: Any, right: Any, obj: str = ...): ...
def assert_is_valid_plot_return_object(objs: Any) -> None: ...
def isiterable(obj: Any) -> bool: ...
def assert_is_sorted(seq: Any) -> None: ...
def assert_categorical_equal(left: Any, right: Any, check_dtype: bool = ..., check_category_order: bool = ..., obj: str = ...) -> None: ...
def assert_interval_array_equal(left: Any, right: Any, exact: str = ..., obj: str = ...) -> None: ...
def assert_period_array_equal(left: Any, right: Any, obj: str = ...) -> None: ...
def assert_datetime_array_equal(left: Any, right: Any, obj: str = ...) -> None: ...
def assert_timedelta_array_equal(left: Any, right: Any, obj: str = ...) -> None: ...
def raise_assert_detail(obj: Any, message: Any, left: Any, right: Any, diff: Optional[Any] = ...) -> None: ...
def assert_numpy_array_equal(left: Any, right: Any, strict_nan: bool = ..., check_dtype: bool = ..., err_msg: Optional[Any] = ..., check_same: Optional[Any] = ..., obj: str = ...): ...
def assert_extension_array_equal(
    left: Any, right: Any, check_dtype: bool = ..., check_less_precise: bool = ..., check_exact: bool = ...,
) -> None: ...
def assert_series_equal(left: Series, right: Series) -> None: ...
def assert_frame_equal(left: DataFrame, right: DataFrame, check_like: Optional[bool] = ...) -> None: ...
def assert_equal(left: Any, right: Any, **kwargs: Any) -> None: ...
def box_expected(expected: Any, box_cls: Any, transpose: bool = ...): ...
def to_array(obj: Any): ...
def assert_sp_array_equal(left: Any, right: Any, check_dtype: bool = ..., check_kind: bool = ..., check_fill_value: bool = ..., consolidate_block_indices: bool = ...) -> None: ...
def assert_contains_all(iterable: Any, dic: Any) -> None: ...
def assert_copy(iter1: Any, iter2: Any, **eql_kwargs: Any) -> None: ...
def getCols(k: Any): ...
def makeStringIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeUnicodeIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeCategoricalIndex(k: int = ..., n: int = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makeIntervalIndex(k: int = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makeBoolIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeIntIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeUIntIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeRangeIndex(k: int = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makeFloatIndex(k: int = ..., name: Optional[Any] = ...): ...
def makeDateIndex(k: int = ..., freq: str = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makeTimedeltaIndex(k: int = ..., freq: str = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makePeriodIndex(k: int = ..., name: Optional[Any] = ..., **kwargs: Any): ...
def makeMultiIndex(k: int = ..., names: Optional[Any] = ..., **kwargs: Any): ...
def all_index_generator(k: int = ...) -> None: ...
def index_subclass_makers_generator() -> None: ...
def all_timeseries_index_generator(k: int = ...) -> None: ...
def makeFloatSeries(name: Optional[Any] = ...): ...
def makeStringSeries(name: Optional[Any] = ...): ...
def makeObjectSeries(name: Optional[Any] = ...): ...
def getSeriesData(): ...
def makeTimeSeries(nper: Optional[Any] = ..., freq: str = ..., name: Optional[Any] = ...): ...
def makePeriodSeries(nper: Optional[Any] = ..., name: Optional[Any] = ...): ...
def getTimeSeriesData(nper: Optional[Any] = ..., freq: str = ...): ...
def getPeriodData(nper: Optional[Any] = ...): ...
def makeTimeDataFrame(nper: Optional[Any] = ..., freq: str = ...): ...
def makeDataFrame(): ...
def getMixedTypeDict(): ...
def makeMixedDataFrame(): ...
def makePeriodFrame(nper: Optional[Any] = ...): ...
def makeCustomIndex(nentries: Any, nlevels: Any, prefix: str = ..., names: bool = ..., ndupe_l: Optional[Any] = ..., idx_type: Optional[Any] = ...): ...
def makeCustomDataframe(nrows: Any, ncols: Any, c_idx_names: bool = ..., r_idx_names: bool = ..., c_idx_nlevels: int = ..., r_idx_nlevels: int = ..., data_gen_f: Optional[Any] = ..., c_ndupe_l: Optional[Any] = ..., r_ndupe_l: Optional[Any] = ..., dtype: Optional[Any] = ..., c_idx_type: Optional[Any] = ..., r_idx_type: Optional[Any] = ...): ...
def makeMissingCustomDataframe(nrows: Any, ncols: Any, density: float = ..., random_state: Optional[Any] = ..., c_idx_names: bool = ..., r_idx_names: bool = ..., c_idx_nlevels: int = ..., r_idx_nlevels: int = ..., data_gen_f: Optional[Any] = ..., c_ndupe_l: Optional[Any] = ..., r_ndupe_l: Optional[Any] = ..., dtype: Optional[Any] = ..., c_idx_type: Optional[Any] = ..., r_idx_type: Optional[Any] = ...): ...
def makeMissingDataframe(density: float = ..., random_state: Optional[Any] = ...): ...
def optional_args(decorator: Any): ...
def can_connect(url: Any, error_classes: Optional[Any] = ...): ...
def network(t: Any, url: str = ..., raise_on_error: Any = ..., check_before_test: bool = ..., error_classes: Optional[Any] = ..., skip_errnos: Any = ..., _skip_on_messages: Any = ...): ...
with_connectivity_check = network

def assert_produces_warning(expected_warning: Any = ..., filter_level: str = ..., clear: Optional[Any] = ..., check_stacklevel: bool = ..., raise_on_extra_warnings: bool = ...) -> None: ...

class RNGContext:
    seed: Any = ...
    def __init__(self, seed: Any) -> None: ...
    start_state: Any = ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...

def with_csv_dialect(name: Any, **kwargs: Any) -> None: ...
def use_numexpr(use: Any, min_elements: Optional[Any] = ...) -> None: ...
def test_parallel(num_threads: int = ..., kwargs_list: Optional[Any] = ...): ...

class SubclassedSeries(Series): ...
class SubclassedDataFrame(DataFrame): ...
class SubclassedCategorical(Categorical): ...

def set_timezone(tz: str) -> Any: ...
def convert_rows_list_to_csv_str(rows_list: List[str]) -> Any: ...