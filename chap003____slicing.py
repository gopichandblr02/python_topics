#####################################################
############### Python List Slicing #################
#####################################################
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index 1 to 4 (excluded)
print(a[1:4]) # [2,3,4]
# list_name[start : end : step]
# Parameters:
# start (optional): Index to begin the slice (inclusive). Defaults to 0 if omitted.
# end (optional): Index to end the slice (exclusive). Defaults to the length of list if omitted.
# step (optional): Step size, specifying the interval between elements. Defaults to 1 if omitted
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get all elements in the list
print(a[::])
print(a[:])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements starting from index 2 to the end of the list
b = a[2:]
print(b)
# Get elements starting from index 0 to index 3 (excluding 3th index)
c = a[:3]
print(c)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index 1 to index 4 (excluding index 4)
b = a[1:4]
print(b) # [2, 3, 4]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get every second element from the list starting from the beginning
b = a[::2]
print(b)
# Get every third element from the list starting from index 2 to 8(exclusive)
c = a[1:8:3]
print(c)
# [1, 3, 5, 7, 9]
# [2, 5, 8]
"""
Out-of-bound slicing
In Python, list slicing allows out-of-bound indexing without raising errors. If we specify indices beyond the list length
then it will simply return the available items.
Example: The slice a[7:15] starts at index 7 and attempts to reach index 15, but since the list ends at index 8, so it 
will return only the available elements (i.e. [8,9]).
"""
b = [1,2,3,4]
print(b[2:20])   #[3, 4]
"""
Negative Indexing
Negative indexing is useful for accessing elements from the end of the list. The last element has an index of -1, the 
second last element -2, and so on.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements starting from index -2
# to end of list
b = a[-2:]
print(b)
# Get elements starting from index 0
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)
# Get every 2nd elements from index -8
# to -1 (excluding index -1)
e = a[-8:-1:2]
print(e)
# [8, 9]
# [1, 2, 3, 4, 5, 6]
# [6, 7, 8]
# [2, 4, 6, 8]
# Reverse a list using slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get the entire list using negative step
b = a[::-1]
print(b) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a[::-2]) # [9, 7, 5, 3, 1]

#######################################################
############### Python String Slicing #################
#######################################################
s = "Hello, Python!"
# Slice string from index 0 to index 5 (exclusive)
s2 = s[0:5]
print(s2) # Hello
s = "Hello, World!"
# Get the entire string
s2 = s[:]
s3 = s[::]
print(s2)
print(s3)
s = "Hello, World!"
# Characters from index 7 to the end
print(s[7:])
# Characters from the start up to index 5 (exclusive)
print(s[:5])
# World!
# Hello
s = "Hello, World!"
# Characters from index 1 to index 5 (excluding 5)
print(s[1:5]) # ello
s = "abcdefghi"
# Every second character
print(s[::2])
# Every third character from index 1 to 8 (exclusive)
print(s[1:8:3])
# acegi
# beh
s = "abcdefghijklmno"
# Characters from index -4 to the end
print(s[-4:])
# Characters from the start up to index -3 (excluding -3)
print(s[:-3])
# Characters from index -5 to -2 (excluding -2)
print(s[-5:-2])
# Get every 2nd elements from index -8 to -1 (excluding index -1)
print(s[-8:-1:2])
# lmno
# abcdefghijkl
# klm
# hjln
s = "Python"
# Reverse the string
print(s[::-1])
# nohtyP