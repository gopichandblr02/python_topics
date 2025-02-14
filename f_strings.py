#f-strings in Python
"""
Python offers a powerful feature called f-strings (formatted string literals) to simplify string formatting and interpolation.
f-strings is introduced in Python 3.6 it provides a concise and intuitive way to embed expressions and variables directly into strings.
 The idea behind f-strings is to make string interpolation simpler.
"""
# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Om'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")

# Prints today's date with help of datetime library
import datetime
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
# Output
# May 23, 2024
# Note: F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format().
"""
Quotation Marks in f-string in Python
To use any type of quotation marks with the f-string in Python we have to make sure that the quotation marks used inside
the expression are not the same as quotation marks used with the f-string.
"""
print(f"'GeeksforGeeks'")
print(f"""Geeks"for"Geeks""")
print(f'''Geeks'for'Geeks''')
# Output
# 'GeeksforGeeks'
# Geeks"for"Geeks
# Geeks'for'Geeks
"""
Evaluate Expressions with f-Strings in Python
We can also evaluate expressions with f-strings in Python. To do so we have to write the expression inside the curly braces
in f-string and the evaluated result will be printed as shown in the below code’s output.
"""
english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")
# Output
# Ram got total marks 219 out of 300
"""
Errors while using f-string in Python
Backslashes in f-string in Python
In Python f-string, Backslash Cannot be used in format string directly.
"""

#f"newline: {ord('\n')"
# Output
# Hangup (SIGHUP)
#   File "Solution.py", line 1
#     f"newline: {ord('\n')"
#     ^
# SyntaxError: f-string expression part cannot include a backslash

"""
However, we can put the backslash into a variable as a workaround though :
"""
newline = ord('\n')
print(f"newline: {newline}")
# Output
# newline: 10
"""
Inline comments in f-string in Python
We cannot use comments inside F-string expressions. It will give an error:

f"GeeksforGeeks is {5*2 + 3 #geeks-5} characters."
Output:
Hangup (SIGHUP)
  File "Solution.py", line 1
    f"GeeksforGeeks is {5*2 + 3 #geeks-5} characters."
    ^
SyntaxError: f-string expression part cannot include '#'
"""

"""
Printing Braces using f-string in Python
If we want to show curly braces in the f-string’s output then we have to use double curly braces in the f-string. N
ote that for each single pair of braces, we need to type double braces as seen in the below code.
"""
# Printing single braces
print(f"{{Hello, Geek}}")
# Printing double braces
print(f"{{{{Hello, Geek}}}}")
# Output
# {Hello, Geek}
# {{Hello, Geek}}
"""
Printing Dictionaries key-value using f-string in Python
While working with dictionaries, we have to make sure that if we are using double quotes (“) with the f-string then we 
have to use single quote (‘) for keys inside the f-string in Python and vice-versa. Otherwise, it will throw a syntax error.
"""
Geek = { 'Id': 112,
         'Name': 'Harsh'}

print(f"Id of {Geek["Name"]} is {Geek["Id"]}")
"""
Output
Hangup (SIGHUP)
  File "Solution.py", line 4
    print(f"Id of {Geek["Name"]} is {Geek["Id"]}")
                            ^
SyntaxError: invalid syntax
Using the same type of quotes for f-string and key
"""
Geek = { 'Id': 100,
         'Name': 'Om'}
print(f"Id of {Geek['Name']} is {Geek['Id']}")
# Output
# Id of Om is 100
"""
How to use .2f in Python?
.2f is used to format floating-point numbers to two decimal places when printing or formatting strings. For example:
"""
num = 3.14159
formatted = f"{num:.2f}"
print(formatted)  # Output: 3.14
"""
How to use F-string in JSON Python?
You can embed f-strings inside JSON strings by using them directly where needed:
"""
name = "Alice"
age = 30
json_data = f'{{ "name": "{name}", "age": {age} }}'
print(json_data)
# Output:
# { "name": "Alice", "age": 30 }
# Note the double curly braces {{ }} around the f-string to escape them in the JSON string.

"""
Can we use F-string in input Python?
Yes, you can use f-strings with input() to prompt the user and dynamically format strings based on input values:
"""

name = input("Enter your name: ")
message = f"Hello, {name}!"
print(message)
"""
What is the alternative to F-string in Python?
Before f-strings were introduced in Python 3.6, you could format strings using str.format() method or using % formatting
(old-style formatting). For example:
"""
name = "Alice"
age = 30
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence)
# Output:
# My name is Alice and I am 30 years old.
# However, f-strings are generally preferred due to their readability, simplicity, and efficiency.