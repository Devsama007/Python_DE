"""
Method vs Function

Method = 
a = Habibi
b = a.count("i")
print(b)

Function
a = Hifs
print(len(a)) , print(type(a))
"""


"""
3. Transformation: we have five types
replace() — Replace text.
F-strings — Format text.
split() — Divide a string.
String repetition using *.
Indexing and slicing — Extract characters.
"""


'''
A. replace(): he replace() method replaces occurrences of a substring with another substring
'''

txt = "I love Java"
res = txt.replace("Java", "Python")

print(res)

# The original string remains unchanged; replace() returns a new string.

# By default, replace() replaces all occurrences of the specified substring.
# But we can also add limit

text = "apple,banana,apple,mango"
print(text.replace("apple",  "orange", 1))

# The third argument, 1, limits the replacement to one occurrence.



# Data Engineering — Cleaning incoming data : Suppose a source system uses "N/A" to represent missing customer information.

cust_data = "Rahul,N/A,Mumbai"
cleaned_data = cust_data.replace("N/A", "Unknown")
print(cleaned_data)


'''
B. F-strings allow you to insert variables and expressions directly into a string.
'''

# First we used to do like this
folder = "C:/Users/Baraa/"
file = "report.csv"

full_path = folder + file
print(full_path)

# With f string we can do like this
print(f"{folder}{file}")


name = "Kevin"
age = 23

print(f"My name is {name} and I am {age} years old")



# Perform calculations inside an f-string
price = 350
qty = 4
print(f"Total price: {price * qty}")



# Data Engineering — Logging pipeline results

pipe_name = "Sales_ETL"
rec = 150000
status = "Success"

message = (
    f"Pipeline: {pipe_name} | "
    f"Records: {rec} | "
    f"Status: {status}"
)

message2 = (
    f"Pipeline: {pipe_name} | Records: {rec} | Status: {status}"
)

print(message)
print(message2)




'''
C. split(): The split() method divides a string into a list of smaller strings based on a separator.
'''

text = "Python is fun"
print(text.split())


records = "101,Wizard,Mumbai,34000"
res = records.split(",")   #split(",") separates the string wherever a comma appears

print(res)
print(res[2]) #result[2] accesses the second element, "Mumbai"


# Data Engineering — Parsing a pipe-delimited record
# Suppose a source system provides records separated by | instead of commas.

record = "ORD101|Rahul|2500|Completed"

rest = record.split("|")
print(rest)

print("Order ID:", rest[0])
print("Customer:", rest[1])
print("Amount:", rest[2])
print("Status:", rest[3])




'''
D. String Repitation / *: Python allows you to repeat a string using the multiplication operator *
'''

print("Hello " * 3)

# Creating Separator
seperator = "-" * 20

print(seperator)
print("DATA PIPELINE")
print(seperator)


# Creating forms
pipe = "Sales ETL"
status = "SUCCESS"

print("=" * 30)
print(f"Pipeline: {pipe}")
print(f"Status: {status}")
print("=" * 30)




'''
E. Indexing() and Slicing(): Indexing and slicing allow you to retrieve individual characters or portions of a string.
'''

'''
                   0   1   2   3   4   5
                   ↓   ↓   ↓   ↓   ↓   ↓
                   P   y   t   h   o   n
                   ↑   ↑   ↑   ↑   ↑   ↑
                  -6  -5  -4  -3  -2  -1
'''

"""Indexing: Extract one character """

text = "Python"

print(text[1])
print(text[-4])



"""Slicing: Extract part of a string """
# string[start:stop:step]
'''exclusive: doesn’t include end term'''

text = "Python"

print(text[0:3])
print(text[2:6])

# Open-ended slicing (Start: ) 
print(text[:4])

# Offset (Skipping character at specific interval) 
print(text[0:4:2])


# Data Engineering — Extract a file extension

file = "sales_data.csv"
             #  -3 -2 -1
ext = file[-3: ]   # filename[-3:] extracts the last three characters.

print(ext)





# Practic questions

txt = "data engineering"

print(txt.replace("data", "cloud"))

print(txt.count("e"))

# Opt: cloud engineering
#      3


record = "101|Rahul|Mumbai"

fields = record.split("|")

print(fields[1])
print(len(fields))

# Opt: Rahul
#      3


# Data Engineering challenge

record = "ORD2026-1042|Rahul|4500.75|COMPLETED"


"""
1. Split the record using |.
2. Extract the order ID, customer name, amount, and status.
3. Convert the amount to a float.
4. Print a formatted message using an f-string.
5. Extract the year (2026) from the order ID using slicing.
"""

# 1
mini_rec = record.split("|")

# 2
print("Order ID:", mini_rec[0])
print("Customer:", mini_rec[1])
print("Amount:", (mini_rec[2]))
print("Status:", mini_rec[3])

# 3
amt = float(mini_rec[2])

print(type(amt))

# 4
print(f"Order Id: {mini_rec[0]}, Customer: {mini_rec[1]}, Amount: {mini_rec[2]}, Status: {mini_rec[3]}")


# 5
id = mini_rec[0]
print(id[3:7])