"""
The math module in Python provides mathematical functions like square root, trigonometric functions, logarithms, and more.
To use it, you need to import it first:
"""
import math
# 1. Basic Mathematical Functions
# 1.1 math.sqrt() - Square Root
import math
print(math.sqrt(25))  # Output: 5.0

# 1.2 math.pow() - Exponentiation (x^y)
print(math.pow(2, 3))  # Output: 8.0

# 1.3 math.factorial() - Factorial of a Number
print(math.factorial(5))  # Output: 120

# 2. Rounding and Absolute Functions
# 2.1 math.floor() - Round Down
print(math.floor(3.9))  # Output: 3

# 2.2 math.ceil() - Round Up
print(math.ceil(3.1))  # Output: 4

#2.3 math.trunc() - Truncate Decimal Part
print(math.trunc(4.7))  # Output: 4

#2.4 math.fabs() - Absolute Value
print(math.fabs(-10.5))  # Output: 10.5

# 3. Trigonometric Functions
# 3.1 math.sin(), math.cos(), math.tan()

angle = math.radians(30)  # Convert degrees to radians
print(math.sin(angle))  # Output: 0.5
print(math.cos(angle))  # Output: 0.866...
print(math.tan(angle))  # Output: 0.577...

# 3.2 math.degrees() and math.radians()
print(math.degrees(math.pi))  # Output: 180.0
print(math.radians(180))  # Output: 3.1415...

# 4. Logarithmic and Exponential Functions
# 4.1 math.log() - Natural Logarithm (Base e)
print(math.log(10))  # Output: 2.302...

# 4.2 math.log10() - Logarithm Base 10
print(math.log10(100))  # Output: 2.0

# 4.3 math.exp() - Exponential Function (e^x)
print(math.exp(2))  # Output: 7.389...

# 5. Constants in math Module
"""
Constant	Description
math.pi	Value of π (3.14159...)
math.e	Euler’s number (2.71828...)
math.tau	Tau (2π)
math.inf	Positive infinity
math.nan	Not-a-Number (NaN)
"""
print(math.pi)   # Output: 3.14159...
print(math.e)    # Output: 2.71828...
print(math.inf)  # Output: inf
# 6. Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
print(math.gcd(12, 18))  # Output: 6
print(math.lcm(4, 5))    # Output: 20 (Python 3.9+)

# 7. Hyperbolic Functions
print(math.sinh(1))  # Output: 1.175...
print(math.cosh(1))  # Output: 1.543...
print(math.tanh(1))  # Output: 0.761...

# 8. Special Functions
# 8.1 math.isfinite(), math.isinf(), math.isnan()
print(math.isfinite(10))    # Output: True
print(math.isinf(math.inf)) # Output: True
print(math.isnan(math.nan)) # Output: True

