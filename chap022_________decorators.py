"""
Python Decorators
A decorator in Python is a function that modifies the behavior of another function without changing its code. Decorators
are often used for logging, access control, memoization, and other cross-cutting concerns.

1. Basic Function Decorator
A simple decorator that adds extra functionality before and after a function call.
"""

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator  # Equivalent to: say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, World!")

say_hello()
# Output:
# Before function execution
# Hello, World!
# After function execution
"""
2. Decorator with Arguments
To allow decorators to work with functions that take arguments, the wrapper function should accept *args and **kwargs.
"""
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))
# Output:
# Executing add with arguments (3, 5) {}
# 8
"""
3. Multiple Decorators
You can stack multiple decorators.
"""
def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        return func() + "!!!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def greet():
    return "hello"

print(greet())  # Output: HELLO!!!
"""
4. Decorator with Arguments (Parameterized Decorators)
A decorator that accepts an argument.
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # Executes 3 times
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!
"""
5. Class-Based Decorators
Instead of using a function, we can define a decorator as a class.
"""
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()
"""
6. Real-World Use Cases
a) Logging Decorator
"""
import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(2)
    print("Function completed")

slow_function()
# b) Authentication Decorator
def require_auth(func):
    def wrapper(user):
        if user != "admin":
            print("Access Denied")
            return
        return func(user)
    return wrapper

@require_auth
def access_dashboard(user):
    print(f"Welcome, {user}!")

access_dashboard("guest")  # Output: Access Denied
access_dashboard("admin")  # Output: Welcome, admin!
"""
When to Use Decorators?
✅ Code Reusability – Avoid repetitive code (e.g., logging, timing).
✅ Function Modification – Modify behavior without altering the original function.
✅ Separation of Concerns – Keeps business logic separate from auxiliary functions.

Python decorators make code cleaner, more readable, and reusable! 
"""