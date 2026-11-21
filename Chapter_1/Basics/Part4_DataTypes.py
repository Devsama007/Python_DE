# ************ Data Types in Python ************

""" In Python there are several built-in data types that are used to store and manipulate data. These data types can be categorized into the following main types: """



"""
1. Numeric Types: These data types are used to represent numbers. The main numeric types in Python are:
   - int: Represents integer values (e.g., 1, -5, 42).
   - float: Represents floating-point numbers (e.g., 3.14, -0.001).
   - complex: Represents complex numbers (e.g., 2 + 3j).        
"""

# Integer
age = 23
temp = -5
count = 0

print(age, temp, count)
print(type(age))


# Float
price = 99.57
tempr = -2.5
avg = 85.65

print(price)
print(tempr)
print(avg)
print(type(price))


# Complex
a = 2 + 3j
b = 4 + 2j

print(a)
print(b)
print(a.real)
print(a.imag)
print(a + b)


# Bonus: Data Engineering example
# Suppose you're processing sales data from a CSV file.

quantity = 17 #int\
pri = 149.99 #float

total = quantity * pri 

print("Total sales: ", total)
print(type(quantity))
print(type(pri))
print(type(total))



"""
2. String Types: Strings are used to represent text. In Python, strings are enclosed in either single quotes (' ') or double quotes (" "). For example:
   - str: Represents a sequence of characters (e.g., "Hello, World!", 'Python is fun!').   
"""        

name = "John Doe"
msg = "Data Engineering is awesome!"

print(name)
print(msg)
print(type(msg))

# String concatenation and f-strings
# You can combine strings using + or insert variables into strings using an f-string.
f_name = "John"
l_name = "Cena"

full_name = f_name + " " + l_name
print(full_name)

age = 24
print(f"My name is {full_name} and I am {age} years old.") # Using f string



"""
3. Boolean Type: The boolean type is used to represent truth values. It can have one of two possible values:
   - bool: Represents either True or False. For example, is_active = True, is_logged_in = False.
"""

ag = 22
min_ag = 18

print(ag > min_ag)
print(ag < min_ag)
print(ag == min_ag)


# Boolean conditions in Data Engineering
# Suppose you're processing customer records and want to identify active customers.

cust_name = "Kane"
is_active = True
purchase_amt = 1500

if is_active and purchase_amt > 1000:
    print(f"{cust_name} is an eligible customer.")
else:
    print("Customer is not eligible")



"""
4. Date and Time Types: Python provides the datetime module to work with dates and times. The main types in this category are:
   - datetime: Represents a specific date and time (e.g., datetime.datetime(2023, 5, 15, 10, 30)).   
   - date: Represents a date (e.g., datetime.date(2023, 5, 15)).
   - time: Represents a time (e.g., datetime.time(10, 30, 0)).
"""

#need to import first
from datetime import date, time, datetime

order_date= datetime(2026,  11,   20,   10,    30,     0)
                   # Year, Month, Day, Hour, Minute, Second

print(order_date)
print(order_date.year)
print(order_date.month)
print(order_date.hour)



"""
5. Sequence Types: These data types are used to store collections of items. The main sequence types in Python are:
   - list: Represents an ordered collection of items (e.g., [1, 2, 3], ['apple', 'banana', 'cherry']).

   - tuple: Represents an ordered, immutable collection of items (e.g., (1, 2, 3), ('a', 'b', 'c')).

   - range: Represents a sequence of numbers (e.g., range(0, 10)).  

   - set: Represents an unordered collection of unique items (e.g., {1, 2, 3}, {'apple', 'banana', 'cherry'}).

   - dict: Represents a collection of key-value pairs (e.g., {'name': 'Alice', 'age': 30}, {1: 'one', 2: 'two'}).

   - array: Represents a collection of items of the same type (e.g., numpy.array([1, 2, 3])).
"""

'''
*************** 1) LIST ****************
A list stores multiple items in an ordered collection. Lists are mutable, meaning you can add, remove, or change elements.
'''
num = [10, 20, 30, 40]
print(num)
print(num[0])
print(num[-1])  # Accessing the last element


fruits = ['apple', 'banana', 'cherry']

fruits.append("mango") #Adding
fruits[2] = "orange"
print(fruits)


# Example 3: Data Engineering — Processing records
sales = [1200, 2500, 1000, 3000]

total_sales = sum(sales)
higest_sales = [amount for amount in sales if amount > 2000]

print("Total sales: ", total_sales)
print("Highest sales: ", higest_sales)



'''
*************** 2) TUPLE ****************
A tuple stores multiple items in an ordered collection. Unlike a list, a tuple is immutable, meaning you cannot change its elements after creation.
'''
person = ("Lie", 45, "Bob")
print(person)
print(person[2])

# Example 3: Data Engineering — Fixed configuration
data_con = ("localhost", 4040, "mydb")
host, port, db = data_con
print("Host:", host)
print("Port:", port)



'''
*************** 3) RANGE ****************
range represents a sequence of integers. It is commonly used in loops and generates numbers as needed instead of storing every number in a list.
'''

for no in range(1, 10):
   print(no)


# range(start, stop, step) increases the value by step each time. Here, it increases by 3
for no in range(1, 15, 3):
   print(no)


# Data Engineering — Batch processing
records = ['A', 'B', 'C', 'D', 'E']
batch_SIZE = 2

for i in range(0, len(records), batch_SIZE):
   batch = records[i:i + batch_SIZE]
   print(batch) 


'''
*************** 4) SET ****************
A set stores unique items. Duplicate values are removed automatically, and sets do not guarantee positional order.
'''

noms = {1, 2, 2, 5, 5, 5, 6}
print(noms)
print(len(noms))


con_a = {"India", "Japan", "USA"}
con_b = {"Russia", "Germany", "Japan"}

print(con_a & con_b) # & finds common items (intersection)
print(con_a | con_b) # | combines unique items (union)
print(con_a - con_b) # - finds items present in the first set but absent from the second (difference).


# Data Engineering — Finding unique IDs
cust_ids = {101, 102, 103, 101, 104, 102}
print("Unique customer IDs:", cust_ids)
print(len(cust_ids))


# Can also use set() to remove duplicates from a list
cust_ids_list = [101, 102, 103, 101, 104, 102]
unique = set(cust_ids_list)
print(unique)


'''
*************** 5) DICTIONARY ****************
A dictionary stores data as key-value pairs. Each key is unique, and you use the key to access its corresponding value. Its mutable, meaning you can add, remove, or change key-value pairs.
'''

emp = {
   "id": 201,
   "name": "John Doe",
   "department": "Data Engineering"
}

print(emp["name"])
print(emp["department"])

# name key is John Doe and department key is Data Engineering


#Adding example
emp = {"name": "Becky", "salary": 30000}

emp["name"] = "Becky Smith"
emp["city"] = "Nevada"

print(emp)


# Data Engineering — Processing JSON-like data
order = {
   "order_id": 1002,
   "customer": "Alice",
   "amount": 250.75,
   "status": "completed"
}

if order["status"] == "completed":
   print(f"Order amount: {order["amount"]} Has been debited from your account")
else:
   print("Order is in progress")


'''
*************** 6) ARRAY ****************
An array stores multiple elements, generally of the same data type. Python provides the built-in array module, while NumPy arrays are widely used for numerical and scientific data processing.
'''

# 1: Built-in Python array
from array import array

temp = array('i', [25, 30, 28, 32]) # i stand for Standard integer (4 bytes). In python we need to include array element types as well (i = int, f = float, u = string, b = char etc)

print(temp)
print(temp[2])



# 2: NumPy array
import numpy as np

sale = np.array([1000, 2000, 3000])

print(sale * 2)
print(sale.mean())
print(sale.sum())


# Data Engineering — Analyzing numerical data
# Numpy question
print("Basic sales")

daily_sales = np.array([1600, 1800, 1400, 3000, 2600])

avg_sales = daily_sales.mean()

highest_sales_days = daily_sales[daily_sales > avg_sales]

print("Average: ", avg_sales)
print("Above avg:", highest_sales_days)


"""
Type          | Ordered?             | Mutable?             | Duplicates?                         | Typical use
----------------------------------------------------------------------------------------------------------------------------
list          | Yes                  | Yes                  | Allowed                             | Collections of records
tuple         | Yes                  | No                   | Allowed                             | Fixed groups of values
range         | Yes                  | No                   | No repeated values in its sequence  | Looping and index ranges
set           | No positional order  | Yes                  | Not allowed                         | Unique values and comparisons
dict          | Insertion order      | Yes                  | Keys must be unique                 | Structured key-value data
array         | Yes                  | Yes                  | Allowed                             | Same-type values
NumPy ndarray | By index/axis        | Elements can change  | Allowed                             | Numerical computation
"""



"""
6. None Type: The None type is used to represent the absence of a value or a null value. It is often used to indicate that a variable has no value assigned to it. For example:
   - None: Represents the absence of a value (e.g., my_variable = None).
"""

#A function that returns None
#If a Python function doesn't explicitly return a value, it automatically returns None.
def greet():
    print("Hello")

res = greet()

print(res)
print(type(res))