

#String and Formatted String Can Use Quotes and Double Quotes

first = "musab"
last = "ismail" 
print(f'Hello, {first} {last}')
print("Hello, {} {}".format(first , last))
print ("Hello, "+first+" " +last )


#output ==> hello, musab ismail 


#--------------------------------------Escape characters--------------------------------------


print('\'') #Single quote
print('\"') #Double quote
print('\t') #Tab
print('\n') #New Line
print('\\') #Backslash



#--------------------------------------Multiline string with triple quotes--------------------------------------


print('''This
	is
	a
	multiline
	string''')


#--------------------------------------Multiple Variable Assignment--------------------------------------

first, last = "musab", "ismail" 
print(f'hello, {first} {last}')


#String functions

first, last = "musab", "ismail" 
print(f'hello, {first} {last}'.title())
#Hello, Musab Ismail
print(f'hello, {first} {last}'.upper())
#HELLO, MUSAB ISMAIL
print(f'hello, {first} {last}'.lower())
#hello, musab ismail



#--------------------------------------Useful string methods--------------------------------------

v = 'Hello, World'
print(v.upper()) #Return an uppercase version of string
print(v.isupper()) #String is all uppercase letters
print(v.lower()) #Return a lowercase version of string
print(v.islower()) #String is all lowercase letters
print(v.istitle()) #String is words of uppercase letter followed by lowercase letters
print(v.isalpha()) #String is letters only
print(v.isalnum()) #String is letters and numbers only
print(v.isdecimal()) #String is a float
print(v.isspace()) #String is just white space characters
print(v.startswith('W')) #String starts with this substring
print(v.endswith('llo')) #String ends with this substring





