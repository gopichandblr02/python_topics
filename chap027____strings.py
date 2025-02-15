"""
lower(): Converts all uppercase characters in a string into lowercase
upper(): Converts all lowercase characters in a string into uppercase
title(): Convert string to title case
swapcase(): Swap the cases of all characters in a string
capitalize(): Convert the first character of a string to uppercase
"""
# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'
# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())
# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())
# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(text.title())
# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())
# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())
# original string never changes
print("\nOriginal String")
print(text)
# Converted String:
# GEEKS FOR GEEKS
#
# Converted String:
# geeks for geeks
#
# Converted String:
# Geeks For Geeks
#
# Converted String:
# GEEkS fOR GEeKs
#
# Original String
# geeKs For geEkS
"""
find(substring): Returns the lowest index in the string where the substring is found.
strip(): Removes any leading and trailing characters (space is the default).
replace(old, new): Replaces occurrences of a substring within the string.
split(delimiter): Splits the string at the specified delimiter and returns a list of substrings.
join(iterable): Concatenates elements of an iterable with a specified separator.
startswith(prefix): Checks if the string starts with the specified prefix.
endswith(suffix): Checks if the string ends with the specified suffix.
"""

text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7

# If the substring is not found
index = text.find("Python")
print(index)  # Output: -1

text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

# Removing specific characters
text = "###Hello, W#orld!###"
stripped_text = text.strip("#")
print(stripped_text)  # Output: "Hello, W#orld!"

text = "Hello, World!"
replaced_text = text.replace("World", "Python")
print(replaced_text)  # Output: Hello, Python!

# Replacing characters
text = "banana"
replaced_text = text.replace("a", "o")
print(replaced_text)  # Output: bonono


## split
text = "file.csv"
split_text=text.split(".")
print(split_text,type(split_text))  # ['file', 'csv'] <class 'list'>

## reverse
text="abcd"
rev_txt=reversed(text)
rev_txt1=text[::-1]
rev_txt_str="".join(reversed(text))
rev_txt_str1=str(rev_txt)
rev_txt_str2=list(rev_txt)
print(rev_txt,type(rev_txt)) # <reversed object at 0x10358b700> <class 'reversed'>
print(rev_txt1,type(rev_txt1)) # dcba <class 'str'>
print(rev_txt_str,type(rev_txt_str)) #dcba <class 'str'>
print(rev_txt_str1,type(rev_txt_str1)) # <reversed object at 0x10358b700> <class 'str'>
print(rev_txt_str2,type(rev_txt_str2)) # ['d', 'c', 'b', 'a'] <class 'list'>

