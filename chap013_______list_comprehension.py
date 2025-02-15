"""
List Comprehension in Python
List comprehension is a concise and efficient way to create lists in Python. It follows the syntax:
new_list = [expression for item in iterable if condition]
1. Basic List Comprehension
Creates a list from an existing sequence.
"""

numbers = [x for x in range(5)]
print(numbers)  # Output: [0, 1, 2, 3, 4]
"""
2. List Comprehension with Condition
Filters elements based on a condition.
"""

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
"""
3. List Comprehension with if-else
Adds a condition inside the comprehension.
"""

labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']
"""
4. Nested List Comprehension
Used to create multi-dimensional lists.
"""
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
"""
5. List Comprehension with String Manipulation
Creates a list based on string operations.
"""
words = ["hello", "python", "world"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'PYTHON', 'WORLD']
"""
6. List Comprehension with zip()
Combines elements from two lists.
"""
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
student_scores = {name: score for name, score in zip(names, scores)}
print(student_scores)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}
"""
7. Removing Duplicates using List Comprehension
Removes duplicates while maintaining order.
"""
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(dict.fromkeys(nums))
print(unique_nums)  # Output: [1, 2, 3, 4, 5]
"""
8. Flattening a Nested List
Converts a 2D list into a 1D list.
"""
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

"""
9. Filtering Words with a Condition
Extracts words with more than 3 letters.
"""
words = ["a", "an", "apple", "dog", "cat"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # Output: ['apple', 'dog']
"""
10. List Comprehension with enumerate()
Gets indices and values together.
"""

words = ["python", "code", "AI"]
indexed_words = [(index, word) for index, word in enumerate(words)]
print(indexed_words)  # Output: [(0, 'python'), (1, 'code'), (2, 'AI')]
"""
11. Prime Numbers using List Comprehension
Generates prime numbers up to 50.
"""

primes = [x for x in range(2, 50) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
