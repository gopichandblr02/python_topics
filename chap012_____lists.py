###################################

"""Python's list data type comes with a variety of built-in methods that allow you to manipulate and interact with lists. Here's a comprehensive list of these APIs:
Adding Elements:
append(x): Adds an item x to the end of the list.
extend(iterable): Appends all the items from an iterable to the end of the list.
insert(i, x): Inserts an item x at the given index i.

Removing Elements:
remove(x): Removes the first occurrence of item x from the list and returns None. Raises a ValueError if x is not found.
pop([i]): Removes and returns the item at the given index i. If i is not provided, it removes and returns the last item.
clear(): Removes all items from the list.

Accessing Elements:
index(x[, start[, end]]): Returns the index of the first occurrence of item x in the list. Raises a ValueError if x is not found.
The optional start and end arguments limit the search to a specific range.
count(x): Returns the number of times item x appears in the list.

Modifying the List:
sort(key=None, reverse=False): Sorts the items in the list in ascending order (by default).
The optional key argument can be used to specify a custom sorting criterion. The reverse argument can be set to True to sort in descending order.
reverse(): Reverses the order of the items in the list.
copy(): Returns a shallow copy of the list.

Other Operations:
len(list): Returns the number of items in the list.
max(list): Returns the maximum value in the list.
min(list): Returns the minimum value in the list.
sum(list): Returns the sum of all items in the list.
any(list): Returns True if at least one item in the list is truthy, otherwise False.
all(list): Returns True if all items in the list are truthy, otherwise False"""

num_list=[1,5,3,5]
num_dict1=dict.fromkeys(num_list,10)
num_dict2=dict.fromkeys(num_list)
print(num_dict1,num_dict2)   #{1: 10, 5: 10, 3: 10} {1: None, 5: None, 3: None}
################
a=num_list.copy()
b=num_list.copy()
c=num_list.copy()
d=num_list.copy()
print(a) #[1, 5, 3]
a.append(100)
b.extend([90,91])
print(a,b)  #[1, 5, 3, 100, 90, 91] [1, 5, 3, 100, 90, 91]
c.insert(0,111) #insert 111 at 0th position
print(c)    #[111, 1, 5, 3, 100, 90, 91]
d.remove(5) # Removes first occurance of 5
print("d:",d)
ddd=d.pop(0) #d: [1, 3, 5]
print(ddd)
gg = [5,5,6,7]
ggg=gg.count(5)
print(ggg)

my_list = [1, 2, 3, 2]
#sort vs sorted........and reverse() vs reversed()
my_list.sort()    # [1, 2, 3, 4]
xx = sorted(my_list)
print("xx:",xx)
my_list.reverse() # [4, 3, 2, 1]
print(my_list)  #[3, 2, 2, 1]
a=my_list.reverse()
print(a) #None
#reversed produces an iterator object
b=reversed(my_list)
print(b) #<list_reverseiterator object at 0x10ae243d0>
print(list(b))  #[3, 2, 2, 1]


##### Shallow copy vs deep copy ###########

#??


## Shallow copy
import copy
ssss=[1,2,[3,4]]
sc=ssss.copy()
sd=copy.deepcopy(ssss)
sc[2][0]=99
print(f"original:{ssss} and shallow copy: {sc} ddepcopy copy: {sd}")   #original:[1, 2, [99, 4]] and shallow copy: [1, 2, [99, 4]]




