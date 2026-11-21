# ************ String Types in Python ************

"""
Types: type(), str()

Math: len(), count()

Transformations: replace(), f-strings, split(), repetition with *

Extraction: indexing and slicing

Cleaning: lstrip(), rstrip(), strip(), lower(), upper()

Search and validation: startswith(), endswith(), find(), isalpha(), isnumeric()

"""


"""
1. Types: we have two types
   type() and str()
"""

'''
A. type(): function tells you the data type of a value or variable.
'''

name = "Python"
print(type(name))

# Python automatically determines the data type based on the value assigned to each variable.


# Data Engineering — Checking incoming data

cust_d = "101"
purchase = "35000"

print(type(cust_d))
print(type(purchase))

# Even though these values look numeric, they are strings because they are enclosed in quotes. Data imported from CSV files often contains values that need type conversion before calculations.



'''
B. str(): function converts a value into its string representation.
'''

age = 24
print(type(age))
print(type(str(age)))

# The value 24 changes from an integer to a string. The displayed output looks the same, but its data type is different.

'''print("My age is: " + age)'''  # This will cause TypeError

print("My age is: " + str(age))

# Python cannot directly concatenate a string and an integer using +. Converting age with str() makes both operands strings.


# Data Engineering — Creating a log message

records = 1500
status = "Success"

log_msg = "Records processed: " + str(records)

print(log_msg)
print(type(log_msg))

# We can also write in f string

print(f"Records processed: {records}")


