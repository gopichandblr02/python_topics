# Sequences vs collections in python
"""
Collections and sequences are both fundamental concepts in Python used to group multiple values together,
but they differ in terms of order and access methods.
Collection:
It is a general term for data structures that can hold multiple objects. Collections are characterized by their ability
to contain elements, but they do not guarantee any specific order. Sets and dictionaries are examples of collections.
Sequence:
It is a type of collection that maintains a specific order of its elements. This order is preserved throughout the
sequence's lifetime, and elements can be accessed by their position (index). Lists, tuples, and strings are examples of sequences.
Feature
Collection-Order: Not guaranteed
Sequence: Maintained
Mutability: Can be mutable or immutable
Iteration is supported in both

While all sequences are collections, not all collections are sequences. Sequences are a specific type of collection
with the added characteristic of order.
"""
# Collection (set)
my_set = {3, 1, 4, 1, 5, 9}
print(my_set)

# Sequence (list)
my_list = [3, 1, 4, 1, 5, 9]
print(my_list)
print(my_list[2])