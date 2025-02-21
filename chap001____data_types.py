"""
Python has several built-in data types, categorized into different groups. Here’s an overview with examples:
1. Numeric Types
a. Integer (int)
Represents whole numbers.
"""
x = 10  # Integer
print(type(x))  # Output: <class 'int'>

"""
b. Floating-Point (float)
Represents real numbers with decimal points.
"""
y = 10.5  # Float
print(type(y))  # Output: <class 'float'>
"""
c. Complex (complex)
Represents complex numbers.
"""
z = 3 + 4j  # Complex number
print(type(z))  # Output: <class 'complex'>
"""
2. Sequence Types
a. String (str)
Represents text enclosed in quotes.
"""
s = "Hello, Python!"
print(type(s))  # Output: <class 'str'>
"""
b. List (list)
A mutable ordered collection of items.
"""
my_list = [1, 2, 3, "Python", 4.5]
print(type(my_list))  # Output: <class 'list'>
"""
c. Tuple (tuple)
An immutable ordered collection of items.
"""
my_tuple = (1, 2, 3, "Python", 4.5)
print(type(my_tuple))  # Output: <class 'tuple'>
"""
d. Range (range)
Represents an immutable sequence of numbers.
"""
r = range(1, 10, 2)  # (start, stop, step)
print(list(r))  # Output: [1, 3, 5, 7, 9]
"""
3. Set Types
a. Set (set)
An unordered collection of unique elements.
"""
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>

"""
b. Frozen Set (frozenset)
An immutable version of a set.
"""
my_fset = frozenset([1, 2, 3, 4, 5])
print(type(my_fset))  # Output: <class 'frozenset'>
# my_fset.add(40)  # This will raise an AttributeError
"""
4. Mapping Type
Dictionary (dict)
A collection of key-value pairs.
"""
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(type(my_dict))  # Output: <class 'dict'>
"""
5. Boolean Type
Represents True or False.
"""
is_python_fun = True
print(type(is_python_fun))  # Output: <class 'bool'>
"""
6. Binary Types
a. Bytes (bytes)
Immutable sequence of bytes.
"""
b = bytes([65, 66, 67])
print(b)  # Output: b'ABC'
"""
b. Bytearray (bytearray)
Mutable sequence of bytes.
"""
ba = bytearray([65, 66, 67])
ba[0] = 68
print(ba)  # Output: bytearray(b'DBC')
"""
c. Memoryview (memoryview)
Provides memory-efficient handling of binary data.
"""
mv = memoryview(bytes([1, 2, 3, 4, 5]))
print(mv[0])  # Output: 1
"""
7. None Type
Represents the absence of a value.
"""
x = None
print(type(x))  # Output: <class 'NoneType'>
