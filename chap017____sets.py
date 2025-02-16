"""
add(): Adds a given element to a set
clear(): Removes all elements from the set
discard(): Removes the element from the set
pop(): Returns and removes a random element from the set
remove(): Removes the element from the set
remove vs discard
discard -> no error if element is not found
"""
# set of letters
s = {'g', 'e', 'k', 's'}

# adding 's'
s.add('f')
print('Set after updating:', s)   #Set after updating: {'k', 's', 'e', 'f', 'g'}

# Discarding element from the set
s.discard('g')
print('\nSet after updating:', s)   # Set after updating: {'k', 's', 'e', 'f'}

# Removing element from the set
s.remove('e')
print('\nSet after updating:', s) # Set after updating: {'k', 's', 'f'}

# Popping elements from the set
print('\nPopped element', s.pop()) # Popped element k
print('Set after updating:', s)   # Set after updating: {'s', 'f'}

s.clear()
print('\nSet after updating:', s)  # Set after updating: set()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)    # True

fruits = frozenset(["apple", "banana", "orange"])
print(fruits)
fruits.add("cherry")
print(fruits)    # AttributeError: 'frozenset' object has no attribute 'add'

my_set1= {1,2,3}
my_set2={3,4,5}
my_set3={8,9}

# Functions Name	Description
# 1. add()	->  Adds a given element to a set
# 2. clear()	->  Removes all elements from the set
# 3. copy()	->  Returns a shallow copy of the set
# 4. difference()	->  Returns a set that is the difference between two sets
my_set1.difference("diff:",my_set2)
print(my_set1)   #{1,2}
# 5. difference_update()	->  Updates the existing caller set with the difference between two sets
#{1,2}
# 6. discard()	->  Removes the element from the set
# 7. frozenset()	->  Return an immutable frozenset object
set5=frozenset(my_set1)
print(set5,type(set5)) # frozenset({1, 2}) <class 'frozenset'>
# 8. intersection()	->  Returns a set that has the intersection of all sets
# 9. intersection_update()	->  Updates the existing caller set with the intersection of sets
# 10. isdisjoint()	->  Checks whether the sets are disjoint or not
# 11. issubset()	->  Returns True if all elements of a set A are present in another set B
# 12. issuperset()	->  Returns True if all elements of a set A occupies set B
# 13. pop()	->  Returns and removes a random element from the set
# 14. remove()	->  Removes the element from the set
# 15. symmetric_difference()	->  Returns a set which is the symmetric difference between the two sets
# 16. symmetric_difference_update()	->  Updates the existing caller set with the symmetric difference of sets
# 17. union()	->  Returns a set that has the union of all sets
# 18. update()	->  Adds elements to the set

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

my_set.add(2)  # No effect
print(my_set)

my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)
