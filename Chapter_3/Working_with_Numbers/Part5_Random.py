"""
5. Python provides a random module to generate random values. This is useful for test data generation, simulations, and sampling.
"""

'''
A. random(): Generates a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).
'''
import random

print(random.random())
print(round(random.random(), 2))
print(random.random())

# The output changes each time you run the code.





'''
B. random.randint(); Generates a random integer between the specified minimum and maximum, including both endpoints.
'''
import random

print(random.randint(1, 100))
print(random.randint(100, 500))
print(random.randint(1, 7))



# Suppose you're testing a pipeline and need sample transaction amounts.
import random

for i in range(5):
    amount = random.randint(100, 5000)
    print("Transactions:", i + 1, "Amount:", amount)
