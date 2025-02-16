"""
Lambda Functions in Python (Anonymous Functions)
A lambda function in Python is a small, anonymous function that can have multiple arguments but only one expression.
It is often used for short, throwaway functions where defining a full function is unnecessary.
lambda arguments: expression
1. Basic Lambda Function
"""
square = lambda x: x * x
print(square(5))  # Output: 25
#Equivalent to:
def square(x):
    return x * x
# 2. Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10
#Equivalent to:
def add(a, b):
    return a + b
"""
3. Using Lambda with map()
Applies a function to all items in an iterable.
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
"""
4. Using Lambda with filter()
Filters elements based on a condition.
"""
numbers = [10, 25, 30, 45, 50]
greater_than_25 = list(filter(lambda x: x > 25, numbers))
print(greater_than_25)  # Output: [30, 45, 50]
"""
5. Using Lambda with sorted()
Sorting a list of tuples by the second value.
"""
pairs = [(1, 2), (3, 1), (5, 4)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(3, 1), (1, 2), (5, 4)]
"""
6. Using Lambda in reduce()
Computes a cumulative sum using reduce() from functools.
"""
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15
"""
7. Lambda Inside a Function
Returning a lambda function from another function.
"""
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))  # Output: 10
# 8. Lambda for Conditional Expressions
max_number = lambda a, b: a if a > b else b
print(max_number(10, 20))  # Output: 20
"""
Why Use Lambda Functions?
✅ Concise and readable for simple functions.
✅ Useful for higher-order functions like map(), filter(), and sorted().
✅ Reduces the need for defining small functions explicitly.

However, avoid using lambdas for complex logic—regular functions (def) are more readable and maintainable! 
"""