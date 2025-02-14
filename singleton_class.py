"""
A Singleton is a design pattern that ensures a class has only one instance and provides a global point of access to that instance.
This is useful when you want to control access to shared resources (e.g., a database or a configuration object).
In Python, there are several ways to implement a singleton. Here's one common way using the __new__ method:
Singleton Pattern Implementation:
"""
class Singleton:
    _instance = None  # Class variable to store the singleton instance

    def __new__(cls):
        if cls._instance is None:
            # If the instance doesn't exist, create one
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Test the Singleton pattern
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Output: True, both are the same instance
"""
Explanation:
__new__ method: The __new__ method is responsible for creating the instance of the class. In the Singleton pattern, 
we override this method to ensure that only one instance of the class is created.
If an instance already exists (cls._instance is None), we return the existing instance.
If no instance exists yet, we create a new one using super(Singleton, cls).__new__(cls), which calls the parent class’s 
__new__ method to create the instance.
Testing the Singleton:
When you run this code, both s1 and s2 will point to the same instance, as shown by the print(s1 is s2) statement, which
will return True. This confirms that only one instance of the Singleton class exists throughout the program.
"""

# Another Example with Logging Singleton:
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log = []  # Initialize log as an empty list
        return cls._instance

    def add_log(self, message):
        self.log.append(message)

    def show_logs(self):
        for msg in self.log:
            print(msg)

# Test the Logger Singleton
logger1 = Logger()
logger1.add_log("This is the first log.")

logger2 = Logger()
logger2.add_log("This is the second log.")

# Both logger1 and logger2 are the same instance
print(logger1 is logger2)  # Output: True

logger1.show_logs()
# Output:
# This is the first log.
# This is the second log.
"""
Explanation of the Logger Example:
Both logger1 and logger2 are the same instance, and changes made via either object reflect in the other, because they 
share the same log list.
When you call add_log or show_logs on either object, the logs are stored and displayed as if they are interacting with 
the same single instance.
This is the essence of the Singleton pattern: one shared instance across the program, which can be used to maintain 
consistency of data and ensure that only one instance is controlling shared resources.
"""
