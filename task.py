#col name : studname phy chem maths total percentage result
# input studid studname phy chem maths
# calculate total percentage
# check condition all paper marks >= 40 then pass  
# student_result_csv.py

import csv
import os

filename = "students.csv"
file_exists = os.path.isfile(filename)
# Input student details
studid = input("Enter Student ID: ")
studname = input("Enter Student Name: ")
phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chemistry Marks: "))
maths = int(input("Enter Maths Marks: "))

# Calculate total and percentage
total = phy + chem + maths
percentage = total / 3

# Result condition
if phy >= 40 and chem >= 40 and maths >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Open CSV file
with open(filename, "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            "studid",
            "studname",
            "phy",
            "chem",
            "maths",
            "total",
            "percentage",
            "result"
        ])
    writer.writerow([
        studid,
        studname,
        phy,
        chem,
        maths,
        total,
        f"{percentage:.2f}",
        result
    ])
print("Record Saved Successfully!")