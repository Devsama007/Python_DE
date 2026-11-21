"""
6. Validation helps us check whether a value has the expected data type or format before processing it.
"""


'''
A. isinstance(): Checks whether a value belongs to a particular data type.
'''

trans_id = 101
amount = 250.50
name = "Alan"

print(isinstance(trans_id, int))
print(isinstance(amount, int))
print(isinstance(name, str))





'''
B. is_integer(): Checks whether a floating-point number has no fractional component.
'''

a = 25.0
b = 25.75
c = -10.4

print(a.is_integer())
print(b.is_integer())
print(c.is_integer())
