# # 1) Remove first n characters from a string. ( use function remove_chars()) 
# name = "Arina ghimire"
# ch = name.replace(name[0]," ")
# print(ch)

# # 2) Area and Circumference of a Circle 
# radius = float(input("enter the radius"))
# area = 3.14*pow(radius,2) # two are same
# # area2 = 3.14 * radius**2
# circumference = 2 * 3.14 * radius
# print(area)
# # print(area2)
# print(circumference)

# 3) Print Ascii Value of the Character
# The ord() method returns ASCII value of a character passed as its argument
# ch = input("enter the character :")
# asc = ord(ch)
# print("\nASCII Value:", asc)

# 4) Area of Triangle 
# length = int(input("enter the length :"))
# breathe = int(input("enter the breathe :"))
# Area = (breathe * length)/2
# print(" the area is :", Area)

# 5) Convert a Person’s Name in Abbreviated

# 6)simple intrest
# p = int(input("enter the number"))
# t = int(input("enter the number"))
# r = int(input("enter the number"))
# intrest = p*t*r/100
# print(intrest)

# 7) factorial
# factorial = 1
# num = int(input("enter the number"))
# if num<0:
#     print("no factorial of negative number")
# elif num==0:
#     print("fatorial is 1")
# else:
#     for i in range(1,num+1):
#        factorial = factorial * i
#     print( f"the factorial of {num} is {factorial}")

# 8) find GCD OR HCF
# import math
# print("The gcd of 60 and 48 is : ", end="")
# print(math.gcd(60, 48))

# import math
# print("The gcd of 60 and 48 is : ", end="")
# print(math.lcm(60, 48))

# converting fahrenheit and celsius 
# Celsius = (Fahrenheit – 32) * 5/9
# Fahrenheit = (Celsius * 9/5) + 32

# 9) The Greatest Number Among the Given Three Number
# num1 = int(input("enter the number"))
# num2 = int(input("enter the number"))
# num3 = int(input("enter the number"))
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3

# print("The largest number is", largest)

# 10) The Number Is Positive or Negative 
# num1 = int(input("enter the number"))
# if num1<0:
#     print("negative")
# else:
#     print("positive")    

 # 11) leap year
# year = int(input("enter the year"))
# if year%400 == 0:
#     print("it is a leap year")
# elif year%4 == 0:
#     print("it is a leap year")
# elif year% 100 == 0:
#     print("it is not a leap year")
# else:
#     print("not leap year")   
 
# 12) max number
# a = 10
# b = 30
# c= 34
# d= (a,b,c)
# print(max(d))

# 13) Check whether the triangle is an equilateral, isosceles or scalene triangle.
# a = int(input("enter the length "))
# b =  a = int(input("enter the length "))
# c = a = int(input("enter the length "))
# if a==b & b== c:
#     print("equilateral triangle")
# elif a == b or b==c or c==a:
#     print("isosceles triagle")
# else:
#     print("scalene triangle")

# 14) Calculate profit or loss. 
# sp = int(input("enter the sp price :"))
# cp = int(input("enter the  cp price :"))
# if sp > cp:
#     profit = sp-cp
#     print("the profit is :", profit)
# elif cp > sp:
#    loss = cp-sp
#    print("the loss is :", loss)
# else:
#     print("no profit and loss")
    
# 15)wap to take random vlaue from the user and check the value is 2 or 3 multiple and if 2 multiple then print zhthe 
# table of its.
# import random 
# a = random.randint(1,10)
# if a % 2==0:
#     print("it is divisible by 2")
#     i = 1
#     for i in range(1,10):
#         print("2 * ",i,"=",(2*i))
# elif a % 3==0:
#          print("is is divisible by 3")
# else:
#          print("it is divisible by both")

# A Character Is an Alphabet or Not
# ch = input("Enter a character: ")
# if((ch>='a' and ch<= 'z') or (ch>='A' and ch<='Z')):
#     print(ch, "is an Alphabet")
# else:
#     print(ch, "is not an Alphabet")


#  Python Program to check whether the given input is alphabet, number or special character 
# ch = input("Please Enter Any Character : ")
# if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
#     print("The Given Character ", ch, "is an Alphabet") 
# elif(ch >= '0' and ch <= '9'):
#     print("The Given Character ", ch, "is a Digit")
# else:
#     print("The Given Character ", ch, "is a Special Character")


# Input week number and print weekday. 
# weekday = int(input("Enter weekday day number (1-7) : "))

# if weekday == 1 :
#     print("\nMonday");

# elif weekday == 2 :
#     print("\nTuesday")
# elif(weekday == 3) :
#     print("\nWednesday")
# elif(weekday == 4) :
#     print("\nThursday")
# elif(weekday == 5) :
#     print("\nFriday")
# elif(weekday == 6) :
#     print("\nSaturday")
# elif (weekday == 7) :
#     print("\nSunday")
# else :
#     print("\nPlease enter weekday number between 1-7.")