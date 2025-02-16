# Python code to demonstrate dictionary
# comprehension
# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}
# We can use below too
# myDict = dict(zip(keys, values))
print (myDict)    # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

##### using fromkeys method
dic=dict.fromkeys(range(5), True)
print(dic)   # {0: True, 1: True, 2: True, 3: True, 4: True}

# Python code to demonstrate dictionary
# creation using list
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)   # {'C': 'ccc', 'O': 'ooo', 'D': 'ddd', 'I': 'iii', 'N': 'nnn', 'G': 'ggg', ' ': '   '}

# Python code to demonstrate dictionary
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)   # {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

#
l="GFG"
my_dict = {x:x+x for x in l}
print(my_dict)   #{'G': 'GG', 'F': 'FF'}   cannot have another G as key
# given string
l="GFG"
# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}
print(dic)    # {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}