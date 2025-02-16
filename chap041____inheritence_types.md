In Python, inheritance allows one class (child or subclass) to inherit the attributes and methods from another class (parent or superclass). There are different types of inheritance based on the number of parent classes involved and the relationships between them.

### Types of Inheritance in Python:
#### 1. Single Inheritance
In single inheritance, a subclass inherits from only one parent class.
Example:
```
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inheriting from Animal class
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Inherited method from Animal
dog.bark()   # Method from Dog
```
#### 2. Multiple Inheritance

In multiple inheritance, a subclass can inherit from more than one parent class. The subclass will inherit attributes and methods from all parent classes.

Example:
```
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Pet:
    def play(self):
        print("Pet is playing")

class Dog(Animal, Pet):  # Inheriting from both Animal and Pet
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Inherited from Animal
dog.play()   # Inherited from Pet
dog.bark()   # Defined in Dog
```
#### 3. Multilevel Inheritance

In multilevel inheritance, a subclass inherits from another subclass. This creates a chain of inheritance, where a class inherits from a class that is already a subclass.

Example:
```
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

class Puppy(Dog):  # Puppy inherits from Dog, which inherits from Animal
    def whine(self):
        print("Puppy is whining")

puppy = Puppy()
puppy.speak()  # Inherited from Animal
puppy.bark()   # Inherited from Dog
puppy.whine()  # Defined in Puppy
```
#### 4. Hierarchical Inheritance

In hierarchical inheritance, multiple subclasses inherit from a single parent class. All the subclasses can access the attributes and methods of the parent class.

Example:
```
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inheriting from Animal
    def bark(self):
        print("Woof!")

class Cat(Animal):  # Inheriting from Animal
    def meow(self):
        print("Meow!")

dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()

cat = Cat()
cat.speak()  # Inherited from Animal
cat.meow()
```
#### 5. Hybrid Inheritance

Hybrid inheritance is a combination of two or more types of inheritance. It may involve any mix of single, multiple, multilevel, or hierarchical inheritance.

Example (Multiple + Multilevel):
```
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Mammal(Animal):  # Inheriting from Animal
    def walk(self):
        print("Mammal walks")

class Dog(Mammal):  # Inheriting from Mammal (which is inherited from Animal)
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Inherited from Animal
dog.walk()   # Inherited from Mammal
dog.bark()   # Defined in Dog

```
#### Method Resolution Order (MRO) in Multiple Inheritance
In Python, when you use multiple inheritance, the Method Resolution Order (MRO) determines the order in which the classes are checked to find the method or attribute.

You can check the MRO for a class by using:

print(Dog.mro())
This will return the method resolution order for the Dog class in a multiple inheritance situation, showing the order in which Python searches for methods and attributes.

Summary of Inheritance Types:
Single Inheritance: One class inherits from a single parent.
Multiple Inheritance: One class inherits from multiple parent classes.
Multilevel Inheritance: A class inherits from a subclass.
Hierarchical Inheritance: Multiple subclasses inherit from a single parent class.
Hybrid Inheritance: A combination of multiple types of inheritance.