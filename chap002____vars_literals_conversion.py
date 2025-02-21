######################## 1. Variables   ########################

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