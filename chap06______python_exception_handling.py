"""
1. Compile:
2. Build:
3. Runtime Error:
4. Compile time Error:
5. Syntax Error:
6. Compiler vs Interpreter:
7. Functional vs

"""
######################## 1. Python Exceptions ######################
"""
An exception is an unexpected event that occurs during program execution. For example,
divide_by_zero = 7 / 0
The above code causes an exception as it is not possible to divide a number by 0.
Python Logical Errors (Exceptions)
    Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.
    For instance, they occur when we
    1. try to open a file(for reading) that does not exist (FileNotFoundError)
    2. try to divide a number by zero (ZeroDivisionError)
    3. try to import a module that does not exist (ImportError) and so on.
    Whenever these types of runtime errors occur, 
    *****
    Python creates an exception object.
    *****
    If not handled properly, it prints a traceback to that error along with some details about why that error occurred.
    In Python, a traceback is a report that shows the sequence of function calls that led to an error.
    Let's look at how Python treats these errors:
"""

"""
*****
In Java, a stack trace is a report that shows the sequence of method calls that led to a particular point in the program's execution,
typically when an exception is thrown. It provides valuable information for debugging and understanding the flow of your code.
******
"""

divide_numbers = 7 / 0
print(divide_numbers)
"""
Traceback (most recent call last):
 File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
"""
############## Python Built-in Exceptions
"""
Illegal operations can raise exceptions. There are plenty of built-in exceptions in Python that are raised when corresponding errors occur.
We can view all the built-in exceptions using the built-in local() function as follows:
"""
print(dir(locals()['__builtins__']))
"""
Run Code
Here, locals()['__builtins__'] will return a module of built-in exceptions, functions, and attributes and dir allows us to list these attributes as strings.
Some of the common built-in exceptions in Python programming along with the error that cause them are listed below:
****************************
Exception	-> Cause of Error
****************************
AssertionError	Raised when an assert statement fails.
AttributeError	Raised when attribute assignment or reference fails.
EOFError	Raised when the input() function hits end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raise when a generator's close() method is called.
ImportError	Raised when the imported module is not found.
IndexError	Raised when the index of a sequence is out of range.
KeyError	Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
MemoryError	Raised when an operation runs out of memory.
NameError	Raised when a variable is not found in local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	Raised when system operation causes system related error.
OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	Raised when an error does not fall under any other category.
StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	Raised when interpreter detects internal error.
SystemExit	Raised by sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.
"""

######################## Python Error and Exception
"""
Errors represent conditions such as compilation error, syntax error, error in the logical part of the code, library incompatibility, infinite recursion, etc.
Errors are usually beyond the control of the programmer and we should not try to handle errors.
Exceptions can be caught and handled by the program.
Now we know about exceptions, we will learn about handling exceptions in the next tutorial.
"""

######################## 1. Python Exception Handling ######################
"""
Python try...except Block
Either except or finally is expected after try
"""
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
# Output: Error: Denominator cannot be 0.

############ Catching Specific Exceptions in Python
"""
For each try block, there can be zero or more except blocks. Multiple except blocks allow us to handle each exception differently.
The argument type of each except block indicates the type of exception that can be handled by it. For example,
"""
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")
# Output: Index Out of Bound

# Python try with else clause
"""
In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
For these cases, you can use the optional else keyword with the try statement.
Let's look at an example:
"""
# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# Output
"""
If we pass an odd number:
Enter a number: 1
Not an even number!
If we pass an even number, the reciprocal is computed and displayed.
Enter a number: 4
0.25
However, if we pass 0, we get ZeroDivisionError as the code block inside else is not handled by preceding except.
Enter a number: 0
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    reciprocal = 1/num
ZeroDivisionError: division by zero
Here, the assert statement in the code checks that num is an even number; if num is odd, it raises an AssertionError, triggering the except block.
Note: Exceptions in the else clause are not handled by the preceding except clauses.
"""

# Python try...finally....optional .....only one finally for one try....but can have many except
"""
In Python, the finally block is always executed no matter whether there is an exception or not.
Let's see an example,
"""

try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("This is finally block.")
# Output
"""
Error: Denominator cannot be 0.
This is finally block.
"""

################ Python Custom Exceptions ###################
"""
sometimes we may need to create our own custom exceptions that serve our purpose.
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
Here's the syntax to define custom exceptions,
"""
class CustomError(Exception):
    ...
    pass
try:
   ...
except CustomError:
    ...
"""
Here, CustomError is a user-defined error which inherits from the Exception class.
Note:
When we are developing a large Python program, it is a good practice to place all the user-defined exceptions that our program raises in a separate file.
Many standard modules define their exceptions separately as exceptions.py or errors.py (generally but not always).
"""

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

# Output
"""
If the user input input_num is greater than 18,
Enter a number: 45
Eligible to Vote
If the user input input_num is smaller than 18,
Enter a number: 14
Exception occurred: Invalid Age
In the above example, we have defined the custom exception InvalidAgeException by creating a new class that is derived from the built-in Exception class.
"""


################# Customizing Exception Classes ##################
"""
We can further customize this class to accept other arguments as per our needs.
To learn about customizing the Exception classes, you need to have the basic knowledge of Object-Oriented programming.
Visit Python Object Oriented Programming to learn about Object-Oriented programming in Python.
Let's see an example,
"""
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# Output
"""
Enter salary amount: 2000
Traceback (most recent call last):
  File "<string>", line 17, in <module>
    raise SalaryNotInRangeError(salary)
__main__.SalaryNotInRangeError: Salary is not in (5000, 15000) range
Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message.
Then, the constructor of the parent Exception class is called manually with the self.message argument using super().
The custom self.salary attribute is defined to be used later.
The inherited __str__ method of the Exception class is then used to display the corresponding message when SalaryNotInRangeError is raised.
"""


############# raise exception vs don't raise exception
############# try catch hierarchy
def method1(x,y):
    try:
        z=method2(x,y)
        print(z)
    except Exception as e:
        print('method1 failed')
def method2(x,y):
    try:
        return x/y
    except Exception as e:
        raise # If we raise, it goes to method1
        return 'method2 failed' # If we dont raise, it prints this
method1(10,0)