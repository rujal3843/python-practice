import datetime

def staticInformation():
    print("-------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\tIncome Tax Calculation System")
    print("\t\t\t\t\t\t\t\t\t\tSatdobato, Lalitpur")
    print("--------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tWelcome to the Income Tax Calculation System")
    print("\t\t\t\t\t\t\t\t\tDate:",datetime.datetime.now())
    print("--------------------------------------------------------------------------------------------------------------")

def details():
    name=input("Enter Your Name::")
    add=input("Enter Your address::")
    age=int(input("Enter Your Age::"))
    status=input("Are you married or unmarried(M/U)::")
    print("---------------------")
    income=int(input("Enter the Monthly income::"))
    yearly_income=income*12
    return name,add,age,status,income,yearly_income

def calculateMarried(yearly_income):
        if(yearly_income<400000):
            tax_amount=yearly_income*0.01
            print("Your taxable amount is",tax_amount)
        elif(yearly_income>=400000 or yearly_income<500000):
            tax_amount=4500+((yearly_income-400000)*0.1)
            print("Your taxable amout is",tax_amount)
        elif(yearly_income>=500000 and yearly_income<700000):
            tax_amount=14500+((yearly_income-500000)*0.2)
            print("Your taxable amount is",tax_amount)
        elif(yearly_income>=700000 and yearly_income<2000000):
            tax_amount=54500+((yearly_income-700000)*0.3)
            print("Your taxable amount is",tax_amount)
        else:
            tax_amount=429500+((yearly_income-2000000)*0.36)
            print("Your taxable amount is",tax_amount)
        return tax_amount
        
def calculateUnmarried(yearly_income):
    if(yearly_income<400000):
        tax_amount=yearly_income*0.01
        print("Your taxable amount is",tax_amount)
    elif(yearly_income>=400000 or yearly_income<500000):
            tax_amount=4000+((yearly_income-400000)*0.1)
            print("Your taxable amout is",tax_amount)
    elif(yearly_income>=500000 and yearly_income<700000):
            tax_amount=14000+((yearly_income-500000)*0.2)
            print("Your taxable amount is",tax_amount)
    elif(yearly_income>=700000 and yearly_income<2000000):
        tax_amount=54000+((yearly_income-700000)*0.3)
        print("Your taxable amount is",tax_amount)
    else:
        tax_amount=444000+((yearly_income-2000000)*0.36)
        print("Your taxable amount is",tax_amount)
    return tax_amount

def display(name,address,age,status,income,yearlyIncome,tax):
    print("Employee Details::")
    print("Name::",name,"\t\t\tAddress::",address)
    print("Age::",age,"\t\t\tMarital Status::",status)
    print("\t\t(Note:: m=married and u=unmarried)")
    print("Monthly income::",income,"Yearly income::",yearlyIncome)
    print(tax)

def main():
    staticInformation()
    name,address,age,status,income,yearlyIncome=details()
    if status== 'M':
       tax=calculateMarried(yearlyIncome)
       with open("income_tax.txt",'w') as file2:
           file2.write(f"The Name of the tax payer is:{name}\n")
           file2.write(f"The Address of the tax payer is:{address}\n")
           file2.write(f"The age of tax payer is:{age}\n")
           file2.write("-------------------------------------------\n")
           file2.write(f"The taxable income of your salary is {tax}\n")
           print("The file has been created stating your records!")

    elif status== 'U':
        tax=calculateUnmarried(yearlyIncome)
        with open("income_tax.txt", 'w') as file2:
            file2.write(f"The Name of the tax payer is:{name}\n")
            file2.write(f"The Address of the tax payer is:{address}\n")
            file2.write(f"The age of tax payer is:{age}\n")
            file2.write("-------------------------------------------\n")
            file2.write(f"The taxable income of your salary is {tax}\n")
            print("The file has been created stating your records!")


if __name__=="__main__":
    main()





