def func(a=3):
    return a**2
x=func()
print(x)   #9
y=func(100)
print(y)  #10000


#######################################################################################################################
"""
Python Functions with Examples
Functions in Python are reusable blocks of code that perform a specific task. They help in organizing code, 
improving readability, and reducing redundancy.

1. Defining a Function
Functions are defined using the def keyword.
"""

def greet():
    print("Hello, Welcome to Python!")
greet()  # Calling the function

# Output:
# Hello, Welcome to Python!
"""
2. Function with Parameters
Functions can take arguments to perform operations dynamically.
"""

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
"""
3. Default Parameter Value
If a parameter is not provided, a default value is used.
"""

def greet(name="User"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, User!
"""
4. Keyword Arguments
You can specify arguments using their names.
"""

def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(age=30, name="John")
# Output:
# Name: John, Age: 30
"""
5. Arbitrary Arguments (*args)
Used when the number of arguments is unknown.
"""

def sum_numbers(*numbers):
    return sum(numbers)

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15
"""
6. Arbitrary Keyword Arguments (**kwargs)
Used to pass multiple keyword arguments as a dictionary.
"""
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
"""
7. Returning Multiple Values
A function can return multiple values using tuples.
"""
def math_operations(a, b):
    return a + b, a - b, a * b, a / b

add, sub, mul, div = math_operations(10, 2)
print(add, sub, mul, div)  # Output: 12 8 20 5.0
"""
8. Lambda (Anonymous) Functions
A compact way to write small functions.
"""
square = lambda x: x * x
print(square(5))  # Output: 25
"""
9. Function with map()
Applies a function to all items in an iterable.
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
"""
10. Function with filter()
Filters elements based on a condition.
"""
numbers = [10, 25, 30, 45, 50]
greater_than_25 = list(filter(lambda x: x > 25, numbers))
print(greater_than_25)  # Output: [30, 45, 50]
"""
11. Recursive Function
A function that calls itself.
"""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
"""
12. Nested Functions
Functions defined inside another function.
"""
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()
outer()
# Output:
# Outer function
# Inner function

"""
13. Function with nonlocal Keyword
Used to modify variables from the outer function.
"""
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
# Output:
# Inner: inner
# Outer: inner
