"""
4. Advance Math: we have four types
math.sqrt() – Square root

math.sin() – Sine

math.cos() – Cosine

math.log() – Logarithm
"""

'''
A. math.sqrt() Square Root: Square root finds a number which, when multiplied by itself, gives the original number.
'''

import math

print(math.sqrt(25))
print(math.sqrt(64))
print(round(math.sqrt(60), 3))

print(type(math.sqrt(25)))
#Notice that the result is a float, even when the answer is a whole number.




# Data Engineering: Statistical calculations
# Suppose you're analyzing how much individual transaction values deviate from their average. One common statistical measure is standard deviation.

import math
variance = 144
std_dev = math.sqrt(variance)

print(std_dev)

'''Note: math.sqrt() raises a ValueError for negative numbers. It works with non-negative real numbers.'''





'''
B. math.sin() Sin: It is commonly used in trigonometry, geometry, physics, and scientific computing.

Important: Python's math.sin() accepts angles in radians, not degrees.
'''

import math

print(math.sin(0))

print(math.sin(math.pi / 2)) #90 deg

print(math.sin(math.pi))  #180 deg



# Using degrees
import math

print(round(math.sin(math.radians(30)), 3))

print(round(math.sin(math.radians(45)), 3))

print(math.sin(math.radians(90)))



# magine calculating the vertical component of an object's movement.
import math

dist = 100
angle = 30

vertical_dist = dist * math.sin(math.radians(angle))

print(round(vertical_dist, 2))





'''
C. math.cos() Cosine: It is commonly used in trigonometry, geometry, physics, and scientific computing.

Important: Python's math.sin() accepts angles 
'''

import math

print(math.cos(0))

print(round(math.cos(math.pi / 3), 2))

print(math.cos(math.pi / 2))



# Using degrees
import math

print(round(math.cos(math.radians(0)), 2))

print(round(math.cos(math.radians(60)), 2))

print(round(math.cos(math.radians(90)), 2))



# Suppose an object moves 100 metres at an angle of 60°.
import math

distance = 100
angle = 60

horizontal_dist = distance * math.cos(math.radians(angle))

print(round(horizontal_dist, 2))





'''
D. math.log() Logarithm: To what power must we raise a base to get a particular number?
'''

import math

print(math.log(1))

print(math.log(math.e))

print(math.log(math.e ** 2))



# Specifying the base
# Imagine a data-processing algorithm repeatedly divides a dataset into two equal parts.

# For 1,024 records, how many times can you divide it by 2 before reaching 1

import math

records = 1024

steps = math.log(records, 2)

print(steps)
# opt: 10 , 2^10 = 1024





# 1) Practice questions

# You are analyzing a dataset.
import math

variance = 225 

# Calculate the standard deviation using math.sqrt().

std_deviatn = math.sqrt(variance)
print(std_deviatn)
# Opt: 15



# 2) 
'''
Your pipeline repeatedly divides a dataset into two equal parts.
Calculate how many divisions are required to reach one record using math.log().
'''
import math

records = 4096

divsn = math.log(records, 2)
print(divsn)




# 3)
'''
A data analytics system has the following measurements:
distance = 250
angle = 45
variance = 196
records = 2048

Calculate:
1. Vertical distance using sin().
2. Horizontal distance using cos().
3. Standard deviation using sqrt().
4. Number of divisions required to reduce the dataset to one record using log() with base 2.
'''

import math

distance = 250
angle = 45
variance = 196
records = 2048

# Vertical distance using sin().
vert_dist = distance * math.sin(math.radians(angle))
print(round(vert_dist, 2))

# Horizontal distance using cos().
horz_dist = distance * math.cos(math.radians(angle))
print(round(horz_dist, 2))

# Standard deviation using sqrt().
std_deviation = math.sqrt(variance)
print(std_deviation)

# Number of divisions required to reduce the dataset to one record using log() with base 2.
no_of_div = math.log(records, 2)
print(no_of_div)