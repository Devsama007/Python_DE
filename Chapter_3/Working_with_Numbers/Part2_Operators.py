
"""
2. Operators are basic maths operators we perform
"""

'''
A. Addition(+): Basic Addition
'''
a = 10
b = 30
print(a + b)


sales = 15000
add_sales = 25000
total = sales + add_sales
print(total)


# Add multiple transaction amounts
transactions = [100, 250, 400, 350]
total = 0

for amount in transactions:
    total = total + amount

print(f"Total amount is: {total}")





'''
B. Subtraction(-): Basic Subtraction
'''
a = 100
b = 40
print(a - b)


total_stock = 500
sold = 175

remain = total_stock - sold
print(remain)





'''
C. Multiplication(*): Basic Multiplication
'''
a = 15
c = 4
print(a * c)


# Calculate total storage
record = 2
total_rec =10000

storage = record * total_rec
print(f"Total storage is: {storage} KB")





'''
D. Division(/): Basic Division
Important: / always returns a floating-point result, even when the division is exact.
'''

a = 10
b = 2
print(a / b)


# Average sales
total = 50000
total_days = 5

avg = total / total_days
print(avg)


# Calculate conversion rate / percentage
total_visitors = 1000
total_customers = 125

conversion_rate = (total_customers / total_visitors) * 100
print(conversion_rate)





'''
E. Floor Division(//): Divides two numbers and rounds the result down to the nearest integer (or lower integer for negative results).
'''

print(10 // 3)
#Opt = 3, 10/3 = 3.333


# Split records into batches
total = 125
batch = 10

total_batches = total // batch
print(total_batches)


# Uneven division
print(17 // 5) #Opt = 3
print(-17 // 5) #Opt = -4, Python floors towards negative infinity, not towards zero.





'''
F. Modulus(%): Returns the remainder after division.
'''
print(10 % 3)
# Opt = 1, 10 = (3 x 3) + 1 Remainder is 1


# Check even and odd
num = 25

if num % 2 == 0:
    print("even")
else:
    print("odd")





'''
G. Exponentiation(**): Raises a number to the power of another number.
'''

print(2 ** 3)
# Opt = 8, 2 ^ 3 = 8


# Calculate compound growth
initial_revn = 100000
growth_rate = 0.10
years = 3

final_rev = initial_revn * (1 + growth_rate) ** years
print(round(final_rev), 2)





# Practice question
# Calculate full batch and remaining records

total_records = 1037
batch_size = 100

full_batches = total_records // batch_size
remaining_records = total_records % batch_size

print("Full batches:", full_batches)
print("Remaining:", remaining_records)





# 2
print(25 // 4) #Opt: 6
print(25 % 4) #Opt: 1
print(-25 // 4) #Opt: -7
print(-25 % 4) #Opt: 3



# 3
res = 10 + 5 * 2 ** 2
print(res)
# first 2 ** 2, sec 5 * 4, last addition


# 4
'''
You receive 2,567 records. Your pipeline processes 250 records per batch.

Calculate:
1. Number of complete batches.
2. Number of remaining records.
3. Total records processed in complete batches.
'''

records = 2567
given_process = 250

#No of complete batches
comp_batch = records // given_process
print(comp_batch)

#No of remaing records
remain = records % given_process
print(remain)

# Total records processed in complete batch
total_records = (records // comp_batch) * comp_batch
print(total_records)

'''
total_records = comp_batch * given_process

print(total_records) Opt = 2500
'''





# 5
'''
A company has an initial revenue of ₹50,000. Revenue grows by 12% annually.

Calculate the revenue after 2 years using exponentiation.
'''

init_revn = 50000
growth = 0.12 #12%
time = 2

#Exponential growth = 
# y = a (1 + r) ^ t

exp_growth = init_revn * (1 + 0.12) ** 2
print(f"Exponential growth: {round(exp_growth, 2)}")





# 6 Advanced – Record distribution
'''
You have 1,003 records and 8 workers. You want to distribute records as evenly as possible.

Calculate:
1. Records each worker gets.
2. Remaining records after equal distribution.
3. Which operator would you use for each calculation?
'''

recs = 1003
workers = 8

#Records each worker gets
each_work = recs // workers
print(each_work)

# Remaining records after equal distribution.
remaining_rec = recs % workers
print(remaining_rec)





# 7
'''
Scenario: Data partitioning

You have 10,257 records. Your pipeline:
- Processes 500 records per batch.
- Has 4 processing workers.
- Needs to calculate how many complete batches each worker can handle if batches are distributed equally.

Calculate:
1. Total complete batches.
2. Remaining records after creating complete batches.
3. Complete batches allocated to each worker.
4. Batches remaining after distributing batches equally.
5. Total records processed by all workers.
'''

rec = 10257
procs = 500
workers = 4

# Total complete batches.
com_batches = rec // procs
print(com_batches)

# Remaining records after creating complete batches
rem_batch = rec % procs
print(rem_batch)

# Complete batches allocated to each worker.
batch_per_worker = com_batches // workers
print(batch_per_worker)


# Batches remaining after distributing batches equally.
batches_remain = com_batches % workers
print(batches_remain)

# Total records processed by all workers
total_rec = (rec // workers) * workers
print(total_rec)
'''
total_rec = com_batches * procs
print(total_rec)
'''
