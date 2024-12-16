from datetime import datetime, date, time
from typing import Any, TypeVar, Type, cast, Callable, List


T = TypeVar("T")

def from_int(x: Any) -> int:
	if x is None: return x
	assert isinstance(x, int) and not isinstance(x, bool)
	return x

def from_datetime(x: Any) -> datetime:
	if x is None: return x
	assert isinstance(x, datetime)
	return x

def from_time(x: Any) -> datetime:
	if x is None: return x
	assert isinstance(x, time)
	return x

def from_date(x: Any) -> date:
	if x is None: return x
	assert isinstance(x, date)
	return x

def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
	if x is None: return x 
	assert isinstance(x, list)
	return [f(y) for y in x]

def from_float(x: Any) -> float:
	if x is None: return x
	assert isinstance(x, float)
	return x

def from_str(x: Any) -> str:
	if x is None: return x
	if not  isinstance(x, str): return str(x)
	return x

def to_class(c: Type[T], x: Any) -> dict:
	assert isinstance(x, c)
	return cast(Any, x).to_dict()