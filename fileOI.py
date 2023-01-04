# use open function to read the content of a file 
# f = open('myfile.txt', 'r')
# f = open('myfile.txt') # by default the mode is r
# # data = f.read()
# data = f.read(5) # read first 5 character from the file 
# print(data)
# f.close()

f = open('another.txt','r') # by default the mode is r

#read first line
# data = f.readline()
# data = f.readline()
# data = f.readline()
# print(data)
# print(data)
# print(data)
# #read second line
# data = f.readline()
# print(data)
# f.close()

# writ2 file
# f = open('another.txt', 'w')
# f.write("please  write to this file")
# f.close()

# with statement
# with open('another.txt','r') as f:
#     a = f.read()
# with open('another.txt','w') as f:
#     a = f.write("me")
#     print(a)