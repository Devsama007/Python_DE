"""
Validation: we have two types
isalpha() — Check if all characters in a string are alphabetic.
isnumeric() — Check if all characters in a string are numeric.
"""




'''
A. isalpha(): The isalpha() method checks if all characters in a string are alphabetic (letters). It returns True if all characters are alphabetic, and False otherwise.
'''


name = "Alice"
print(name.isalpha())  # Output: True

name = "Alice123"
print(name.isalpha())  # Output: False




'''
B. isalpha() — Check if all characters in a string are alphabetic.
isnumeric() — Check if all characters in a string are numeric.
'''
#Note:  numeric doesn’t consider float or any special charater like (-, &…)

print("12345".isnumeric())  # Output: True
print("125.67".isnumeric()) # Output: False
print("12a45".isnumeric()) # Output: False
print("-1234".isnumeric()) # Output: False