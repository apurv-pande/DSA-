import csv
f = open("Employee.csv",'a')
a = csv.writer(f)
#a.writerow(["EmpID","Empname","Empage"])
print("File has been created!")
EmpID = int(input("Enter a value : "))
Empname = input("Enter the data : ")
Empage = input("Enter the age : ")
a.writerow([EmpID,Empname,Empage])