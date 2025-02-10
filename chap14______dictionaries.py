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


################ default dictionary
