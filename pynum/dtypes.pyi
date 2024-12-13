# defined at `./pynum/src/dtypes.cpp`

from typing import Union

class int8:
  def __init__(self, value:int) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: Union["int8",int]) -> "int8": ...
  def __sub__(self, other: Union["int8",int]) -> "int8": ...
  def __mul__(self, other: "int8") -> "int8": ...
  def __truediv__(self, other: "int8") -> "int8": ...
  def __floordiv__(self, other: "int8") -> "int8": ...
  def __mod__(self, other: "int8") -> "int8": ...
  def __pos__(self) -> "int8": ...
  def __neg__(self) -> "int8": ...
  def __abs__(self) -> "int8": ...
  def nbits(self) -> int: ...
  def toInt(self) -> int: ...

class int16:
  def __init__(self, value:int) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: "int16") -> "int16": ...
  def __sub__(self, other: "int16") -> "int16": ...
  def __mul__(self, other: "int16") -> "int16": ...
  def __truediv__(self, other: "int16") -> "int16": ...
  def __floordiv__(self, other: "int16") -> "int16": ...
  def __mod__(self, other: "int16") -> "int16": ...
  def nbits(self) -> int: ...
  def toInt(self) -> int: ...

class int32:
  def __init__(self, value:int) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: "int32") -> "int32": ...
  def __sub__(self, other: "int32") -> "int32": ...
  def __mul__(self, other: "int32") -> "int32": ...
  def __truediv__(self, other: "int32") -> "int32": ...
  def __floordiv__(self, other: "int32") -> "int32": ...
  def __mod__(self, other: "int32") -> "int32": ...
  def __pow__(self, other: Union[int,float,"int32"]) -> "int32": ...
  def nbits(self) -> int: ...
  def toInt(self) -> int: ...

class int64:
  def __init__(self, value:int) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: "int64") -> "int64": ...
  def __sub__(self, other: "int64") -> "int64": ...
  def __mul__(self, other: "int64") -> "int64": ...
  def __truediv__(self, other: "int64") -> "int64": ...
  def __floordiv__(self, other: "int64") -> "int64": ...
  def __mod__(self, other: "int64") -> "int64": ...
  def nbits(self) -> int: ...
  def toInt(self) -> int: ...

class float32:
  def __init__(self, value:float) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: "float32") -> "float32": ...
  def __sub__(self, other: "float32") -> "float32": ...
  def __mul__(self, other: "float32") -> "float32": ...
  def __truediv__(self, other: "float32") -> "float32": ...
  def __floordiv__(self, other: "float32") -> "float32": ...
  def __mod__(self, other: "float32") -> "float32": ...
  def nbits(self) -> int: ...
  def toFloat(self) -> float: ...

class float64:
  def __init__(self, value:float) -> None: ...
  def __repr__(self) -> str: ...
  def __add__(self, other: "float64") -> "float64": ...
  def __sub__(self, other: "float64") -> "float64": ...
  def __mul__(self, other: "float64") -> "float64": ...
  def __truediv__(self, other: "float64") -> "float64": ...
  def __floordiv__(self, other: "float64") -> "float64": ...
  def __mod__(self, other: "float64") -> "float64": ...
  def nbits(self) -> int: ...
  def toFloat(self) -> float: ...
