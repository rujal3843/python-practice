 # 1) Write a Python program to print all natural numbers from 1 to n. 
# num = int(input("enter the number"))
# for i in range(1,num+1):
#     print(i)
#using while loop
# num = int(input("enter  the number"))
# i = 1
# while i <= num:
#     print(i)
#     i = i+1


# 2) Write a Python program to print all natural numbers in reverse (from n to 1)
# num = int(input("enter the number"))
# i = num
# while i>=1:
#     print(i)
#     i = i-1

# 3) Write a Python program to print all alphabets from a to z. 
# print("Uppercase Alphabets are:")
# for i in range(65,91): 
#         print(chr(i),end=' ') 
# using lower case
   # print("Lowercase Alphabets are:")
# for i in range(97,123): 
#         print(chr(i),end=' ')

# 4) Write a Python program to print all even numbers between 1 to 100. 
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i, end=' ')

# 5) Write a Python program to print all odd number between 1 to 100.
# for i in range(1,101):
#     if i % 2 != 0:
#         print(i, end=' ')

# 6) Write a Python program to find sum of all natural numbers between 1 to n.
# num = int(input("enter the number"))
# sum = 0
# for i in range(1,num+1):
#     sum = sum + i
#     print(sum)
               
# 7) Write a Python program to find sum of all even numbers between 1 to n
# num = int(input("enter the number"))
# sum = 0
# for i in range(1,num+1):
#    if i % 2 == 0:
#        sum = sum + i
#        print(sum)
        
# 8)Write a Python program to find sum of all odd numbers between 1 to n.
# num = int(input("enter the number"))
# sum = 0
# for i in range(1,num+1):
#     if i % 2 != 0:
#         sum = sum + i
#         print(sum)

# 9) Write a Python program to print multiplication table of any number.
# num = int(input("Display multiplication table of : "))
# for i in range(1, 11):
#    # print(num, 'x', i, '=', num*i)  
# OR 
#    print(f"{num} x {i} = {num*i} ")
    
# 10) Write a Python program to count number of digits in a number.
# num = int(input("enter the number :"))
# print(len(str(num)))
#  OR 
# count= 0
# num = int(input("enter the number"))
# while num>0:
#  num = num //10
#  count = count + 1
#  print(count)

# 11) Write a Python program to find sum of first and last digit of a number.
# number = 1247
# number = str(number) # changing integer to string so that we can index 
# first_digit = int(number[0])
# last_digit = int(number[-1])
# addition = first_digit + last_digit
# print('Addition of first and last digit of the number is',  addition)

# 12) Write a Python program to calculate sum of digits of a number.
# Number = int(input("Please Enter any Number: "))
# add = 0

# while(Number > 0):
#     Reminder = Number % 10
#     add = add + Reminder
#     Number = Number //10
#     print(add)

# 13) Write a Python program to enter a number and print its reverse.
# Number = int(input("Please Enter any Number: "))
# Reverse = 0
# while(Number > 0):
#     Reminder = Number %10
#     Reverse = (Reverse *10) + Reminder
#     Number = Number //10
#     print(Reverse)
 
# 14) Write a Python program to check whether a number is palindrome or not.
# num = int (input("Enter the number:"))
# org = num
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
    
# print ("The reverse of ", org, "is ", rev)
# if rev == org:
#     print ("The number ", org, "is Palindrome")
# else:
#     print ("The number ", org, "is not a Palindrome")


# 15) Write a Python program to print all ASCII character with their values
# c = input("enter the character")
# print("The ASCII value of '" + c + "' is", ord(c))

# 16) factorial
# num = 8
# factorial = 1
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

# 17) Program to print Fibonacci numbers
# num = int(input("enter the number :"))
# a = 0
# b= 1
# for i in range(0,num):
#    c = a + b
#    a = b
#    b = c
#    print(c)
