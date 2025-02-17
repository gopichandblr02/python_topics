Object-Oriented Programming is a programming paradigm that organizes code into classes and objects. It helps make code more modular, reusable, and easier to maintain.
### Basics of OOPs in python

### 1. object super class (default): 
In Python, every class implicitly inherits from a default superclass called object if no other superclass is explicitly defined. This means that every class in Python, whether it's a custom class or a built-in class, is a subclass of object by default.

This class provides basic methods that all Python objects inherit, such as __init__, __str__, __repr__, and others.
Why is object Important?
Even though the object class doesn’t define any attributes or methods by default, it ensures that every Python class has access to fundamental methods like:

1. __init__: The constructor (though you can override it).
2. __str__: A method to return a string representation of the object (often used for printing).
3. __repr__: A method to return a detailed string representation of the object.
4. __eq__, __ne__, etc.: Methods for comparing objects.
Example: Implicit Inheritance from object
Here’s an example to show how the default object superclass works in Python:

```
class MyClass:
    pass  # No superclass specified, so it implicitly inherits from object

# Creating an instance of MyClass
obj = MyClass()

# Checking the superclass of MyClass
print(MyClass.__bases__)  # Output: (<class 'object'>,)

# Checking the class of the object
print(type(obj))  # Output: <class '__main__.MyClass'>
```

In this example:

MyClass implicitly inherits from object because no superclass was specified.
MyClass.__bases__ confirms that its superclass is object.
Default Inheritance from object Example:
When you don't explicitly define a parent class, Python will automatically make your class a subclass of object. This is why MyClass inherits all the methods that are defined in object, like __str__ and __repr__.

```
class MyClass:
    def __init__(self, name):
        self.name = name

# Creating an object
obj = MyClass("Sample Object")

# Using the __str__ method inherited from object (or can be overridden)
print(obj)  # Output: <__main__.MyClass object at 0x7fbb2c755610>
```

In this case:

The print(obj) output shows the default string representation, which is the memory address of the object. This is the default behavior from the object class's __str__ method.
You can override this method to return a more user-friendly string representation.

```
class MyClass:
    def __init__(self, name):
        self.name = name
    
    # Override the __str__ method to return a custom string representation
    def __str__(self):
        return f"MyClass with name: {self.name}"

# Creating an object
obj = MyClass("Sample Object")

# Printing the object will now call the overridden __str__ method
print(obj)  # Output: MyClass with name: Sample Object
```

In this example:
The __str__ method is overridden to return a custom string representation when the object is printed.
This makes the output more user-friendly than the default representation.
Summary:
* Default Superclass (object): If no superclass is explicitly specified, all classes inherit from object by default.
* object Class: Provides default implementations of basic methods like __init__, __str__, __repr__, etc., which can be overridden.
* Customizing Behavior: You can override methods like __str__ to provide more meaningful output or customize other behaviors inherited from object.


### 2. Constructor: 
The __init__ method is a special method in Python that is automatically called when a new object is created from a class. It is called the constructor and is used to initialize the attributes of the object.

```
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
```

### 3. Default Constructor:
    * In Python, a default constructor refers to a constructor that is provided by Python automatically when no constructor is explicitly defined in a class.
    * If you don't define an __init__ method in a class, Python automatically provides a default constructor that doesn't take any parameters (except for self), and it does nothing.

```
class Person:
    pass  # No __init__ method defined, so Python provides a default constructor

# Creating an object
person1 = Person()

print(person1)  # Output: <__main__.Person object at 0x7f9f8e6f3f10>
```

Default Constructor (Automatically Provided by Python)
When you create a class without an __init__ method, Python automatically creates a default constructor for the class, which does nothing except initializing the object.

In this example:

Person has no __init__ method, so Python provides a default constructor that initializes the object.
The object is created successfully, but since there is no explicit constructor code, no attributes are initialized, and no special behavior occurs.
Custom Constructor (With __init__)
If you want to customize how objects are initialized (i.e., setting attributes when an object is created), you can define an __init__ method, which acts as a custom constructor.

Example with Custom Constructor:

```
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

# Creating an object with custom constructor
person1 = Person("Alice", 30)

print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
```

### 4. Inheritance and Superclass

  * Inheritance allows a class to inherit attributes and methods from another class (called the superclass or parent class). 
  * The child class can extend or override the behavior of the parent class. 
  * We use super() to call methods from a superclass in the child class.

```
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the constructor of the parent class (Animal)
        self.breed = breed
    def speak(self):  # Overriding the speak method
        print(f"{self.name} barks")
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # Output: Buddy barks
```

* Instance variables vs class variables
  * Instance Variables: These are variables that belong to a specific instance of the class. They are usually defined inside the __init__ method using self.
  * Class Variables: These are variables that belong to the class itself, not to any particular instance. They are shared among all instances of the class.

```
class Dog:
    species = "Canis familiaris"  # Class variable (shared by all instances)

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

dog1 = Dog("Buddy", 5)
dog2 = Dog("Bella", 3)

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Bella
```

### 5. Class Methods and Static Methods
    * Class Methods: These methods are bound to the class and not to the instance. They can modify class-level variables. Class methods are defined using the @classmethod decorator and take cls as the first parameter.
    * Static Methods: These methods do not depend on the class or the instance and are used when a method doesn't need to access or modify the class or instance attributes. Static methods are defined using the @staticmethod decorator.

```
class Car:
    # Class variable
    count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.count += 1  # Incrementing the count when a new car is created

    @classmethod
    def get_car_count(cls):
        return cls.count  # Accessing class variable

    @staticmethod
    def car_info(make, model):
        print(f"Car Make: {make}, Model: {model}")

# Creating instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Using class method
print(Car.get_car_count())  # Output: 2

# Using static method
Car.car_info("Toyota", "Corolla")  # Output: Car Make: Toyota, Model: Corolla

```

### 6. Overriding vs Overloading in python
In Python, overriding and overloading are two important concepts related to methods and operators, but they have different meanings and uses. Let's break down both:

1. Method Overriding:
Overriding happens when a subclass provides its own implementation of a method that is already defined in its superclass. The method in the subclass has the same name, same parameters, and performs a different function or behavior compared to the one in the superclass.

Key Points:

The method in the subclass overrides the method in the superclass.
It allows the subclass to change or extend the behavior of the inherited method.
The method signature (name, parameters) in the subclass must match the one in the superclass.
Example of Method Overriding:

```
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):  # This overrides the speak method of Animal class
        print("Dog barks")
class Cat(Animal):
    def speak(self):  # This overrides the speak method of Animal class
        print("Cat meows")
# Creating instances
dog = Dog()
cat = Cat()
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
```

When to Use Method Overriding:
To customize or change the behavior of a method in the child class.
To implement polymorphism, where the same method name behaves differently depending on the subclass object.

2. Method Overloading:
Overloading refers to the ability to define multiple methods with the same name but different parameters (either different number of parameters or different types of parameters). Python doesn't support traditional method overloading like in other languages such as Java or C++. Instead, Python allows default arguments and variable-length arguments to achieve similar functionality.
Using Default Arguments:

```
class Calculator:
    def add(self, a, b=0):  # Second parameter has a default value
        return a + b

calc = Calculator()
print(calc.add(5))      # Output: 5 (only one argument, default value for b is used)
print(calc.add(5, 3))   # Output: 8 (both arguments are provided)
```

Using *args (Variable-length Arguments):

```
class Calculator:
    def add(self, *args):
        return sum(args)
calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 3))       # Output: 8
print(calc.add(1, 2, 3, 4)) # Output: 10
```

Summary:
  * Overriding: Occurs when a subclass provides its own implementation of a method that is already defined in the superclass, allowing the subclass to change the method's behavior.
  * Overloading: Involves defining methods with the same name but different parameters (this is not natively supported in Python, but it can be simulated using default or variable-length arguments).

### ********* Add more here ***************


### Here are the core OOP concepts in Python:

#### 1. Classes and Objects
* Class: A blueprint for creating objects (instances). It defines properties (attributes) and methods (functions) that the object will have.
* Object: An instance of a class, created using the class blueprint.
Example:

```
class Car:
    def __init__(self, make, model):
        self.make = make  # Attribute
        self.model = model  # Attribute

    def start(self):  # Method
        print(f"The {self.make} {self.model} is starting!")

my_car = Car("Toyota", "Corolla")  # Object instantiation
my_car.start()  # Calling a method
```

#### 2. Encapsulation
Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. It also involves restricting access to some of an object's components to protect the object's integrity.

Private: Variables and methods that are not accessible outside the class.
Public: Variables and methods that are accessible from outside the class.
In Python, we use an underscore (_) to indicate "protected" members and a double underscore (__) for "private" members.

Example:

```
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.age = age  # Public attribute

    def greet(self):  # Public method
        print(f"Hello, my name is {self.__name} and I am {self.age} years old.")

person = Person("Alice", 30)
person.greet()
# print(person.__name)  # This will raise an AttributeError because __name is private
```

### public vs protected vs private variables in python encapsulation

In Python, encapsulation refers to the concept of restricting direct access to certain object attributes and methods, which helps to protect the internal state of an object from outside interference or misuse. Python doesn't strictly enforce access control like some other languages (e.g., Java or C++), but it provides naming conventions that indicate the intended level of access to a variable.

Here’s how public, protected, and private variables work in Python:

#### 1. Public Variables
Definition: These variables are accessible from outside the class.
Syntax: No leading underscores.
Example:

```
class MyClass:
    def __init__(self, value):
        self.value = value  # public variable

obj = MyClass(10)
print(obj.value)  # Accessing the public variable
```

Access: Public variables can be accessed directly from any part of the code.
Intended Usage: Use public variables when you want them to be available to external code or when there's no need for restricting access.
#### 2. Protected Variables
Definition: These variables are meant to be used only within the class and by subclasses (inherited classes). It’s a convention and doesn't provide strict access control.
Syntax: A single leading underscore _.
Example:

```
class MyClass:
    def __init__(self, value):
        self._value = value  # protected variable

obj = MyClass(10)
print(obj._value)  # Technically accessible, but not recommended
```

Access: Technically, protected variables can still be accessed directly from outside the class, but it’s considered a bad practice. It's an indication to other programmers that the variable is intended for internal use, or for subclass manipulation.
Intended Usage: Protected variables are typically used when you want the variable to be "protected" from outside interference but still allow subclasses to modify or access it.
#### 3. Private Variables
Definition: These variables are intended to be used only within the class. Access to them is strongly discouraged from outside the class, and Python provides name mangling to make it harder to access them directly.
Syntax: A double leading underscore __.
Example:

```
class MyClass:
    def __init__(self, value):
        self.__value = value  # private variable

    def get_value(self):
        return self.__value  # providing controlled access

obj = MyClass(10)
print(obj.get_value())  # Accessing private variable through a method
print(obj.__value)  # Will raise an AttributeError
```

Access: Python "name mangles" private variables to make them harder to access directly by changing their name (e.g., self.__value becomes _MyClass__value). However, it can still be accessed via the mangled name if absolutely needed, but it's not recommended.
Intended Usage: Private variables are typically used when you want to restrict external access to an attribute and provide controlled access through getter and setter methods.

#### Key Differences:
|Type   |Syntax	|   Access from Outside	| Intended Use                                                    |
|--------------|:-----------|:-------------|:----------------------------------------------------------------|
|Public	|No leading underscore	|Direct access	| Use when you want the variable to be freely accessible.         |
|Protected	|Single leading underscore (_)	|Access possible, but discouraged	| Intended for internal or subclass usage.                        |
|Private	|Double leading underscore (__)	|Access via name mangling (not recommended)| 	Intended to be fully hidden, with access only through methods. |

#### Additional Notes:
Python doesn’t strictly enforce access control. The naming conventions (_ for protected and __ for private) are simply guidelines and don’t prevent access.
You can still access private variables using their mangled name (e.g., _MyClass__value), but this goes against the purpose of encapsulation.
To provide controlled access to private variables, it’s common to use getter and setter methods.

#### 3. Inheritance
Inheritance allows one class (child class) to inherit the attributes and methods from another class (parent class). This helps to reuse code.
Example:

```
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog is a subclass of Animal
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()  # Defined in Dog
```

#### 4. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It also allows methods to have the same name but behave differently based on the object.
Example:

```
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

make_sound(cat)  # Outputs: Meow
make_sound(dog)  # Outputs: Woof
```

#### 5. Abstraction
Abstraction involves hiding complex implementation details and showing only the necessary features of an object. In Python, abstraction is typically achieved using abstract classes and methods. Python has an abc module for defining abstract base classes.
Example:

```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# dog = Animal()  # This will raise an error because you cannot instantiate an abstract class
dog = Dog()
dog.make_sound()  # Outputs: Woof!
```

#### Explanation:
The Animal class is an abstract class, and it contains an abstract method sound() which has no implementation.
Any class that inherits from Animal (like Dog and Cat) must implement the sound() method.
This allows us to hide the implementation details of how the sound() method works and only expose the interface (the fact that Animal has a sound() method).
Benefits in this Example:
Abstraction: We don't need to know exactly how Dog or Cat makes a sound; we just need to know that they have a sound() method.
Polymorphism: We can treat both Dog and Cat objects as Animal objects, calling sound() without caring about the specific type.
By using abstraction, we can design our code in a more modular, maintainable, and flexible way, making it easier to add new animals (or other features) without modifying existing code significantly.

Conclusion:
Abstraction allows programmers to focus on high-level functionalities, keeps systems simpler by hiding details, makes code more flexible and maintainable, and improves collaboration by enforcing a clear interface. It helps make code easier to understand, extend, and manage in large software systems.
