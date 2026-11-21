
"""
A company receives messy customer data from an external CSV file and needs to clean it before inserting it into PostgreSQL.
"""

''' 
Customer ID	 |    Name	   |      Email	          |    Country	 |    Status
" C101 "     |  " AJAY "   |  " AJAY@GMAIL.COM "  |   " india "  |  " SUCCESS "
"C102"	     |  " rahul "  |  "rahul@gmail.com"	  |   " USA "	 |  " pending"
" C103"	     |  "PRIYA"	   |  " PRIYA@YAHOO.COM"  |   "INDIA"	 |  " Failed "
"C104 "	     |  "  amit"   |  "AMIT@GMAIL.COM "	  |   " uk"	     |  "SUCCESS"
'''



'''
Your task
Write a Python program that cleans all the records.

Cleaning requirements:
Field	Required operation
Customer ID	Remove spaces and convert to uppercase
Name	Remove leading/trailing spaces
Email	Remove spaces and convert to lowercase
Country	Remove spaces and convert to uppercase
Status	Remove spaces and convert to lowercase
'''



customers = [
    [" C101 ", " AJAY ", " AJAY@GMAIL.COM ", " india ", " SUCCESS "],
    ["C102", " rahul ", "rahul@gmail.com", " USA ", " pending"],
    [" C103", "PRIYA", " PRIYA@YAHOO.COM", "INDIA", " Failed "],
    ["C104 ", "  amit", "AMIT@GMAIL.COM ", " uk", "SUCCESS"]
]

#Transforming the data according to the cleaning requirements

cleaned_rec = []

for cust in customers:

    cust_id = cust[0].strip().upper()
    name = cust[1].strip()
    email = cust[2].strip().lower()
    country = cust[3].strip().upper()
    stat = cust[4].strip().lower()

    cleaned_rec.append([cust_id, name, email, country, stat])

for rec in cleaned_rec:
    print(rec)



'''
Bonus challenge – Data validation
Let's make it slightly harder.

After cleaning the records, add these validations:
1. Customer ID must start with "C".
2. Email must end with "@gmail.com" or "@yahoo.com".
3. Country must contain only alphabetic characters.
4. Status must be either "success", "pending", or "failed".
'''

for rec in cleaned_rec:

    #We will check with if not
    if not rec[0].startswith("C"):
        print(f"Invalid Customer ID: {rec[0]}")

    if not (rec[2].endswith("@gmail.com") or rec[2].endswith("@yahoo.com")):
        print(f"Invalid Email: {rec[2]}")

    if not rec[3].isalpha():
        print(f"Invalid Country: {rec[3]}")

    if not rec[4] in ["success", "pending", "failed"]:
        print(f"Invalid Status: {rec[4]}")