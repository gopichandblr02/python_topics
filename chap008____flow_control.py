############# Python for loop ##############
"""
In Python, we use a for loop to iterate over sequences such as lists, strings, dictionaries, etc.
The for loop iterates over the elements of sequence in order, and in each iteration, the body of the loop is executed.
For example,
"""
languages = ['Swift', 'Python', 'Go']
# access elements of the list one by one
for lang in languages:
    print(lang)
# Swift
# Python
# Go
"""
In Python's print() function, end and sep are optional parameters used to control the output format.
sep (separator):
It specifies how multiple arguments passed to the print() function should be separated. By default, sep is a space (" ").
end:
It specifies what should be printed at the end of the print() statement. By default, end is a newline character ("\n").
"""
for lang in languages:
    print(lang,end=";")
#Swift;Python;Go;
print("mango","apple","banana",sep=";")
#mango;apple;banana
my_list = [1, 2, 3, 4, 5]
print(*my_list, sep="$")
# 1$2$3$4$5
print(*my_list)
# 1 2 3 4 5
my_list = [1, 2, 3, 4, 5]
print(*my_list, end="$")
# 1 2 3 4 5$
my_list = [10, 20, 30, 40, 50]
print(" ".join(map(str, my_list)))
# 10 20 30 40 50
# Example: Loop Through a String
language = 'Python'
# iterate over each character in language
for x in language:
    print(x)
# P
# y
# t
# h
# o
# n
# generate numbers from 0 to 3
values = range(0, 4)
print(values)   #range(0, 4)
# iterate from i = 0 to i = 3
for i in range(0, 4):
    print(i)
# 0
# 1
# 2
# 3

# break Statement
"""
The break and continue statements are used to alter the flow of loops.
"""
languages = ['Swift', 'Python', 'Go', 'C++']
for lang in languages:
    if lang == 'Go':
        break
    print(lang)
# Swift
# Python
# The continue Statement
"""
The continue statement skips the current iteration of the loop and continues with the next iteration. For example,
"""
languages = ['Swift', 'Python', 'Go', 'C++']
for lang in languages:
    if lang == 'Go':
        continue
    print(lang)
# Swift
# Python
# C++
##### Nested for loops
"""
A loop can also contain another loop inside it. These loops are called nested loops.
In a nested loop, the inner loop is executed once for each iteration of the outer loop.
"""
# outer loop
attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Porsche', 'Mercedes']
for attribute in attributes:
    for car in cars:
        print(attribute, car)

    # this statement is outside the inner loop
    print("-----")
# Electric Tesla
# Electric Porsche
# Electric Mercedes
# -----
# Fast Tesla
# Fast Porsche
# Fast Mercedes
# -----

######## for and while can be used with except stmt, gets executed at the end
a=[1,2,3]
for x in a:
    print(x)
else:
    print('hi')
# 1
# 2
# 3
# hi

####### While loop
"""
In Python, we use a while loop to repeat a block of code until a certain condition is met. For example,
"""
number = 1
while number <= 3:
    print(number)
    number = number + 1
"""
Here,
The while loop evaluates condition, which is a boolean expression.
If the condition is True, body of while loop is executed. The condition is evaluated again.
This process continues until the condition is False.
Once the condition evaluates to False, the loop terminates.
Tip: We should update the variables used in condition inside the loop so that it eventually evaluates to False. 
Otherwise, the loop keeps running, creating an infinite loop.
"""
# Print numbers until the user enters 0
number = int(input('Enter a number: '))
# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))
print('The end.')

# python while loop with else clause
counter = 0
while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')
#############################################################
##### do while in python using "True and break" #######
#############################################################
num=10
while True:
    if num == 0:
        break
    num-=1
    print(num)
# Here 0 will be printed once just like do while
num=0
while True:
    print(num)
    if num == 0:
        break
    num-=1
##### Python pass Statement
"""
In Python programming, the pass statement is a null statement which can be used as a placeholder for future code.
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement.
"""
n = 10
# use pass inside if statement
if n > 10:
    pass
print('Hello')
"""
Use of pass Statement inside Function or Class
We can do the same thing in an empty function or class as well. For example,
"""
def function(args):
    pass
class Example:
    pass


