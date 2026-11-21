# ************ Number Types in Python ************

"""
Types: type(), int()

Math Operators

Rounding: abs(), round(), ceil(), floor(), trunc()

Advance Maths: sqrt(), pow(), log(), log10(), exp(), sin(), cos()

Random: random(), randint(), uniform()

Validation: isinstance(), is_integer(), is_float()

"""


"""
1. Types: we have four types
   type(), int(), float(), complex()
"""

'''
A. type(): function tells you the data type of a value or variable.
'''

x = 5
y = 3.14
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))



# Check data received from an API

cust_data = {
    "cust_id": 101,
    "balance": 3500.75,
    "active": True
}

for key, value in cust_data.items():
    print(key, type(value))





'''
B. int(): The int() function converts compatible values into integers.
'''

price = 99.560

print(type(price))
print(type(int(price)))


#Negative float
val = -46.78

print(type(val))
print(type(int(val)))





'''
C. float(): The float() function converts compatible values into floating-point numbers.
'''

price = 99

print(type(price))
print(type(float(price)))


#Negative float
val = -46

print(type(val))
print(float(val))
print(type(float(val)))


#Scientific notation
val = "2.5e3"
print(float(val))

#e3 means multiply by 10^3 = 2.5 x 10^3 = 2500.0


'''
float() can introduce precision limitations for decimal values.

For financial calculations, Python's decimal.Decimal is often more appropriate.
'''

from decimal import Decimal

price = Decimal("10.25")
tax = Decimal("2.50")

print(price + tax)  # Output: 12.75
print(type(price + tax))  # Output: <class 'decimal.Decimal'>





'''
D. complex(): A complex number contains two parts:
- Real part
- Imaginary part
In Python, j represents the imaginary unit.
'''

num = complex(2, 3)

print(num)
print(type(num))

#Or dirctly printing real and imaginary parts
print(num.real)
print(num.imag)

print(type(num.real)) # Gives float type



# Complex number calculations
a = 5 + 3j
b = 2 + 4j

print("Addition: ", a + b)
print("Multiplication: ", a * b)






######### 4. Data Engineering challenge #########

# 1)
a = "200"
b = 50

print(a + str(b)) #Gives concatination: 20050
print(int(a) + b) #Gives sum: 250



# 2)
'''
You receive this raw transaction data:
transaction = {
    "transaction_id": "1001",
    "quantity": "5",
    "price": "249.99"
}

    Convert transaction_id into an integer.    
    Convert quantity into an integer.
    Convert price into a float.
    Calculate the total transaction amount.
    Print the result and its data type.
'''

transaction = {
    "transaction_id": "1001",
    "quantity": "5",
    "price": "249.99"
}

#1, 2, 3, 5
for key, value in transaction.items(): 
    if key == "transaction_id":
        Id = int(value)
        print(type(Id))
        print(f"Transaction_id: {Id}")
      #print(f"Transaction_id: {int(value)}")

    elif key == "quantity":
        Qnty = int(value)
        print(type(Qnty))
        print(f"Quantity: {Qnty}")

    elif key == "price":
        price = float(value)
        print(type(price))
        print(f"Price: {price}")

qty = int(transaction["quantity"])
pric = float(transaction["price"])

print(f"Total Transaction amount: {qty * pric}")




# Advanced conversion challenge
# print(int("45.75")) invalid literal for int()
print(float("45.75"))
print(int(float("45.75")))