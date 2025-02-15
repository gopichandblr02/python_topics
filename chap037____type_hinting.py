"""
Type hinting in Python is a feature that allows you to specify the expected data types of variables, function parameters,
and return values. It improves code readability and helps with debugging and static analysis. Type hints do not enforce
type checking at runtime but can be checked using tools like mypy.
Basic Type Hinting Examples
1. Variables
You can specify types for variables using :
"""
x: int = 10
y: float = 3.14
name: str = "Alice"
is_active: bool = True
"""
2. Function Parameters and Return Types
You can specify the expected types of function parameters and return values using ->
"""
def add(a: int, b: int) -> int:
    return a + b
print(add(3, 5))  # Output: 8
"""
3. Using Optional for Nullable Values
If a parameter or return value can be None, use Optional
"""
from typing import Optional
def greet(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, Guest!"
print(greet("John"))  # Output: Hello, John!
print(greet(None))    # Output: Hello, Guest!
"""
4. Using List, Tuple, Set, and Dict
You can specify generic types for collections
"""
from typing import List, Tuple, Set, Dict
numbers: List[int] = [1, 2, 3]
coordinates: Tuple[float, float] = (10.5, 20.3)
unique_ids: Set[int] = {101, 102, 103}
user_data: Dict[str, int] = {"Alice": 25, "Bob": 30}
"""
5. Using Union for Multiple Possible Types
If a variable or parameter can have multiple types, use Union
"""
from typing import Union
def get_length(value: Union[str, list]) -> int:
    return len(value)
print(get_length("Hello"))  # Output: 5
print(get_length([1, 2, 3]))  # Output: 3
"""
6. Using Any for Any Type
Use Any when a variable can be of any type
"""
from typing import Any
def process_data(data: Any) -> None:
    print(f"Processing: {data}")
process_data("Hello")
process_data(123)
process_data([1, 2, 3])
"""
7. Using Callable for Function Types
Specify a function type using Callable
"""

from typing import Callable
def apply_func(x: int, func: Callable[[int], int]) -> int:
    return func(x)
print(apply_func(5, lambda n: n * 2))  # Output: 10
"""
8. Using TypeAlias for Custom Type Names
You can create a type alias to make code more readable
"""
from typing import TypeAlias
Coordinates: TypeAlias = Tuple[float, float]

def get_location() -> Coordinates:
    return (40.7128, -74.0060)
print(get_location())  # Output: (40.7128, -74.0060)
"""
9. Using TypedDict for Dictionary Structures
You can define a dictionary with specific key-value types
"""
from typing import TypedDict
class User(TypedDict):
    name: str
    age: int
user: User = {"name": "Alice", "age": 30}
print(user)
"""
10. Using Literal for Specific Values
Use Literal when a variable must have specific values
"""
from typing import Literal
def set_status(status: Literal["active", "inactive", "pending"]) -> str:
    return f"Status set to {status}"
print(set_status("active"))  # Valid
# print(set_status("unknown"))  # Type checker will warn