import datetime
name = []
address = []
age = []
tax = []

def topDisplay():
    print("\n\tInland Revenue Income System\n\t\tLazimpat,Kathmandu")
    print("==================================================")
    print("  Welcome to the Income Tax Calculation System")
    print("==================================================\n")
    print("\t\t\t\tDate: ", datetime.date.today(), "\n")

def inputs():
    name.append(input(" Enter customer Name:"))
    address.append(input(" Enter customer Address:"))
    age.append(int(input(" Enter customer Age:")))
    print("--------------")
    marriageStatus = input("Are you married or unmarried (y/n)::").lower()
    income = int(input("Enter the monthly income::"))
    return marriageStatus, income

def calculate(marriageStatus, income):
    if (marriageStatus == 'n'):
        tax.append(unmarried(income))
    else:
        tax.append(married(income))

def unmarried(income):
    taxableAmount = 0
    if(income <= 400000):
        taxableAmount = income*0.01
    else:
        if(income > 400000 and income <= 500000):
            temp = income-400000
            taxableAmount = temp*0.1 + 400000*0.01
        elif(income > 500000 and income <= 700000):
            temp = income-500000
            taxableAmount = temp*0.2 + 100000*0.1 + 400000*0.01
        elif(income > 700000 and income <= 2000000):
            temp = income-700000
            taxableAmount = temp*0.3 + 200000*0.2 + 100000*0.1 + 400000*0.01
        elif(income > 2000000):
            temp = income-2000000
            taxableAmount = temp*0.36 + 1300000*0.3 + 200000*0.2 + 100000*0.1 + 400000*0.01
    return taxableAmount

def married(income):
    taxableAmount = 0
    if(income <= 450000):
        taxableAmount = income*0.01
    else:
        if(income > 450000 and income <= 550000):
            temp = income-450000
            taxableAmount = temp*0.1 + 450000*0.01
        elif(income > 550000 and income <= 750000):
            temp = income-550000
            taxableAmount = temp*0.2 + 100000*0.1 + 450000*0.01
        elif(income > 750000 and income <= 2000000):
            temp = income-750000
            taxableAmount = temp*0.3 + 200000*0.2 + 100000*0.1 + 450000*0.01
        elif(income > 2000000):
            temp = income-2000000
            taxableAmount = temp*0.36 + 1250000*0.3 + 200000*0.2 + 100000*0.1 + 450000*0.01
    return taxableAmount

    
def finaldisplay():
    f=open("display.txt","w")
    f.write("\n\n*************************************")
    f.write("\n   Tax Calculation for; ")
    f.write("\n     Customer Name: {}".format(name[0]))
    f.write("     Address: {}".format(address[0]))
    f.write("     Age: {}".format(age[0]))
    f.write("\n     TaxAmount: Rs. {}".format(tax[0]))
    f.write("\n*************************************\n")

def main():
    topDisplay()
    married, income = inputs()
    calculate(married, income)
    finaldisplay()


main()
