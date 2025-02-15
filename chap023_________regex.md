### Python Regex (Regular Expressions)
#### Regular expressions (regex) in Python allow you to search, match, and manipulate text patterns. The re module provides regex functionality.

1. Importing the re Module
```
import re
```
2. Basic Regex Functions

| Function	        | Description                                  |
|------------------|:---------------------------------------------|
| re.match()	   |  Matches a pattern at the start of a string. |
| re.search()      | 	Searches the entire string for a match.    | 
| re.findall()     | 	Returns all occurrences of the pattern.     |
| re.finditer()    | 	Returns an iterator over all matches.       |
| re.sub()         | 	Replaces matches with a new substring.      |
| re.split()	      | Splits a string based on the pattern.        |

3. match() – Check if String Starts with Pattern

```
import re

text = "Hello, World!"
match = re.match(r"Hello", text)

if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match")
```
4. search() – Find Pattern Anywhere

```
import re

text = "The price is $50."
match = re.search(r"\$\d+", text)  # Find "$" followed by numbers

if match:
    print("Found:", match.group())  # Output: Found: $50
```
5. findall() – Find All Matches

```
import re

text = "My numbers are 123, 456, and 789."
numbers = re.findall(r"\d+", text)  # Find all numbers
print(numbers)  # Output: ['123', '456', '789']
```
6. finditer() – Iterate Over Matches
```
import re
text = "Email: user@example.com, support@service.com"
matches = re.finditer(r"[\w\.-]+@[\w\.-]+", text)

for match in matches:
    print("Found email:", match.group())
Output:
Found email: user@example.com
Found email: support@service.com

```

7. sub() – Replace Matches
```
import re

text = "I love Python and Python is awesome!"
new_text = re.sub(r"Python", "Java", text)  # Replace "Python" with "Java"
print(new_text)  # Output: I love Java and Java is awesome!
```

8. split() – Split String by Pattern
```
import re

text = "apple, orange;banana|grape"
words = re.split(r"[,;|]", text)  # Split using multiple delimiters
print(words)  # Output: ['apple', ' orange', 'banana', 'grape']

```

9. Regex Metacharacters and Special Sequences
Metacharacters

| Symbol                        | Meaning	                        |Example|
|-------------------------------|:--------------------------------|:---------------------------------------------|
| .                             | 	Any character (except newline) |	"a.b" matches "acb"|
| ^                             | 	Start of string                |	"^hello" matches "hello world"|
| $                             | 	End of string                  |	"world$" matches "hello world"|
| *                             | 	0 or more occurrences          |	"ab*" matches "a", "ab", "abb"|
| +                             | 	1 or more occurrences          |	"ab+" matches "ab", "abb", not "a"|
| ?                             | 	0 or 1 occurrence              |	"ab?" matches "a", "ab"|
| {n,m}                         | 	Between n and m occurrences	   |"a{2,4}" matches "aa", "aaa", "aaaa"|
| []                            | 	Character set                  |	"[aeiou]" matches any vowel|
| \\ | 	Escape special characters      |	"\." matches "."|


Special Sequences

|Pattern	|Meaning|	Example|
|---------------------|:--------------------------------|:---------------------------|
|\d|	Any digit (0-9)|	"\d+" matches "123" |
|\D|	Any non-digit	|"\D+" matches "abc"|
|\w|	Any word character (a-z, A-Z, 0-9, _)|	"\w+" matches "hello123" |
|\W|	Any non-word character	|"\W+" matches "@$%" |
|\s	|Any whitespace|	"\s+" matches " " |
|\S|	Any non-whitespace	|"\S+" matches "hello" |

10. Example: Extract Phone Numbers
```
import re
text = "Call me at 123-456-7890 or 987.654.3210"
pattern = r"\d{3}[-.]\d{3}[-.]\d{4}"  # Matches "123-456-7890" or "987.654.3210"

matches = re.findall(pattern, text)
print(matches)  # Output: ['123-456-7890', '987.654.3210']
```
11. Example: Validate Email Addresses

```
import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

print(is_valid_email("user@example.com"))  # Output: True
print(is_valid_email("invalid-email"))  # Output: False

```

12. Example: Extract URLs from Text
```
import re

text = "Visit https://www.google.com or http://example.com"
pattern = r"https?://[a-zA-Z0-9./-]+"

urls = re.findall(pattern, text)
print(urls)  # Output: ['https://www.google.com', 'http://example.com']
```
When to Use Regex?
* Validating input (emails, phone numbers, usernames) 
* Searching and extracting specific patterns 
* Text preprocessing (removing unwanted characters, splitting text) 
* Find and replace operations

Regex makes text processing powerful and efficient!