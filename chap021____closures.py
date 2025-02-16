"""
Python Closures
A closure in Python is a function that retains access to variables from its enclosing scope, even after the outer function
has finished executing. Closures are useful when you want to encapsulate behavior along with some associated data.
"""
# 1. Basic Closure Example

def outer_function(message):
    def inner_function():
        print(f"Message: {message}")  # `message` is captured from `outer_function`
    return inner_function  # Returns inner function without calling it
# Creating a closure
closure = outer_function("Hello, World!")
closure()  # Output: Message: Hello, World!
# Explanation:
"""
inner_function() captures the message variable from outer_function().
Even though outer_function() has finished executing, message is still accessible inside inner_function().

2. Closure with Arguments
"""
def multiplier(n):
    def multiply(x):
        return x * n  # Captures `n` from the outer scope
    return multiply

double = multiplier(2)  # Creates a closure that multiplies by 2
triple = multiplier(3)  # Creates a closure that multiplies by 3

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
# Explanation:
"""
multiplier(n) returns multiply(x), which remembers n even after multiplier() finishes execution.
3. Closure for Data Encapsulation
Closures can be used to create private-like variables.
"""
def counter():
    count = 0  # Private variable

    def increment():
        nonlocal count  # Modify `count` in the outer scope
        count += 1
        return count

    return increment

counter1 = counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2

counter2 = counter()
print(counter2())  # Output: 1 (Separate closure instance)
#Explanation:
"""
Each counter() call creates a new closure with an independent count variable.
nonlocal count allows modifying count inside the inner function.
4. Using Closures Instead of Classes
Instead of a class, we can use a closure to manage state.

Class-based approach:
"""
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
        return self.count

c = Counter()
print(c.increment())  # Output: 1
print(c.increment())  # Output: 2
# Closure-based approach:

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
print(c())  # Output: 1
print(c())  # Output: 2

# Both approaches work similarly, but closures are useful when you don’t need the full power of a class.
"""
5. Closure for Function Decorators
Closures are often used in decorators.
"""
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Explanation:
"""
decorator() returns wrapper(), which wraps the original function (say_hello()).
When to Use Closures?
✅ When you need stateful functions without using a class.
✅ When you need to hide data (like private variables).
✅ When using function decorators to modify behavior.

Closures make Python code more elegant and efficient in many scenarios! 
"""