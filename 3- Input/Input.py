
name=input("what is your name : ") # ask for name ==> musab
age=input("what is your age : ")
hight=input("what is your hight : ")

  
print("your name is " + name) #==> musab
print("your age is " + str(age))
print("your Hight is " + str(hight))




#Casting the age for use ==> check the input int or not

age=input("what is your age : ")

loops = 0
if(age.isnumeric()):
	loops = int(age)
	print(loops)
else:
	print("Not an integer!")

