"""
4. Cleaning: we have five types
lstrip() — Remove leading whitespace.
rstrip() — Remove trailing whitespace.
strip() — Remove leading and trailing whitespace.
lower() — Convert to lowercase.
upper() — Convert to uppercase
"""


'''
A. lstrip(): The lstrip() method removes any leading whitespace characters (spaces, tabs, newlines) from the beginning of a string.
'''

test = "  Hello, World!"
print(test.lstrip())

#Removing specific character
t1 = "###Python"
print(t1.lstrip("#"))
#When you provide characters, Python removes any matching characters from the left until it encounters a different character



'''
B. rstrip(): The rstrip() method removes any trailing whitespace characters (spaces, tabs, newlines) from the end of a string.
'''
stat = "Success   "
print(stat.rstrip())


#Removing specific character
t2 = "report.csv...."
print(t2.rstrip("."))



'''
C. strip(): The strip() method removes any leading and trailing whitespace characters (spaces, tabs, newlines) from a string.
'''

mail = "  user@example.com  "
print(mail.strip())

#trip() does not remove spaces between words. It only cleans the beginning and end.



'''
D. lower(): The lower() method converts all characters in a string to lowercase.
'''
name = "ALICE"
print(name.lower())



'''
E. upper(): The upper() method converts all characters in a string to uppercase.
'''
name = "bob"
print(name.upper())




"""
Combining cleaning methods – Real Data Engineering example
In real ETL pipelines, you will often combine multiple string methods.

Imagine you receive customer records from an API
"""

customers = [
    "  GAMMA@GMAIL.COM  ",
    "  Rahul@GMAIL.COM",
    "PRIYA@YAHOO.COM   "
]

cleaned_data = []

for email in customers:
    cleaned = email.strip().lower()
    cleaned_data.append(cleaned)

print(cleaned_data)





# Q1. Predict the output:
text = "   Data Engineering   "
print(text.strip().lower())

# Opt: data engineering


#Q2. Clean this customer ID:
customer_id = "   cust-102   "
print(customer_id.strip())

# Opt: cust-102


#Q3. What will be the output?
text = "###HELLO WORLD###"
print(text.strip("#").lower().upper())

# Opt: HELLO WORLD


'''
You receive this list from an API:
Create a new list where:
- All leading and trailing spaces are removed.
- Every status is converted to lowercase.
'''

statuses = [
    " success ",
    "FAILED  ",
    "  Pending",
    "sUcCeSs"
]
cleaned_stat = []

for stat in statuses:
    clean = stat.strip().lower()
    cleaned_stat.append(clean)

print(cleaned_stat)

# Opt: ['success', 'failed', 'pending', 'success']



############ Challenge ############ 
'''
Convert the following string in below format 

"968-Maria, ( D@t@ Engineer ) ;; 27y " 

"name: maria | role: data engineer | age: 27" 
'''

# First need to cleaned data with strip() and lower() methods
str = "968-Maria, ( D@t@ Engineer ) ;; 27y " 

new_data = str.replace("@", "a").replace(";;", ",").replace("y", "").replace("(", "").replace(")", "").strip().lower()
print(new_data)

# Now we can split the string to extract name, role, and age
parts = new_data.split(",")
print(parts)

# Now we can extract the name, role, and age from the parts
name = parts[0].split("-")[1].strip()
role = parts[1].strip()
age = parts[2].strip()

#Print the result
result = f"name: {name} | role: {role} | age: {age}"
print(result)