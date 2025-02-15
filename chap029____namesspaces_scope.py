"""
Namespaces and Scope in Python
In Python, namespaces and scope are crucial concepts related to variable visibility and lifetime. They define where and
how a variable can be accessed in your program.

1. What is a Namespace?
A namespace is a container where names (identifiers like variables, functions, classes) are mapped to objects (values).
Each namespace in Python is a dictionary where the key is the name and the value is the object that the name refers to.

Types of Namespaces:
Built-in Namespace: Contains built-in functions and exceptions (e.g., print(), int()).
Global Namespace: The namespace for all objects at the level of the main program or module.
Local Namespace: The namespace for objects within a function or method. Each function has its own local namespace.
Enclosing Namespace: The namespace in which a function is defined (used for closures). It’s the namespace surrounding a
nested function.
2. What is Scope?
Scope refers to the region in which a particular namespace is accessible. It defines where a variable can be used within
 the code.

Types of Scope:
Local Scope: Variables defined inside a function or block are in the local scope of that function. These variables are
only accessible within that function.
Enclosing Scope: This scope refers to any enclosing functions or methods, particularly in the case of nested functions.
Global Scope: Variables defined at the top level of a script or module are in the global scope. They are accessible
throughout the program, but not inside a function unless specified.
Built-in Scope: This scope contains Python's built-in functions and exceptions, and is always available.
The LEGB rule governs the scope lookup order:

L: Local scope
E: Enclosing scope (if nested functions exist)
G: Global scope
B: Built-in scope

3. Example of Namespaces and Scope
Let's look at an example to understand namespaces and scope in Python.

Example 1: Global and Local Scope
"""

x = 10  # Global variable

def foo():
    y = 5  # Local variable
    print("Inside foo, x =", x)  # Global variable
    print("Inside foo, y =", y)  # Local variable

foo()
print("Outside foo, x =", x)  # Global variable
# print("Outside foo, y =", y)  # Uncommenting this will raise an error: NameError: name 'y' is not defined

# Output
# Inside foo, x = 10
# Inside foo, y = 5
# Outside foo, x = 10
"""
Explanation:
x is defined globally, so it's accessible inside the function foo() and outside it.
y is defined locally inside foo(), so it's only accessible within that function. Trying to access y outside foo() would 
raise a NameError.
Example 2: Enclosing Scope (Nested Functions)
"""
def outer():
    outer_var = 'I am from outer'

    def inner():
        inner_var = 'I am from inner'
        print(outer_var)  # Accessing variable from enclosing (outer) scope
        print(inner_var)  # Accessing variable from local (inner) scope
    inner()
outer()
# I am from outer
# I am from inner
"""
Explanation:
outer_var is defined in the enclosing scope (in the outer() function) and is accessible inside the inner() function due 
to the enclosing scope rule.
inner_var is defined in the local scope of inner() and is only accessible inside inner().
Example 3: Built-in Scope
"""
print(len([1, 2, 3]))  # Using built-in function 'len'

# Uncommenting the line below will raise an error:
# print(input('Enter something: '))  # 'input' is not defined in this scope

"""
Explanation:
len() is a built-in function that is available in the built-in namespace.
If you try to use a built-in function or identifier (like input()) with the same name in your local or global namespace,
Python will use the one in the local or global namespace instead of the built-in.

4. Modifying Global Variables Inside a Function
If you want to modify a global variable inside a function, you must declare it as global within the function.

Example: Modifying Global Variable
"""
x = 10

def modify_global():
    global x
    x = 20

print("Before function call, x =", x)
modify_global()
print("After function call, x =", x)

# Before function call, x = 10
# After function call, x = 20
"""
Explanation:
The global keyword tells Python to use the global variable x inside the function. Without it, Python would create a new 
local variable x inside the function, which wouldn't affect the global x.
5. The nonlocal Keyword
In the case of nested functions, you can use the nonlocal keyword to modify variables in the enclosing (but not global) scope.

Example: Using nonlocal
"""
def outer():
    x = 10
    def inner():
        nonlocal x  # Modify x in the enclosing scope
        x = 20
        print("Inside inner, x =", x)

    inner()
    print("Inside outer, x =", x)
outer()
#
# Inside inner, x = 20
# Inside outer, x = 20

"""
Explanation:
The nonlocal keyword is used to modify the variable x in the enclosing scope (in this case, outer()), rather than 
creating a new local variable in inner().
6. The globals() and locals() Functions
globals() returns a dictionary of the global namespace.
locals() returns a dictionary of the local namespace.
Example: Using globals() and locals()
"""
x = 10  # Global variable

def foo():
    y = 20  # Local variable
    print("Global namespace:", globals())
    print("Local namespace:", locals())

foo()

# Global namespace: {'__name__': '__main__', '__doc__': None, 'x': 10, ...}
# Local namespace: {'y': 20}

"""
Summary:
Namespace: A mapping of variable names to objects.
Scope: The region where a variable is accessible.
LEGB Rule: The order Python looks for a variable is: Local > Enclosing > Global > Built-in.
Global variables can be modified inside a function using the global keyword.
Enclosing variables (from outer functions) can be modified using the nonlocal keyword in nested functions.
"""