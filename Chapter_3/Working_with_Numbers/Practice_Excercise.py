"""
Level 1 – Fundamentals
"""

"""
Q1. Type conversion and validation

You receive the following transaction data:

Tasks:
1. Convert transaction_id into an integer.
2. Convert quantity into an integer.
3. Convert price into a float.
4. Calculate the total transaction amount.
5. Check whether the converted values have the expected types using isinstance().
6. Print the final transaction details.
"""

transaction_id = "1052"
quantity = "12"
price = "149.75"

# Convert transaction_id into an integer.
trn_id = int(transaction_id)
print(trn_id)

# Convert quantity into an integer.
qty = int(quantity)
print(qty)

# Convert price into a float.
prz = float(price)
print(prz)

# Calculate the total transaction amount.
total_amt = qty * prz
print("Total amount:", total_amt)

# Check whether the converted values have the expected types using isinstance().

print(isinstance(trn_id, int))
print(isinstance(qty, int))
print(isinstance(prz, float))

# Print the final transaction details.
print(type(trn_id))
print(type(qty))
print(type(prz))





"""
Q2. Operators and batch calculations

A system receives 12,875 records.
- Each batch processes 400 records.
- There are 5 workers.

Calculate:
1. Complete batches.
2. Remaining records.
3. Total batches required.
4. Complete batches allocated to each worker.
5. Undistributed complete batches.
6. Total records processed by complete batches.
Use //, %, and math.ceil().
"""

records = 12875
processes = 400
workers = 5

# Complete batches.
comp_batch = records // processes
print("Complete Batches:", comp_batch)

# Remaining records.
rem_batch = records % processes
print("Remaining Bathces:", rem_batch)

# Total batches required.
import math
total_batch = math.ceil(records / processes)
print("Total Batches:", total_batch)

# Complete batches allocated to each worker.
comp_batch_each = comp_batch // workers
print("Complete batches allocated to each worker:", comp_batch_each)

# Undistributed complete batches.
und_batch = comp_batch % workers
print("Undistributed complete batches:", und_batch)

# Total records processed by complete batches
total_comp = comp_batch * processes
print("Total records processed by complete batches:", total_comp)





"""
Level 2 – Numerical processing
"""

"""
Q3. Rounding and data quality

Your source and destination systems report:

Calculate:
1. Absolute difference.
2. Percentage difference relative to the source.
3. Round the percentage to 2 decimal places.
4. If the percentage difference exceeds 0.5%, print "Data quality alert"; otherwise print "Data is within tolerance".
"""

source = 250000
destination = 248765

# Absolute difference.
abs_dif = abs(source - destination)
print("Absolute difference:", abs_dif)

# Percentage difference relative to the source.
# Round the percentage to 2 decimal places.
per_diff = round((abs_dif / source) * 100, 2)
print("Percentage difference relative to the source:", per_diff)

# If the percentage difference exceeds 0.5%, print "Data quality alert"; otherwise print "Data is within tolerance".
if per_diff > 0.5:
    print("Data quality alert")
else:
    print("Data is within tolerance")





"""
Q4. Advanced math

Calculate:
1. Vertical distance using sin().
2. Horizontal distance using cos().
3. Standard deviation using sqrt().
4. Number of divisions required to reduce 8,192 records to one using logarithm base 2.
Round the first three results to 2 decimal places.
"""

distance = 500
angle = 60
variance = 324
records = 8192

import math
# Vertical distance using sin()
ver_dist = round(distance * math.sin(math.radians(angle)), 2)
print("Vertical distance:", ver_dist)

# Horizontal distance using cos().
hoz_dist = round(distance * math.cos(math.radians(angle)), 2)
print("Horizontal distance:", hoz_dist)

# Standard deviation using sqrt()
std_dev = math.sqrt(variance)
print("Standard deviation", std_dev)

# Number of divisions required to reduce 8,192 records to one using logarithm base 2
logs = math.log(records, 2)
print("No of divisions:", logs)





"""
Level 3 – Data Engineering challenges
"""

"""
Q5. Random test-data generator

Generate 10 sample transaction records.

Requirements:
- Transaction ID: random integer between 1000 and 9999.
- Quantity: random integer between 1 and 20.
- Unit price: random floating-point number between 10 and 500.
- Calculate transaction amount.
- Round transaction amount to 2 decimal places.
- Print each transaction.
"""

import random

for i in range(10):
    trn_id = random.randint(1000, 9999)
    qty = random.randint(1, 20)
    price = round(10 + random.random() * (500 - 10), 2)
    amount = round(qty * price, 2)

    print(f"Transaction id: {trn_id}, Quantity: {qty}, Price: {price}, Amount: {amount}")