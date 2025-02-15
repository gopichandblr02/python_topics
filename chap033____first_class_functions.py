"""
In Python, first-class functions means that functions are treated as first-class citizens. This means that:

* Functions can be assigned to variables.
* Functions can be passed as arguments to other functions.
* Functions can be returned from other functions.
* Functions can be stored in data structures like lists, dictionaries, etc.
Essentially, Python allows you to treat functions as objects, which is a powerful concept and forms the basis of functional
programming in Python.
1. Assigning Functions to Variables
You can assign a function to a variable and use the variable to call the function.
"""
def greet(name):
    return f"Hello, {name}!"
# Assigning the function to a variable
say_hello = greet
# Now we can call the function using the variable
print(say_hello("Alice"))  # Output: Hello, Alice!
"""
2. Passing Functions as Arguments
You can pass functions as arguments to other functions. This is commonly seen with higher-order functions like map(), filter(), and reduce().
"""
def apply_function(func, value):
    return func(value)
def square(x):
    return x * x
# Passing the square function as an argument
result = apply_function(square, 5)
print(result)  # Output: 25
"""
3. Returning Functions from Other Functions
You can define a function that returns another function. This is often used in closures and decorators.
"""
def outer():
    def inner():
        return "I'm the inner function!"
    return inner  # Returning the inner function
# Getting the inner function
inner_function = outer()
# Calling the inner function
print(inner_function())  # Output: I'm the inner function!
"""
4. Storing Functions in Data Structures
You can store functions in lists, dictionaries, or other data structures.
"""
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
# Storing functions in a list
operations = [add, subtract]
# Using the stored functions
print(operations[0](10, 5))  # Output: 15 (add)
print(operations[1](10, 5))  # Output: 5  (subtract)
"""
Practical Example: Using Functions as First-Class Citizens
A common use case of first-class functions is in decorators. A decorator is a function that modifies the behavior of another function.
"""
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

# The say_hello function is now wrapped by the decorator
say_hello()
# Output:
# Before calling the function.
# Hello, World!
# After calling the function.
"""
Key Points:
Functions as Arguments: You can pass functions as arguments to other functions, which allows for higher-order functions.
Functions as Return Values: Functions can return other functions, making it easier to create dynamic behavior (like closures).
Assigning Functions to Variables: You can assign a function to a variable and use it later, which makes the code more flexible.
Storing Functions in Data Structures: Functions can be stored in data structures and accessed as needed, which is useful for
cases like callbacks or event handling.
First-class functions make Python very versatile and allow for more functional programming approaches.
"""
