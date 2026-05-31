print("--------Exception Handling---------")
# try:
#     a = int(input("Enter a number : "))
#     b = int(input("Enter another number : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero!") 
# except ValueError:
#     print("Enter only an integer value .")
    
#or
import logging
logging.basicConfig(filename="newfile.txt" , level=logging.DEBUG)
try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))
    print(a/b)
except(ZeroDivisionError , ValueError) as msg:
    print(msg)
    logging.exception(msg)
print("Logging level is set up !")
# else: 
#     print("Everything is Ok!")

print("------File Handling------")
import csv
f = open("Employee.csv",'a')
a = csv.writer(f)
#a.writerow(["EmpID","Empname","Empage"])
print("File has been created!")
EmpID = int(input("Enter a value : "))
Empname = input("Enter the data : ")
Empage = input("Enter the age : ")
a.writerow([EmpID,Empname,Empage])

