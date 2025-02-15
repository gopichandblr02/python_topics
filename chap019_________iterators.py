############ Python Iterators
"""
Iterators are methods that iterate collections like lists, tuples, etc. Using an iterator method,
we can loop through an object and return its elements.
Technically, a Python iterator object must implement two special methods, __iter__() and __next__(), collectively
called the iterator protocol.
In Python, we can use the next() function to return the next item in the sequence.
"""
# define a list
my_list = [4, 7, 0]
# create an iterator from the list
iterator = iter(my_list)
# get the first element of the iterator
print(next(iterator))  # prints 4
# get the second element of the iterator
print(next(iterator))  # prints 7
# get the third element of the iterator
print(next(iterator))  # prints 0
"""
Here, first we created an iterator from the list using the iter() method. 
And then used the next() function to retrieve the elements of the iterator in sequential order.
When we reach the end and there is no more data to be returned, we will get the StopIteration Exception.
"""

"""
A more elegant way of automatically iterating is by using the for loop. For example,
"""
# define a list
my_list = [4, 7, 0]
for element in my_list:
    print(element)
# 4
# 7
# 0
# create a list of integers
my_list = [100, 200, 300, 400, 500]
# create an iterator from the list
iterator = iter(my_list)
# iterate through the elements of the iterator
for element in iterator:
    # Print each element
    print(element)
# 100
# 200
# 300
# 400
# 500

#####  Building Custom Iterators
class PowTwo:
    """Class to implement an iterator
    of powers of two"""
    def __init__(self, max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

# create an object
numbers = PowTwo(3)
# create an iterable from the object
i = iter(numbers)
# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
#print(next(i)) # raises StopIteration exception
for i in PowTwo(3):
    print(i)



# Another custom iterator

class EvenNums:
    def __init__(self,max_val):
        self.max_val=max_val
    def __iter__(self):
        self.min_val=-2
        return self
    def __next__(self):
        if self.max_val>self.min_val:
            self.min_val+=2
            return self.min_val
        else:
            raise StopIteration

for j in EvenNums(20):
    print(j)
# en = EvenNums(20)
# jj=iter(en)
# print(next(jj))
