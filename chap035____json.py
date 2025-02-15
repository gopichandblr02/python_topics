"""
Python JSON Methods
Python provides the json module for working with JSON data. The json module allows you to parse JSON data,
convert Python objects to JSON format, and more.
Here are the common methods in Python's json module:
1. json.dumps() – Convert Python Object to JSON String
Converts a Python object (like a dictionary or list) into a JSON string.
Example:
"""
import json
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)

print(json_string)
# Output:
# {"name": "John", "age": 30, "city": "New York"}
"""
2. json.loads() – Convert JSON String to Python Object
Converts a JSON string into a Python object.
Example:
"""
import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
python_obj = json.loads(json_string)

print(python_obj)
# Output:
# {'name': 'John', 'age': 30, 'city': 'New York'}
"""
3. json.dump() – Write Python Object to a JSON File
This method writes a Python object into a JSON file.
Example:
"""

import json
data = {"name": "John", "age": 30, "city": "New York"}

with open("data.json", "w") as file:
    json.dump(data, file)
"""    
This will write the dictionary into data.json in JSON format.

4. json.load() – Read JSON from a File and Convert to Python Object
Reads a JSON file and converts it to a Python object.
Example:
"""
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
"""
Output (assuming data.json contains {"name": "John", "age": 30, "city": "New York"}):
{'name': 'John', 'age': 30, 'city': 'New York'}

5. json.dumps() with Optional Parameters
The dumps() method has several optional parameters to customize the output.
indent: Adds indentation for pretty formatting.
separators: Specifies how to separate keys and values (default is (', ', ': ')).
sort_keys: Sorts the dictionary by keys.
Example with indent, separators, and sort_keys:
"""
import json
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data, indent=4, separators=(", ", ": "), sort_keys=True)
print(json_string)
"""
Output:
{
    "age": 30,
    "city": "New York",
    "name": "John"
}
6. Handling Non-Serializable Objects with default
If you're trying to serialize an object that is not natively serializable (like a custom class), you can use the default parameter to specify how to handle it.
Example:
"""
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_serializer(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError("Type not serializable")

person = Person("John", 30)

json_string = json.dumps(person, default=person_serializer)

print(json_string)
"""
Output:
{"name": "John", "age": 30}
7. json.JSONDecodeError
When parsing invalid JSON, Python raises a JSONDecodeError. You can handle this with try...except.

Example:
"""
import json
invalid_json = '{"name": "John", "age": 30'  # Missing closing brace
try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
"""    
Output:
Invalid JSON: Expecting ',' delimiter: line 1 column 34 (char 33)

8. json.JSONEncoder
Custom JSON encoder can be created by subclassing json.JSONEncoder.

Example:
"""
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age}
        return super().default(obj)

person = Person("John", 30)

json_string = json.dumps(person, cls=CustomEncoder)

print(json_string)
"""
When to Use JSON Methods?
✅ Data Serialization – Convert data between Python objects and JSON format (e.g., saving data to a file or sending 
it over a network).
✅ Data Interchange – Exchange data between different systems or applications that use JSON format.
✅ Working with APIs – Interacting with APIs that send or receive JSON.

JSON handling in Python is simple and flexible, making it easy to work with data in JSON format!
"""