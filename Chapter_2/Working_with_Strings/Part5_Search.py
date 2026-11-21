"""
5. Searching: we have four types
startswith() — Check if a string starts with a specific substring.
endswith() — Check if a string ends with a specific substring.
find() — Find the index of the first occurrence of a substring.
in — Check if a substring exists within a string.
"""




'''
A. startswith(): The startswith() method checks if a string starts with a specific substring. It returns True if the string starts with the specified substring, and False otherwise.
'''

file = "sales_data.csv"

print(file.startswith("sales"))
print(file.startswith("data"))


files = "raw_data.csv"

if files.startswith("raw"):
    print("Raw file detected.")
else:
    print("Invalid file")





'''
B. endswith(): The endswith() method checks if a string ends with a specific substring. It returns True if the string ends with the specified substring, and False otherwise.
'''

file = "customer.csv"

print(file.endswith(".csv"))
print(file.endswith(".json"))


files = "transactions.json"

if files.endswith(".json"):
    print("JSON file detected.")
else:
    print("Invalid file")






'''
C. find(): The find() method returns the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
'''


text = "Data Engineering"

print(text.find("Engineering"))
#Opt : 5

'''
Why 5 ? cause python indexing starts at zero
D  a  t  a     E  n  g  i  n  e  e  r  i  n  g
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
'''


text2 = "Python for Data Engineering"
print(text2.find("Java"))
#Opt : -1


# Find a delimiter in a record
record = "John,Doe,30,New York"
position = record.find(",")
print(position)  
# Output: 4 (index of the first comma)

# Data Engineering use case: Finding delimiters, identifying substrings, or locating specific values in raw text.


####### Another way ########

phone1 = "+48-123-45678"
phone2 = "+48-987-65432"
phone3 = "0048-555-12345"

print(phone1.find("-")) 
#Opt: 3
# So we need after 3

print(phone1[phone1.find("-") + 1:]) #+1 to get next index
print(phone2[phone2.find("-") + 1:])
print(phone3[phone3.find("-") + 1:])





'''
D. in: The in operator checks if a substring exists within a string. It returns True if the substring is found, and False otherwise.
'''

email = "john.doe@example.com"

if "@" in email:
    print("Valid email address.")
else:
    print("Invalid email address.")



'''
Combining methods – Data Engineering example
Imagine a data pipeline receives multiple files. We want to identify valid CSV files that belong to the sales dataset.
'''

files = [
    "sales_2026.csv",
    "customer_2026.json",
    "sales_2025.csv",
    "orders_2026.csv",
    "sales_backup.txt"
]

for file in files:
    if file.startswith("sales") and file.endswith(".csv"):
        print("Processing:", file)



test = "PythonPython"
print(test.find("Python", 1))  
# Output: 6 (finds the second occurrence of "Python" starting from index 1)