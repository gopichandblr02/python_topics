"""
Class Method vs Static Method in Python
Both @classmethod and @staticmethod are used to define methods inside a class that are not regular instance methods. However, they have different purposes and behaviors.
1. @classmethod
It takes the class (cls) as the first parameter.
It can modify the class state (class variables).
It is called on the class itself rather than an instance.
Example: @classmethod
"""
class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def set_company(cls, new_company):
        cls.company = new_company  # Modifies the class variable

# Using the class method
Employee.set_company("NewTech")
print(Employee.company)  # Output: NewTech

"""
Use Cases of @classmethod
✅ When you need to modify class-level attributes
✅ When you want an alternative constructor
"""

"""
2. @staticmethod
It does not take self or cls as a parameter.
It behaves like a regular function but resides inside a class.
It does not modify the class or instance.
Example: @staticmethod
"""
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_even(num):
        return num % 2 == 0

# Using static methods
print(MathOperations.add(10, 5))   # Output: 15
print(MathOperations.is_even(4))   # Output: True
"""
Use Cases of @staticmethod
✅ When a method does not depend on instance or class variables
✅ When you want utility/helper methods inside a class
"""

"""
Feature	                          @classmethod	                    @staticmethod
Takes self?	                        ❌ No	                            ❌ No
Takes cls?	                        ✅ Yes	                            ❌ No
Can modify class variables?	        ✅ Yes	                            ❌ No
Can modify instance variables?	    ❌ No	                            ❌ No
Used for alternative constructors?	✅ Yes                           	❌ No
Used for utility methods?	        ❌ No	                            ✅ Yes
"""

# Example: Class Method vs Static Method
class Car:
    car_count = 0  # Class variable

    def __init__(self, model):
        self.model = model
        Car.car_count += 1

    @classmethod
    def update_car_count(cls, count):
        cls.car_count = count  # Updates class variable

    @staticmethod
    def is_luxury_car(model):
        return model in ["BMW", "Mercedes", "Audi"]

# Using class method
Car.update_car_count(5)
print(Car.car_count)  # Output: 5

# Using static method
print(Car.is_luxury_car("BMW"))  # Output: True
print(Car.is_luxury_car("Toyota"))  # Output: False

"""
When to Use Which?
Use @classmethod when working with class variables or creating alternative constructors.
Use @staticmethod when a method is logically related to the class but does not use class or instance attributes.
"""
