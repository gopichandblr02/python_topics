######################## 1. Variables   ########################

"""In Python, a variable is not a memory container itself but a symbolic name (or reference) that points to an object in memory.
Memory allocation is handled automatically by Python's memory manager, abstracting low-level details from the programmer. """
# Variable Creation
"""Variables are created the moment you first assign a value to them using the assignment operator (=).
Syntax: The basic syntax is variable_name = value."""
# python
age = 30           # Assigns the value 30 to the variable name 'age'
greeting = "Hello" # Assigns the string "Hello" to the variable name 'greeting'
# Dynamic Typing:
"""Python is a dynamically typed language, so you do not need to declare the variable's data type explicitly.
 Python infers the type from the assigned value at runtime.
"""
# Reference Binding: When you execute age = 30, Python:
"""Creates an integer object with the value 30 in the computer's memory (specifically, on the heap).
Creates a name age in the current namespace (e.g., the function's stack frame).
Binds the name age to the memory address (reference) of that object."""
# Memory Allocation
"""Memory management in Python is automatic and involves several key mechanisms:
Automatic Management: Python's memory manager handles the allocation and deallocation of memory,
so developers don't use explicit commands like malloc or free."""
# Heap and Stack:
"""Heap Memory: All Python objects (e.g., integers, strings, lists, dictionaries, custom objects) are stored in a 
private heap space. This allows objects to persist as long as they are needed and accessible across different function scopes.
Stack Memory: The stack is primarily used for function calls and storing the local variable names (references) within those function scopes."""
# Reference Counting: Python uses reference counting as a primary garbage collection technique.
"""Every object in memory has a reference counter that tracks how many variables are pointing to it.
When a variable is assigned a new value, the count for the old object decreases. When the reference count of an object 
drops to zero, Python automatically deallocates its memory, making it available for reuse."""
# Memory Optimization: Python employs optimization strategies to reuse existing objects:
"""
1. Integer Caching: Python pre-allocates and caches integer objects in the range of -5 to 256 at startup. 
Any variables assigned a value within this range will likely point to the same existing object in memory.
2. String Interning: Similar optimization is used for identical string literals to save memory.
Memory Pools: The Python interpreter uses special-purpose memory allocators (like pymalloc) for small objects to manage
memory efficiently and reduce the overhead of calling the system's malloc for every tiny allocation.
3. You can inspect the memory address (identity) of any object using the built-in id() function.
"""

"""In programming, a variable is a container (storage area) to hold data. For example,"""
# assign value to site_name variable
site_name = 'programiz.pro'
print(site_name)
# Output: programiz.pro
"""
Note: Python is a type-inferred language, so you don't have to explicitly define the variable type. 
It automatically knows that programiz.pro is a string and declares the site_name variable as a string.
"""
a, b, c = 5, 3.2, 'Hello'
print (a)  # prints 5
print (b)  # prints 3.2
print (c)  # prints Hello
x = y  = 'programiz.com'
print (x)  # prints programiz.com
print (y)  # prints programiz.com

# Creating an empty set
my_set = set()
print(type(my_set))
# Output: <class 'set'>

my_set = {1, 2, 3, 4}
print(my_set,type(my_set))
# {1, 2, 3, 4} <class 'set'>

# Creating an empty dictionary
my_dict = {}
print(type(my_dict))
# Output: <class 'dict'>

a={}
print(a,type(a))
# {} <class 'dict'>

"""
In Python, global variables do not reside in a specific "stack frame" in the same way local variables do. 
Instead, they are stored within the global namespace, which is associated with the module (file) where they are defined
"""



######################### 2. Python Literals ###########################
site_name = 'programiz.com'
"""
In the above expression, site_name is a variable, and 'programiz.com' is a literal.
1. Python Numeric Literals
Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.
        1. Integer Literals
        Integer literals are numbers without decimal parts. It also consists of negative numbers. For example, 5, -11, 0, 12, etc.
        2. Floating-Point Literals
        Floating-point literals are numbers that contain decimal parts.
        Just like integers, floating-point numbers can also be both positive and negative. For example, 2.5, 6.76, 0.0, -9.45, etc.
        3. Complex Literals
        Complex literals are numbers that represent complex numbers.
        Here, numerals are in the form a + bj, where a is real and b is imaginary. For example, 6+9j, 2+3j.

2. Python String Literals
        In Python, texts wrapped inside quotation marks are called string literals..
        "This is a string."
        We can also use single quotes to create strings.
        'This is also a string.'
"""
# Boolean literals
is_pass = True
print(is_pass)
# Output: True
# Character literals
some_character = 'S'
# Special literals
value = None
print(value)
# Output: None
# Collections literals
# list literal
fruits = ["apple", "mango", "orange"]
print(fruits)

# tuple literal
numbers = (1, 2, 3)
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'}
print(vowels)

# ['apple', 'mango', 'orange']
# (1, 2, 3)
# {'a': 'apple', 'b': 'ball', 'c': 'cat'}
# {'e', 'a', 'o', 'i', 'u'}


######################### 3. Type Conversion ###########################
"""
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.
There are two types of type conversion in Python.
Implicit Conversion - automatic type conversion
Explicit Conversion - manual type conversion
We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
"""
a = 10
b = a
b += 1  # If integers were mutable, 'a' would also change, which is undesirable.

# Implicit Conversion Example
integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))
# Note: It is because Python always converts smaller data types to larger data types to avoid the loss of data.

# Explicit Conversion Example (is also called Type Casting)
# In Type Casting, loss of data may occur as we enforce the object to a specific data type.
num_string = '12'
num_integer = 23
print("Data type of num_string before Type Casting:",type(num_string))
# explicit type conversion
num_string = int(num_string)
print("Data type of num_string after Type Casting:",type(num_string))
num_sum = num_integer + num_string
print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))