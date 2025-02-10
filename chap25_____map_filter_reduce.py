"""
In this article, we will study Map, Reduce, and Filter Operations in Python. These three operations are paradigms of functional programming.
Map Function in Python
The map () function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple, etc.).
"""

# Function to return double of n
def double(n):
    return n * 2
# Using map to double all numbers
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))

# Reduce Function in Python
"""
The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned 
in the sequence passed along.This function is defined in “functools” module.
"""

import functools
# Define a list of numbers
numbers = [1, 2, 3, 4]
# Use reduce to compute the product of list elements
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)
## without lambda
def multiply(x, y):
  return x * y
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(multiply, numbers)
print(product)

## Filter Function in Python
"""
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 
"""
# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)
print("Even numbers:", list(even_numbers))

# [10, 12, 14, 16]
# Product of list elements: 24
# 120
# Even numbers: [2, 4, 6, 8, 10]