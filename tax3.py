import datetime
 
 
class Tax:
 
   def __init__(self, name, age, gender, address, phone, marStatus, insurance, premium, disability, diplomat, income):
       self.name = name
       self.age = age
       self.gender = gender
       self.address = address
       self.phone = phone
       self.marStatus = marStatus.lower()
       self.income = int(income * 12)
       self.insurace = insurance
       self.premium = premium
       self.disability = disability
       self.diplomat = diplomat
       self.tax = 0
 
   @staticmethod
   def top():
       print("\n\tInland Revenue Income System\n\t\tLazimpat,Kathmandu")
       print("==================================================")
       print("  Welcome to Income Tax Calculation System")
       print("==================================================\n")
       print("\t\t\t\tDate: ", datetime.date.today(), "\n")
       num = int(input("Enter number of customers:"))
       return num
 
   @staticmethod
   def information():
       name = input("Input the name: ")
       age = int(input("Input the age: "))
       gender = input("Input the gender(M,F): ").lower()
       address = input("Input the address: ")
       phone = input("Input the phone no: ")
       marStatus = input("Input the marriage status-(y for married/n for unmarried):: ").lower()
       disability = input("Do you have any disability (y/n):: ").lower()
       diplomat = input("Do you have a diplomat job (y/n):: ").lower()
       insurance = input("Do you have any insurance (y/n):: ").lower()
       if (insurance == 'y'):
           premium = int(input("Input premium amount:"))
       else:
           premium = 0
       income = int(input("Input the monthly income:: "))
       return Tax(name, age, gender, address, phone, marStatus, insurance, premium, disability, diplomat, income)
 
   def unmarried(self):
       taxPayable = 0
       dis = 0
       if (self.income <= 400000):
           taxPayable = self.income * 0.01
       else:
           if (self.income > 400000 and self.income <= 500000):
               temp = self.income - 400000
               taxPayable = temp * 0.1 + 400000 * 0.01
           elif (self.income > 500000 and self.income <= 700000):
               temp = self.income - 500000
               taxPayable = temp * 0.2 + 100000 * 0.1 + 400000 * 0.01
           elif (self.income > 700000 and self.income <= 2000000):
               temp = self.income - 700000
               taxPayable = temp * 0.3 + 200000 * 0.2 + 100000 * 0.1 + 400000 * 0.01
           elif (self.income > 2000000):
               temp = self.income - 2000000
               taxPayable = temp * 0.36 + 1300000 * 0.3 + 200000 * 0.2 + 100000 * 0.1 + 400000 * 0.01
 
       if (self.insurace == 'y'):
           dis += taxPayable - 20000
       if (self.disability == 'y'):
           dis += taxPayable * 0.5
       if (self.diplomat == 'y'):
           dis = taxPayable * 0.75
       if (self.gender == 'f'):
           dis += taxPayable * 0.1
 
       return taxPayable - dis
 
   def married(self):
       taxPayable = 0
       dis = 0
       if (self.income <= 450000):
           taxPayable = self.income * 0.01
       else:
           if (self.income > 450000 and self.income <= 550000):
               temp = self.income - 450000
               taxPayable = temp * 0.1 + 450000 * 0.01
           elif (self.income > 550000 and self.income <= 750000):
               temp = self.income - 550000
               taxPayable = temp * 0.2 + 100000 * 0.1 + 450000 * 0.01
           elif (self.income > 750000 and self.income <= 2000000):
               temp = self.income - 750000
               taxPayable = temp * 0.3 + 200000 * 0.2 + 100000 * 0.1 + 450000 * 0.01
           elif (self.income > 2000000):
               temp = self.income - 2000000
               taxPayable = temp * 0.36 + 1250000 * 0.3 + 200000 * 0.2 + 100000 * 0.1 + 450000 * 0.01
 
       if (self.insurace == 'y'):
           dis += taxPayable - 20000
       if (self.disability == 'y'):
           dis += taxPayable * 0.5
       if (self.diplomat == 'y'):
           dis = taxPayable * 0.75
       if (self.gender == 'f'):
           dis += taxPayable * 0.1
 
       return taxPayable - dis
 
   def displayTop(self):
       f = open("display.txt", "w")
       list = ["\t\tInland Revenue Income System\n", "\t\t\tLazimpat,Kathmandu\n",
               "==================================================\n",
               "  Welcome to the Income Tax Calculation System\n",
               "==================================================\n",
               "\t\t\t\t\t\t\t\t\tDate: {}\n\n".format(datetime.date.today())]
       f.writelines(list)
       f.close()
 
   def display(self):
       f = open("display.txt", "a")
       list = ["Name: {}\t".format(self.name), "\t\t\t\t\tAddress: {}\n".format(self.address),
               "Age: {}\t".format(self.age), "\t\t\t\t\tGender: {}\n".format(self.gender),
               "Phone: {}\t".format(self.phone), "\t\t\t\t\tMarriage Status: {}\n".format(self.marStatus),
               "Disability: {}\t".format(self.disability), "\t\t\t\t\tDiplomat: {}\n".format(self.diplomat),
               "Insurance: {}\t".format(self.insurace), "\t\t\t\t\tIncome: {}\n".format(self.income),
               "\nTaxable amount= Rs. {}\n\n".format(self.tax)]
       f.writelines(list)
       print("\nTax Calculation Completed..\n")
       f.close()
 
 
num = Tax.top()
employees = []
 
for x in range(num):
   empx = Tax.information()
   if (empx.marStatus == 'n'):
       empx.tax = empx.unmarried()
   else:
       empx.tax = empx.married()
 
   empx.displayTop()
   empx.display()
   employees.append(empx)
