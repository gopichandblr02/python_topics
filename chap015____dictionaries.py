"""
***   A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. ***

Accessing and Modifying Elements:
get(key, default=None):
Returns the value associated with the key. If the key is not found, it returns the default value (which defaults to None).
setdefault(key, default=None):
Similar to get(), but if the key is not found, it inserts the key with the default value and returns the default value.
pop(key, default=None):
Removes and returns the value associated with the key. If the key is not found, it returns the default value or raises a KeyError if default is not provided.
popitem():
Removes and returns an arbitrary (key, value) pair from the dictionary. Raises a KeyError if the dictionary is empty.
update(other_dict):
Adds the key-value pairs from other_dict to the dictionary. If a key already exists, its value is updated.

Viewing Dictionary Contents:
keys(): Returns a view object containing the keys of the dictionary.
values(): Returns a view object containing the values of the dictionary.
items(): Returns a view object containing the (key, value) pairs of the dictionary.
Creating and Copying Dictionaries:
dict(): Creates a new dictionary. It can be used with keyword arguments or by passing an iterable of key-value pairs.
fromkeys(iterable, value=None): Creates a new dictionary with keys from iterable and all values set to value.
copy(): Returns a shallow copy of the dictionary.
Checking Dictionary Properties:
clear(): Removes all items from the dictionary.
len(dict): Returns the number of items (key-value pairs) in the dictionary.
in: Checks if a key is present in the dictionary.
"""
# clear
my_dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}
my_dict.clear()
print("clear:",my_dict)
# get
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print("get:",d.get('Name'))
print("get:",d.get('Gender','default'))
# items -> List of tuples  ...... <class 'dict_items'>
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print("items:",d.items(),type(d.items()))
print("items:",list(d.items())[1][0])
print("items:",list(d.items())[1][1])
# keys
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print("keys:",list(d.keys()),type(d.keys()))    #keys: ['Name', 'Age', 'Country'] <class 'dict_keys'>
# values
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
print("values:",list(d.values()),type(d.values()))    # keys: ['Name', 'Age', 'Country'] <class 'dict_keys'>
# update
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}
d1.update(d2)
print("update:",d1)
# pop
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d.pop('Age')
print("pop:",d)  # pop: {'Name': 'Ram', 'Country': 'India'}
# pop item
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
val = d.popitem()
print(val)    # ('Country', 'India')
val = d.popitem()
print(val)    # ('Age', '19')

dict1 = {1:10,2:20,3:30}
dict1.setdefault(5,"abcd")
print(dict1)    #{1: 1, 2: 2, 3: 3, 5: 'abcd'}

print(dict1.pop(3))   #30
print(dict1.pop(33))   #30   #error

##################################################################################################
################             default dictionary         ##########################################
##################################################################################################
"""
defaultdict in Python (from collections module)
A defaultdict is a subclass of the built-in dict class. It provides a default value for missing keys instead of raising a KeyError.
Syntax:
"""

from collections import defaultdict
d = defaultdict(default_factory)
"""
default_factory is a callable (like int, list, set, etc.) that provides a default value for missing keys.
1. Default value as int (defaults to 0)
"""
from collections import defaultdict
d = defaultdict(int)
d["a"] += 1  # No KeyError, default value is 0
print(d)  # Output: defaultdict(<class 'int'>, {'a': 1})
"""
2. Default value as list
Creates a dictionary where missing keys get an empty list.
"""

from collections import defaultdict
d = defaultdict(list)
d["fruits"].append("apple")
d["fruits"].append("banana")
print(d)  # Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})
"""
3. Default value as set
Creates a dictionary where missing keys get an empty set.
"""

from collections import defaultdict
d = defaultdict(set)
d["numbers"].add(1)
d["numbers"].add(2)
print(d)  # Output: defaultdict(<class 'set'>, {'numbers': {1, 2}})
"""
4. Default value as lambda (custom defaults)
Using a lambda function for custom default values.
"""

from collections import defaultdict
d = defaultdict(lambda: "Not Found")
print(d["name"])  # Output: Not Found
"""
5. Counting Elements (like Counter)
Using defaultdict(int) to count occurrences of elements.
"""

from collections import defaultdict
word_count = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "banana"]

for word in words:
    word_count[word] += 1
print(word_count)  # Output: defaultdict(<class 'int'>, {'apple': 2, 'banana': 3, 'orange': 1})
"""
6. Grouping Values (Using defaultdict(list))
Categorizing words based on their first letter.
"""
from collections import defaultdict
grouped_words = defaultdict(list)
words = ["apple", "banana", "avocado", "blueberry", "cherry"]

for word in words:
    grouped_words[word[0]].append(word)

print(grouped_words)
# Output: {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
"""
7. Storing Index Positions of Elements
Tracking positions of words in a sentence.
"""

from collections import defaultdict
index_map = defaultdict(list)
sentence = "this is a test this is only a test".split()

for index, word in enumerate(sentence):
    index_map[word].append(index)

print(index_map)
# Output: {'this': [0, 4], 'is': [1, 5], 'a': [2, 7], 'test': [3, 8], 'only': [6]}
"""
Why Use defaultdict Instead of dict?
Avoids KeyError – No need to check if a key exists before accessing it.
Simplifies Code – Reduces the need for explicit checks and initializations.
Useful for Grouping & Counting – Efficient when collecting or categorizing data.
"""

##################################################################################################
################             ordered dictionary         ##########################################
##################################################################################################
"""
OrderedDict in Python (collections module)
An OrderedDict is a dictionary subclass that maintains the order of keys based on their insertion sequence. 
Starting from Python 3.7, regular dictionaries (dict) also maintain insertion order, but OrderedDict provides additional features.
"""
from collections import OrderedDict

od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3

print(od)
# Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
"""
2. Maintaining Order Compared to Regular Dict
Even though Python 3.7+ dicts maintain insertion order, OrderedDict ensures compatibility with older versions and 
provides extra methods.
"""
# Regular Dictionary (Python 3.7+)
d = {}
d["x"] = 10
d["y"] = 20
d["z"] = 30
print(d)  # Output: {'x': 10, 'y': 20, 'z': 30}

# OrderedDict (Maintains Order Explicitly)
from collections import OrderedDict

od = OrderedDict()
od["x"] = 10
od["y"] = 20
od["z"] = 30
print(od)  # Output: OrderedDict([('x', 10), ('y', 20), ('z', 30)])
"""
3. move_to_end() Method
Moves a key to the end (right) or beginning (left) of the dictionary.
"""
from collections import OrderedDict

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("a")  # Moves "a" to the end
print(od)  # Output: OrderedDict([('b', 2), ('c', 3), ('a', 1)])

od.move_to_end("c", last=False)  # Moves "c" to the beginning
print(od)  # Output: OrderedDict([('c', 3), ('b', 2), ('a', 1)])
"""
4. popitem() Method
Removes and returns the last (or first) inserted item.
"""

from collections import OrderedDict

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

print(od.popitem())  # Removes the last item: ('c', 3)
print(od.popitem(last=False))  # Removes the first item: ('a', 1)
"""
5. Comparing OrderedDicts
Since OrderedDict maintains order, two dictionaries with the same key-value pairs but different insertion orders 
are not equal.
"""
from collections import OrderedDict

od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])

print(od1 == od2)  # Output: False (order matters!)

"""
6. Reversing an OrderedDict
"""

from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
reversed_od = OrderedDict(reversed(od.items()))

print(reversed_od)
# Output: OrderedDict([('c', 3), ('b', 2), ('a', 1)])
"""
7. Using OrderedDict for a LRU Cache Simulation
Used to implement a simple Least Recently Used (LRU) cache.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: str):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Move accessed key to end (most recently used)
        return self.cache[key]

    def put(self, key: str, value: int):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move existing key to end
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used item (first one)
        self.cache[key] = value


# Example usage
lru = LRUCache(2)
lru.put("a", 1)
lru.put("b", 2)
print(lru.cache)  # OrderedDict([('a', 1), ('b', 2)])

lru.get("a")  # Access 'a', so it becomes most recently used
lru.put("c", 3)  # 'b' is least recently used, so it gets removed
print(lru.cache)  # OrderedDict([('a', 1), ('c', 3)])
"""
Why Use OrderedDict?
✅ Maintains insertion order explicitly(important for older Python versions).
✅ Useful for LRU caches and ordered data processing.
✅ Provides extra methods(move_to_end, popitem, etc.).

Though dict now maintains order (Python 3.7+), OrderedDict is still valuable for its specialized functionalities.
"""