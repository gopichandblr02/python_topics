### Determining Time Complexity (O(n)):
Identify the dominant operations: Focus on operations that are repeatedly executed, especially those within loops or recursive calls.
Count operations relative to 'n':
1. Constant Time (O(1)): Operations that take a fixed amount of time regardless of 'n', such as accessing an array element by index, a single arithmetic operation, or a simple print statement.
2. Linear Time (O(n)): Operations that execute proportionally to 'n', like iterating through an array once using a single for or while loop.

```
for item in data:
    # O(1) operation inside the loop
    print(item)
```


3. Quadratic Time (O(n^2)): Operations involving nested loops where the inner loop also runs 'n' times for each iteration of the outer loop.

```
for i in range(n):
    for j in range(n):
        # O(1) operation
        result = i * j
```


3. Logarithmic Time (O(log n)): Operations where the input size is repeatedly halved, like in binary search.
4. Linearithmic Time (O(n log n)): Often seen in efficient sorting algorithms like merge sort or quicksort.
5. Discard constant factors and lower-order terms: Big O notation focuses on the dominant term as 'n' approaches infinity. 
For example, O(2n + 5) simplifies to O(n), and O(n^2 + n) simplifies to O(n^2).



### Determining Space Complexity (O(n)):

Analyze memory allocation: Identify how much memory the algorithm uses based on the input size 'n'.
Consider data structures:
Constant Space (O(1)): If the algorithm uses a fixed amount of memory regardless of 'n', such as a few variables.
Linear Space (O(n)): If the algorithm creates data structures (like arrays, lists, or hash tables) whose size is directly proportional to 'n'.

```
new_list = [0] * n  # Creates a list of size n
```


1. Quadratic Space (O(n^2)): If the algorithm creates a 2D data structure (like a matrix) where both dimensions are proportional to 'n'.
2. **Ignore input space:** Usually, space complexity refers to auxiliary space, meaning the extra space used by the algorithm, not the space taken by the input itself.