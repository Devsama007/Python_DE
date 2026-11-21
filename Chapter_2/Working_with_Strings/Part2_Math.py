

"""
2. Math: we have two types
   len() and count()
"""

'''
A. len(): function returns the total number of characters in a string, including spaces and special characters.
'''

txt = "Hello World"
print(len(txt))


# Data Engineering — Validating customer IDs

password = "  123sgvndgvdbioi"
print(len(password))

if len(password) == 8:
    print("Valid ID length")
else :
    print("Invalid length")

# Data Engineering use case: Validate incoming IDs, postal codes, product codes, or other fields with expected lengths.


'''
B. count(): The count() method returns how many times a particular character or substring appears.
'''

test = """
Python is easy to learn.
Python is powerful
Many people love python
"""

print(test.count("Python"))

# By default, count() is case-sensitive. Means uppercase and lowercase letters are teated as different



# Data Engineering — Checking data quality

rec = "101, Rahul, Mumbai, 34000"

com_cnt = rec.count(",")

print("Comma count: ", com_cnt)

if com_cnt == 3:
    print("Structure looks correct")
else :
    print("Structure is incorrect")



# Combining len() and count()

email = "user123@gmail.com"

print("Total chars: ", len(email))

print("Total of @ symbols: ", email.count("@"))

print("No of dots: ", email.count("."))




# A data pipeline receives this record:

record = "ORD101|Rahul|2500|Completed"

'''
Count the total characters.
Count the number of | delimiters.
Check whether the record contains exactly three delimiters.
'''

dele = record.count("|")

print("total characters: ", len(record))
print("Count the number of | delimiters", dele)

if dele == 3:
    print("Valid Records")
else:
    print("Invalid Records")

