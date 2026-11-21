"""
3. Rounding: we have five types
abs() – Absolute value

round() – Round to nearest value

math.ceil() – Round up

math.floor() – Round down

math.trunc() – Remove decimal part
"""


'''
A. abs() Absolute Value: abs() returns the distance of a number from zero. It removes the negative sign if one exists.
'''

print(abs(25))
print(abs(-25))
print(abs(-0.75))


# Suppose you're comparing daily record counts between two systems.
src_rec = 10500
tar_rec = 10380

diff = abs(src_rec - tar_rec) #or we can subtract reverse

print("Record mismatch:", diff)





'''
B. round() Round to Nearest Value: round() rounds a number to the nearest integer or specified decimal places.
'''

# Basic rounding
print(round(10.4))
print(round(10.6)) # depends on nearest ceil and floor
print(round(15.9))


# Decimal precision
price = 249.56789

print(round(price, 2))
print(round(price, 3))
print(round(price, 0))


# Suppose a pipeline processes records in different durations.
processing_times = [2.456, 3.789, 4.123]
avg = sum(processing_times) / len(processing_times)
print(round(avg, 2))


'''
Important Python behavior: Banker’s rounding

Python uses round half to even for exact halfway cases.
'''
print(round(4.5)) #Opt = 4

'''
When a number is exactly halfway, Python rounds towards the nearest even integer.

For financial calculations, don't blindly rely on round() with floating-point values. Python's decimal.Decimal is generally a better choice when exact decimal rounding is required.
'''





'''
C. math.ceil() Round up: ceil() rounds a number up to the smallest integer greater than or equal to it.

It requires importing math
'''
import math

print(math.ceil(4.3))
print(math.ceil(4.8))
print(math.ceil(5.0))
print(math.ceil(-4.2))
print(math.ceil(-4.8))
# Notice that rounding up means moving towards positive infinity, not simply increasing the absolute value.


# Suppose you have 10,257 records and want to process 500 records per batch.
# How many batches are required to process every record?

import math

total_rec = 10257
batch_size = 500

act_total = (total_rec / batch_size)
total_batches = math.ceil(total_rec / batch_size)

print(act_total)  #Opt: 20.514
print(total_batches) #Opt: 21





'''
D. math.floor() Round down: floor() rounds a number down to the greatest integer less than or equal to it.

It requires importing math
'''

import math

print(math.floor(4.2))
print(math.floor(4.8))
print(math.floor(5.0))
print(math.floor(-4.2))
print(math.floor(-4.9))


# Suppose you have 10,257 records and want to process 500 records per batch.
# How many batches are required to process every record?

import math

total_rec = 10257
batch_size = 500

act_total = (total_rec / batch_size)
total_batches = math.floor(total_rec / batch_size)

print(act_total)  #Opt: 20.514
print(total_batches) #Opt: 20





'''
E. math.trunc() Remove Decimal Part: trunc() removes the decimal portion of a number without rounding. It moves towards zero

It requires importing math
'''

import math

print(math.trunc(4.9))
print(math.trunc(4.2))
print(math.trunc(-4.9))


# Processing numerical values
import math

procs_sec = 125.85
whole_sec = math.trunc(procs_sec)
print(whole_sec)


'''
int() vs trunc()
If you are not using math already, just use int(), its simple and build in

If you have already imported trunc then use trunc
'''







# 1) Understand the difference
import math

x = -12.6

a = math.ceil(x)
b = math.floor(x)
c = math.trunc(x)

print(a, b, c)



# 2)
'''
You have 15,678 records. Each batch can process 750 records.

Calculate:
1. Number of complete batches.
2. Remaining records.
3. Total batches required to process all records.
4. Records processed in the final batch.
'''

import math
records = 15678
process = 750

# Number of complete batches.
com_batches = records // process
print(com_batches)

# Remaining records. / Records processed in the final batch.
remaining = records % process
print(remaining)

# Total batches required to process all records.
total_batch = math.ceil(records / process)
print(total_batch)




# 3)
'''
Your source and destination databases contain different record counts.
'''

source_count = 125678
destination_count = 124923

difference_noabs = source_count - destination_count
difference = abs(source_count - destination_count)

percentage_difference = (difference / source_count) * 100

print(difference_noabs)
print(difference)
print(round(percentage_difference, 2))

# abs gives distance from zero, if diff causing negative, abs will give positive





# 4)
'''
Q5. Challenge – Pipeline allocation

A pipeline processes 28,765 records. Each worker processes 1,200 records per batch. You have 6 workers.

Calculate:
1. Complete batches.
2. Total batches required.
3. Remaining records after complete batches.
4. If batches are distributed equally, how many complete batches does each worker get?
5. How many batches remain undistributed?
6. How many records are processed by the complete batches?
'''

import math
recds = 28765
procs = 1200
workers = 6

# Complete batches.
comp_batch = math.ceil(recds / procs)
print(comp_batch)

# Total batches required.
tot_batch = recds // procs
print(tot_batch)

# Remaining records after complete batches.
remain_recs = recds % procs
print(remain_recs)

# If batches are distributed equally, how many complete batches does each worker get
eq_batch_per_wrk = tot_batch // workers
print(eq_batch_per_wrk)

# How many batches remain undistributed
batch_remain = tot_batch % workers
print(batch_remain)

# How many records are processed by the complete batches?
complete_batch_records = (recds // procs) * procs
print(complete_batch_records)

'''
Correct but more better way

import math

recds = 28765
procs = 1200
workers = 6

# Complete batches
comp_batch = recds // procs
print("Complete batches:", comp_batch)

# Total batches required
tot_batch = math.ceil(recds / procs)
print("Total batches:", tot_batch)

# Remaining records
remain_recs = recds % procs
print("Remaining records:", remain_recs)

# Distribute complete batches equally
eq_batch_per_wrk = comp_batch // workers
print("Complete batches per worker:", eq_batch_per_wrk)

# Undistributed complete batches
batch_remain = comp_batch % workers
print("Undistributed complete batches:", batch_remain)

# Records processed by complete batches
complete_batch_records = comp_batch * procs
print("Records processed:", complete_batch_records)
'''