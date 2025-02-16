"""
Tuple in Python
A tuple is an immutable (unchangeable) ordered collection in Python. It is similar to a list but cannot be modified after creation.
Tuples are defined using parentheses ().
"""
# Empty tuple
empty_tuple = ()
# Tuple with elements
numbers = (1, 2, 3, 4, 5)
# Tuple with different data types
mixed = (10, "hello", 3.14, True)
# Tuple with one element (comma is required)
single_element = (5,)
# Tuple without parentheses (Implicit tuple)
implicit_tuple = 10, 20, 30
print(numbers)  # Output: (1, 2, 3, 4, 5)
print(single_element)  # Output: (5,)
print(implicit_tuple)  # Output: (10, 20, 30)
"""
Tuple Methods
Since tuples are immutable, they have only a few built-in methods.
1. count() - Counts occurrences of an element
"""
t = (1, 2, 3, 2, 2, 4, 5)
print(t.count(2))  # Output: 3
"""
2. index() - Finds the first index of an element
"""
t = (10, 20, 30, 40, 50)
print(t.index(30))  # Output: 2
"""
Tuple Operations
1. Accessing Elements
"""
t = (10, 20, 30, 40)
print(t[0])   # Output: 10
print(t[-1])  # Output: 40
"""
2. Slicing
"""
t = (1, 2, 3, 4, 5)
print(t[1:4])   # Output: (2, 3, 4)
print(t[:3])    # Output: (1, 2, 3)
print(t[::2])   # Output: (1, 3, 5)
"""
3. Tuple Concatenation & Repetition
"""
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)   # Output: (1, 2, 3, 4, 5, 6)
print(a * 2)   # Output: (1, 2, 3, 1, 2, 3)
# 4. Checking Membership
t = (10, 20, 30, 40)
print(20 in t)   # Output: True
print(50 in t)   # Output: False
# 5. Iterating Over a Tuple
t = (10, 20, 30)
for item in t:
    print(item)
# 6. Tuple Unpacking
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # Output: 1 2 3

###########################################
############# NamedTuple in Python #################
###########################################
"""
A NamedTuple is a subclass of tuple that allows for named fields, making code more readable and self-documenting. 
It is defined in the collections module.
Creating a NamedTuple
You can define a NamedTuple using collections.namedtuple().
"""

from collections import namedtuple
# Define a NamedTuple
Person = namedtuple("Person", ["name", "age", "city"])
# Create an instance
p1 = Person(name="Alice", age=30, city="New York")
print(p1,type(Person),type(p1))  # Output: Person(name='Alice', age=30, city='New York') <class 'type'> <class '__main__.Person'>
"""
Accessing Elements
You can access elements in three ways:
"""
# 1. By Attribute Name
print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30
print(p1.city)  # Output: New York

# 2. By Index
print(p1[0])  # Output: Alice
print(p1[1])  # Output: 30
print(p1[2])  # Output: New York
# 3. By Unpacking
name, age, city = p1
print(name, age, city)  # Output: Alice 30 New York

# Methods of NamedTuple
# 1. _asdict() - Convert NamedTuple to Dictionary
print(p1._asdict())
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# 2. _replace() - Create a New Instance with Modified Values
p2 = p1._replace(age=35)
print(p2)  # Output: Person(name='Alice', age=35, city='New York')
# 3. _fields - Get Field Names
print(Person._fields)  # Output: ('name', 'age', 'city')
# 4. _make() - Create NamedTuple from an Iterable
data = ("Bob", 28, "Los Angeles")
p3 = Person._make(data)
print(p3)  # Output: Person(name='Bob', age=28, city='Los Angeles')

"""
Feature                 NamedTuple                  Regular Tuple
Access by name	        ✅ Yes	                    ❌ No
Readability	            ✅ High                  	❌ Low
Mutability	            ❌ Immutable	            ❌ Immutable
Dictionary Conversion	✅ Yes (_asdict())	        ❌ No
"""

from collections import namedtuple
Employee = namedtuple("Employee", ["id", "name", "salary"])
e1 = Employee(id=101, name="John", salary=50000)
e2 = Employee(id=102, name="Jane", salary=60000)
print(e1.name, e1.salary)  # Output: John 50000
# Alternative: typing.NamedTuple (Modern Approach)
# Python 3.6+ introduced typing.NamedTuple with type annotations.

from typing import NamedTuple
class Car(NamedTuple):
    brand: str
    model: str
    year: int
car1 = Car(brand="Toyota", model="Camry", year=2022)
print(car1.brand)  # Output: Toyota

# This method is more Pythonic and supports static type checking.