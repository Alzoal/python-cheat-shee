'''
Introduction A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. 

Previously we have been using many of the built-in functions in Python If you are familiar with one or more other programming language, creating and using functions should be familiar and known to you. 

All programming languages has the possibility to create functions, but the syntax is slightly different from one language to another. Some programming languages uses the term Method instead of a Function.

Functions and Methods behave in the same manner, but you could say that Methods are functions that belongs to a Class.

**Scripts vs. Functions**

It is important to know the difference between a Script and a Function. 

**Scripts:**
• A collection of commands that you would execute in the Editor 
• Used for automating repetitive tasks 
**Functions:**
• Operate on information (inputs) fed into them and return outputs 
• Have a separate workspace and internal variables that is only valid inside the function
• Your own user-defined functions work the same way as the built-in functions you use all the time, such as plot(), rand(), mean(), std(), etc.


'''


#---------------------------Simple function with doc string---------------------------
def greet_user():
	"""Greet me"""
	print("Hello!")

greet_user()


#### ---------------------------Simple function with parameter---------------------------

def greet_user(name):
	print(f"Hello, {name}!")

greet_user('musab')

#### Keyword arguments 

greet_user(name='ismail')


#---------------------------Simple function with two parameters, one with a default value---------------------------

def greet_user(name, user_type='musab'):
	print(f"Hello, {name}! You are an {user_type}.")

greet_user('Sam')

#Returning a value
def format_name(name):
	return name.title()

name = format_name('Sam the man')
print(name)

#### ---------------------------The contents of lists and dictionaries can be modfied via the reference passed---------------------------

def modify_person(person):
	person['last-name'] = 'Gates'

person = {'first-name': 'Bill', 'last-name': 'Watterson'}
print(person)
modify_person(person)
print(person)

#---------------------------Arbitary number of arguments. Arguments are stored in a tuple---------------------------
def print_arguments(*arguments):
	print(arguments)

print_arguments('1', '2', '3')


def name (name):
 print("your name is  " + name)

name("musab ismail")

### --------------------------- retuurn => return value that can store on varible---------------------------

def multi (x , y):
 m = x * y
 return m

c = multi(4,3)
print(c)

###--------------------------- keyword argument---------------------------

def hello (first , middel , last):
 print("hello " + first +" "+ middel +" "+ last)
 
hello(first="musab", last="ismail" , middel="ibrahim")




