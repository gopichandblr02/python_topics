"""
In Python, variables can be classified into global and local variables based on their scope and where they are defined.

1. Global Variables
A global variable is a variable that is defined outside any function or block, typically at the top level of the script.
Global variables can be accessed and modified from any function in the script.
They have global scope, which means they exist for the entire duration of the program.
Example:
"""
x = 10  # Global variable
def func1():
    print(x)  # Accessing global variable

def func2():
    global x  # Modify global variable
    x = 20  # Change global x

func1()  # Output: 10
func2()
print(x)  # Output: 20 (global x was modified)
"""
2. Local Variables
A local variable is a variable that is defined inside a function or block.
Local variables are only accessible within the function or block where they are defined and do not exist outside that scope.
They only exist during the execution of the function.
Example:
"""
def my_function():
    y = 5  # Local variable
    print(y)  # Accessing local variable

my_function()  # Output: 5
# print(y)  # This would raise an error because y is a local variable
"""
Key Differences:
Scope:
Global variables can be accessed from anywhere in the script.
Local variables can only be accessed within the function or block where they are defined.
Lifetime:
Global variables live throughout the program's execution.
Local variables are created when the function is called and destroyed when the function finishes execution.
Modifying Global Variables:
To modify a global variable inside a function, you need to declare it as global using the global keyword.
"""
x = 5  # Global variable
def modify_global():
    global x
    x = 10  # Modify global x
modify_global()
print(x)  # Output: 10

# Note: Without the global keyword, Python will create a new local variable instead of modifying the global one.