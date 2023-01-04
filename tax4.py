
#Income tax Calculator using function

def fmt():
  print("\t\t\t\t____________________________________________________________________________________________\n")
  print("\t\t\t\t\t\t\t\tIncome Tax Calculation System\n")
  print("\t\t\t\t\t\t\t\t    Lazimpat, kathmandu")
  print("\t\t\t\t____________________________________________________________________________________________\n")
  print("\t\t\t\t\t\t\tWelcome to the Income Tax Calculation System")
  print("\t\t\t\t_____________________________________________________________________________________________")

def ask_user():
  name = input("\n\nName: ")
  address = input("Address: ")
  age = input("Age: ")
  print("__________________________")
  m_income = int(input("Enter your monthly income: "))
  m_sta = input("Are you married or unmarried? Please type 'Y' or 'N': ") #type 'Y' or 'N' 
  a_income = m_income*12
  return m_sta, a_income

#function for single
def Calculate_Single(y):
    if y<=400000:
        tax = 1/100*y
        total = y-tax
    elif y>400000 and y<=500000:
        tax1 = 4000 #tax for upto 400000
        additional = y - 400000 #extra amount greater than 400000 and less than or equal to 500000
        tax2 = 10/100*additional #tax for that extra amount that is greater than 400000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 400000 and that extra amount
    elif y>500000 and y<=700000:
        tax1 = 14000 #tax for upto 500000
        additional = y - 500000 #extra amount greater than 500000 and less than or equal to 700000
        tax2 = 20/100*additional #tax for that extra amount that is greater than 500000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 500000 and that extra amount
    elif y>700000 and y<=2000000:
        tax1 = 54000 #tax for upto 700000
        additional = y - 700000 #extra amount greater than 700000 and less than or equal to 2000000
        tax2 = 30/100*additional #tax for that extra amount that is greater than 700000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 700000 and that extra amount
    elif y>2000000:
        tax1 = 444000 #tax for upto 2000000
        additional = y - 2000000 #extra amount greater than 2000000
        tax2 = 36/100*additional #tax for that extra amount that is greater than 2000000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 2000000 and that extra amount 
    return tax, total 

#function for married
def Calculate_Married(y):
    if y<=450000:
       tax = int(1/100*y)
       total = int(y-tax)
    elif y>450000 and y<=550000:
       tax1 = 4500 #tax for upto 450000
       additional = y - 450000 #extra amount greater than 450000 and less than or equal to 550000
       tax2 = 10/100*additional #tax for that extra amount that is greater than 450000
       tax = int(tax1 + tax2) #total tax 
       total = int(y-tax) #salary after deducting tax on both 450000 and that extra amount
    elif y>550000 and y<=750000:
        tax1 = 14500 #tax for upto 550000
        additional = y - 550000 #extra amount greater than 550000 and less than or equal to 750000
        tax2 = 20/100*additional #tax for that extra amount that is greater than 550000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 550000 and that extra amount
    elif y>750000 and y<=2000000:
        tax1 = 54500 #tax for upto 750000
        additional = y - 750000 #extra amount greater than 750000 and less than or equal to 2000000
        tax2 = 30/100*additional #tax for that extra amount that is greater than 750000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 750000 and that extra amount
    elif y>2000000:
        tax1 = 429500 #tax for upto 2000000
        additional = y - 2000000 #extra amount greater than 2000000
        tax2 = 36/100*additional #tax for that extra amount that is greater than 2000000
        tax = int(tax1 + tax2) #total tax 
        total = int(y-tax) #salary after deducting tax on both 2000000 and that extra amount
    return tax, total

#function for display
def display(tax1, total):
    fmt()
    print("\nYour total payable tax is {}.\nYour total salary after deducting tax is {}.".format (tax1, total))

#function to write in file
def infile():
    file = open('abc.txt','w')
    file.write(str())
    print("Success!")

infile()
#main function definition
def main():
    fmt()
    x, y = ask_user()
    #for individual
    if x=='N' or x=='n':
        a, b = Calculate_Single(y) #function call
    #for couple
    elif x=='Y' or x=='y':
        a, b = Calculate_Married(y) #function call
    else:
        print("Please enter a valid character!!!")
    display(a, b)

#main function call
main()