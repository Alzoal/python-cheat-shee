# python cheat sheet
### Introduction to Python

Python is an open source and cross-platform programming language, that has become increasingly popular over the last ten years. It was first released in 1991.

Python is a multi-purpose programming languages (due to its many extensions), examples are scientific computing and calculations, simulations, web development (using, e.g., the Django Web framework), etc

Python is an object-oriented programming language (OOP), but you can use Python in basic application without the need to know about or use the objectoriented features in Python.

Python is an interpreted programming language, this means that as a developer With interpreted languages, the code is saved in the same format that you entered. Compiled programs generally run faster than interpreted ones because interpreted programs must be reduced to machine instructions at run-time. It is usually easier to develop applications in an interpreted environment because you don’t have to recompile your application each time you want to test a small section.




## First Python Program

`print ("Hello World")`


## Variable And Opration

`# This is a comment if you didn't already know. It is not interpreted.`
```
''' This is a 
multiline comment ''' 
```

Nothingness assigned to a variable
```
nothing = None
if nothing == None:
	print('The void')
```

Integers
```
print(2 + 3)
#5
print(2 * 3)
#6
print(3 - 2)
#1
print(4 / 2)
#2
print(3 ** 2)
#Exponent: 9
```

Order of Operations supported
```
print(2 + 3 * 4)
#14
print((2 + 3) * 4)
#20
```

Combining Floats and Integers always results in a Float
> print(1 + 2.0)
#3.0

Underscores used as commas in large numbers
> print(14_000_000)
#14000000

Constants not supported. Just use all caps
>MAX_CONNECTIONS = 2

Type conversaion
> print('I am ' + str(29) + ' years old.')
#I am 29 years old
print( 40 + int('9'))
#49
print(100.0 - float(10))
#90.0

Modifying a global variable from within a function
```
def spam():
	global eggs
	eggs = 'spam'

eggs = 'global'
print(eggs)
spam()
print(eggs)
```

## String 

String and Formatted String
Can Use Quotes and Double Quotes
```
first = "musab"
last = "ismail" 
print(f'Hello, {first} {last}')
print("Hello, {} {}".format(first , last))
print ("Hello, "+first+" " +last )


output ==> hello, musab ismail 

```

Escape characters
```

print('\'') #Single quote
print('\"') #Double quote
print('\t') #Tab
print('\n') #New Line
print('\\') #Backslash

```

Multiline string with triple quotes
```

print('''This
	is
	a
	multiline
	string''')
```

Multiple Variable Assignment
```
first, last = "musab", "ismail" 
print(f'hello, {first} {last}')
```

String functions
```
first, last = "musab", "ismail" 
print(f'hello, {first} {last}'.title())
#Hello, Musab Ismail
print(f'hello, {first} {last}'.upper())
#HELLO, MUSAB ISMAIL
print(f'hello, {first} {last}'.lower())
#hello, musab ismail
```


Useful string methods
```
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

```


## Input

```
name=input("what is your name : ") # ask for name ==> musab
age=input("what is your age : ")
hight=input("what is your hight : ")

  
print("your name is " + name) #==> musab
print("your age is " + str(age))
print("your Hight is " + str(hight))

```


Casting the age for use==> check the input int or not
```
age=input("what is your age : ")

loops = 0
if(age.isnumeric()):
	loops = int(age)
	print(loops)
else:
	print("Not an integer!")

```


## Loops

### For Loops 
A For loop is used for iterating over a sequence. I guess all your programs will use one or more For loops. So if you have not used For loops before, make sure to learn it now. Below you see a basic example how you can use a For loop in Python:

- limited execute code

  
> for x in range(1,10) :
    print ( x ) #=>1-9


The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. You can also use the range() function like this:

```
start = 1
stop = 13
step = 2
for x in range(start , stop , step) :
  print ( x ) #==> 1,3,5,7,9,11
```

Example 
```
for i in range(1,10):
 print(i+1)
```
```
for i in range(50,100+2,1):
 print(i)
```
```
for i in "musab ismail" :
 print(i)
```
```
for i in name :
 print(i)
```

```
import time
for i in range(10,1,-1):
 print(i)
 time.sleep(1)

print("happy new years")
```


### Nested For Loops 
In Python and other programming languages you can use one loop inside another loop.

```
for i in range ( 1 , 10 ) :
   for k in range ( 1 , 10 ) :
       print ( i , k )

output ==> 1-1 -> 1-9 ,2-1 ->2-9 -->>>> 9-9
```

```
raw = int(input("how many raw :? ")) #->3
columns = int(input("how many columns :? ")) #-> 5
symbol= input("Enter the  symbol :? ")#-> *

  
for i in range(raw) :
 for j in range (columns) :
   print(symbol , end="")
 print()

 output:
*****
*****
*****
```


### While Loops 
The while loop repeats a group of statements an indefinite number of times under control of a logical condition.
- unlimited execute code

```
m = 8

while m > 2:
  print (m)
  m=m-1

output= > 8 , 7 -->3
```


### loop control ==> break - continus - pass

Break
```
while True :

 name = input("inter your name :")
 if name != "":
   break
```

Continue
```
number="912-121-2213-7"

for i in number:
 if i =="-":
   continue
 else:
   print(i , end="")
```

Pass
```
for i in range(1,20):
 if i == 13 :
   pass
 else :
   print(i , end="")
```


## If-statements

```
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
```

Other Comparators
```
# !=
# <
# <=
# >
# >=
```

And - Or 
```
#And Or
ages = (22, 24)
if ages[0] >= 22 and ages[1] <= 24:
	print(True)
#True
ages = (22, 24)
if ages[0] == 22 or ages[0] == 23:
	print(True)
#True
```

```
#Is a value in a list
toppings = ['mushrooms', 'sausage', 'pepperoni']
print('mushrooms' in toppings)
#True

#Not in a list
print('mushrooms' not in toppings)
#False

#List is not empty
if toppings:
	print(True)
#True

#List is empty
if not toppings:
	print(True)
else:
	print(False)

#Checking for a boolean
flag = False
if flag:
	print(flag)
elif not flag:
	print(flag)
#False

#Else If
age = 16
if age < 12:
	price = 25
elif age < 18:
	price = 50
else:
	price = 75
print(price)
#50
```

```
temp = int(input("What the temp now : "))

if temp >= 0 and temp < 30 :
 print("go outside")

elif temp >33 or temp < 55 :
 print("dont go outside")

elif not(temp >33 or temp < 55) :
 print("stay home")
 
else :
 print("stay home")
```


## List 

```
#Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#['trek', 'cannondale', 'redline', 'specialized']

#List Access
#First
print(bicycles[0])
#trek
#Last
print(bicycles[-1])
#specialized

#Modification
bicycles[0] = 'training'
print(bicycles[0])
#training

#Adding
bicycles.append('mountain')
print(bicycles[-1])
#mountain

#Inserts value at 0 and shifts all elements to the right
bicycles.insert(0, 'toddler')
print(bicycles[0])
#toddler

#Removal of list items
del bicycles[0]
print(bicycles)
# ['training', 'cannondale', 'redline', 'specialized', 'mountain']

#Popping from tail
bicycles.pop()
print(bicycles)
# ['training', 'cannondale', 'redline', 'specialized']

#Popping from inside list; all elements to right shift to left
bicycles.pop(1)
print(bicycles)
# ['training', 'redline', 'specialized']

#Remove by value
bicycles.remove('training')
print(bicycles)
#['redline', 'specialized']

#Sort the list
bicycles.sort(reverse = True)
print(bicycles)
#['specialized', 'redline']

#Returns a sorted list without sorting the list itself
print(sorted(bicycles))
print(bicycles)
#['redline', 'specialized']
#['specialized', 'redline']

#Reverse index order
bicycles.reverse()
print(bicycles)
#['redline', 'specialized']

#List length
print(len(bicycles))
#2
```
#Multiple assignment of list values to variables
```
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

#Enumerating a list
for index, item in enumerate(cat):
	print(index)
	print(item)
```
#Get a random value
```
import random
print(random.choice(cat))

#Randomly sort the list
random.shuffle(cat)
print(cat)

#Convert back and forth to immutable tuple
t = tuple(cat)
print(t)
l = list(t)
print(l)
```
#Copy vs Deep Copy - Deep copy does inner lists. These methods create a new reference, so they can be changed
#independently of each other
```
c = [['fat', 'loud'], 1, 2]
import copy
c2 = copy.copy(c)
c2.append(3)
print(c)
print(c2)
```

### List-Loops

```
# Loop, loop, loop
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(magician)

# alice
# david
# carolina

# Using variables in a loop
for magician in magicians:
	print(f"{magician.title()} is a magician")

# Alice is a magician
# David is a magician
# Carolina is a magician

# Using tabs to control flow
for magician in magicians:
	print(f"{magician.title()} is a magician")
	print(f"{magician.title()} is in the list")

print(f"{magician.title()} is the last in the list")

#Alice is a magician
#Alice is in the list
#David is a magician
#David is in the list
#Carolina is a magician
#Carolina is in the list
#Carolina is the last in the list
```
#Generating a range of numbers to loop through
```
for value in range(1,5):
	print(value)
```
#Storing the range in a list
```
numbers = list(range(1,5))
for value in numbers:
	print(value)

#1
#2
#3
#4
```
Even numbers using step size
```
numbers = list(range(2,11,2))
for value in numbers:
	print(value)

#2
#4
#6
#8
#10
```
Odd numbers using step size
```
numbers = list(range(1,10,2))
for value in numbers:
	print(value)

#1
#3
#5
#7
#9
```
Statistics with a set of numbers
```
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
#0
print(max(digits))
#9
print(sum(digits))
#45
```
List Comphrensions
```
#1-10 raised to the power of 2 and added to the list
squares = [value**2 for value in range(1,11)]
print(squares)

#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
#Slicing ou a subset of a list. Start at position 1 and end before position 4
```
players = ['a', 'b', 'c', 'd', 'e']
print(players[1:4])
#['b', 'c', 'd']

#Slicing : 0:3 is identical to :3
print(players[0:3])
print(players[:3])
#['a', 'b', 'c']
#['a', 'b', 'c']

#Slicing: 2:5 is identical to 2:
print(players[2:5])
print(players[2:])
#['c', 'd', 'e']
#['c', 'd', 'e']

#Inverse: Start from end of list. Last two players
print(players[-2:])
#['d', 'e']
```
 Copying a list
 ```
food = ['pizza', 'falafel', 'carrot cake']
friends_food = food[:]
print(food)
print(friends_food)
#['pizza', 'falafel', 'carrot cake']
#['pizza', 'falafel', 'carrot cake']
food.append('ice cream')
friends_food.append('milkshake')
print(food)
print(friends_food)
#['pizza', 'falafel', 'carrot cake', 'ice cream']
#['pizza', 'falafel', 'carrot cake', 'milkshake']

# Tuples: Identical to lists except immutable and use () instead of []
dimensons = (400, 200)
print(dimensons[0])
print(dimensons[1])
```

### 2D list => list of list


```
subject =["music" , "footbool" , "study"]
drink = ["pipse" , "cocacola" , "fanta"]
path = ["12 str" , "33 str" , "90 str"]


all = [subject , drink , path]
  
print(all[0][2]) # study
print(all[1][1]) # cocacola
print(all[2][2]) # fanta


if "footbool" in subject :
 print("found")


```

## Dictionaries

```
#Key Value Pair
#Can mix variable types
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

#Adding new keys
alien['x-position'] = 0
alien['y-position'] = 25
alien['armor'] = 100
print(alien)

#Empty dictionary
alien_new = {}

#Modifiying a key
alien['color'] = 'yellow'

print(alien)

#Deleting a key
del alien['points']
print(alien)

#Formatting
alien_new = {
	'color': 'green',
	'points': 10
}
print(alien_new)

#Pretty printing
import pprint
pprint.pprint(alien_new)

#Using a default value if key not found
point_value = alien.get('points', 5)
print(point_value)

alien.setdefault('points', 5)
print(alien.get('points'))

#Looping
for key,value in alien_new.items():
	print(f"Key: {key} Value: {value}")

#Key Looping
for key in alien_new.keys():
	print(f"Key: {key}")

#Sorting the keys
sorted_alien = sorted(alien)
print(alien)
print(sorted_alien)

#Value looping
for value in alien_new.values():
	print(f"Value: {value}")

#Nesting
nested_alien = {
	'points': 10,
	'color': 'green',
	'coordinates': {
		'x': 0,
		'y': 25
	},
	'attributes': [
		'small',
		'fast'
	]
}
print(nested_alien)
for attribute in nested_alien['attributes']:
	print(attribute)
print(nested_alien['coordinates']['x'])
print(nested_alien['coordinates']['y'])

#List of aliens
#Make 10 aliens
aliens = []
for i in range(10):
	aliens.append({'color': 'green', 'points': 25, 'id': i})
#Print first five
for alien in aliens[:5]:
	print(alien)
#Count the aliens
print(len(aliens))

```

```
capital = {"SD" : "sudan", "KSA" : "sudi arabia" , "IN" : "indian"}

capital.update({"germany" : "berlin"})

print(capital.keys())
print(capital.get("sd"))
print(capital.values())
print(capital.items())


for key,value in capital.items() :
 print(key , value)

```
##  Exception

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here: 

```
>>> 10 ∗ ( 1 / 0 ) 
>>> Traceback ( mostre cent call last ) : 
>>>  Zero Division Error : division by zero
```

```
try :

 a = 3
 b = 0
 r= a/b

except ZeroDivisionError as e:
 print(e)
 print("you can not division by zero")

except ValueError as e:
 print(e)
 print("thire value error here")

except Exception as e :
 print(e)
 print("something is wrong here")

except SyntaxError as e :
 print(e)
 print("there syntaxt Error here")

  
  print(r)
```

## File 

Python has several functions for creating, reading, updating, and deleting files. The key function for working with files in Python is the open() function. 
The open() function takes two parameters; Filename, and Mode. 
There are four different methods (modes) for opening a file: 
• ”x” - Create - Creates the specified file, returns an error if the file exists 
• ”w” - Write - Opens a file for writing, creates the file if it does not exist 
• ”r” - Read - Default value. Opens a file for reading, error if the file does not exist 
• ”a” - Append - Opens a file for appending, creates the file if it does not exist In addition you can specify if the file should be handled as binary or text mode 
• ”t” - Text - Default value. Text mode 
• ”b” - Binary - Binary mode (e.g. images)

### Check Input ==> if it file or dir

```
import os
path = "C:\\Users\\ZeroDay\\Desktop\\test.txt"

if os.path.exists(path):
 print("loaction existe")
 
 if os.path.isfile(path):
 print("file is existe")

 elif os.path.isdir(path):
 print("dir is existe")

else:
 print( "the location does not existe")

```

###  Add Text To File

```
text = "hello \n my name is musa \n my age is 22 \n i live on sudan"

try :
 with open('x.txt',"r") as file :    # r
 print(file.read())
 file.close()

 with open('x.txt', "w") as file :   #"w"
 file.write(text)
 file.close()

 with open('x.txt', "a") as file :   #"a"
 file.write(text)
 file.close()

except FileNotFoundError as e:
 print(e)

```



### copy , move and delete
#copy file 3 type  copyfile() = copy content of the file
#copy() = copyfile() + permision and destination
#copy2() =  copy() + metadata  (creation + modifaction file )

  
```
import shutil
# copy 

shutil.copyfile("x.txt", "text.txt")
shutil.copyfile("x.txt", "C:\\Users\\ZeroDay\\Desktop\\text.txt")


#move file

source = "musab1.txt"
des = "C:\\Users\\ZeroDay\\Desktop\\musabs.txt"

try:

 if os.path.exists(des):
 print("file is exists")
 else:
 os.replace(source ,des)
 print(soures + "was moved")

  

except FileNotFoundError as e:
 print(e)


#remove

os.remove(path/"file.txt")
os.rmdir(path)

```


### Open file and read line by line


```
m= open("musab1.txt" , "r")
line = m.readline()
cnt = 1

while line:
 print(line.strip())

 line = m.readline()
 cnt += 1
 ```

 ```
 #Defining a file path thats windows, mac or linux agnostic
 
from pathlib import Path
#Folder path
p = Path('spam/bacon/eggs')
#spam\bacon\eggs
print(p)
#spam\bacon\eggs
print(str(p))

#File path
p2 = Path('C:/files', 'text.txt')
#files\text.txt
print(p2)

#spam\bacon\eggs\files\text.txt
print(p / p2)

#Current directory
print(Path.cwd())

#Home directory
print(Path.home())

#Make a directory
p3 = Path.cwd() / Path('test')
#p3.mkdir()

#Parts of a file
#files
print(p2.parent)
#text.txt
print(p2.name)
#text
print(p2.stem)
#.txt
print(p2.suffix)
#C:
print(p.drive)

#C:\Users
print(Path.home().parents[0])
#C:\
print(Path.home().parents[1])

#Check if absolute path
print(Path.cwd().is_absolute())
#True
print(Path('spam', 'bacon', 'eggs').is_absolute())
#False

import os
#Get size of home folder in bytes
print(os.path.getsize(Path.home()))
#Get list of files in directoy
print(os.listdir(Path.home()))

#Does it even exist?
print(Path.cwd().exists()) #True
#Is it a file?
print(Path.cwd().is_file()) #False
#Is it a dir?
print(Path.cwd().is_dir()) #True

#Get multiple files in a directory based on a filter.
print(list(Path.cwd().glob('*.txt')))

#Read txt using path
#6
print(Path('spam.txt').write_text('Hello!'))
#Hello!
print(Path('spam.txt').read_text())
```
#Reading and writing to files with open function
```
nf = Path.cwd() / Path('numbers.txt')
inf = Path.cwd() / Path('inverse-numbers.txt')
```
#Reading a file
```
with open(nf) as file:
	contents = file.read()
	print(contents.rstrip())
```
#Reading line by line
```
with open(nf) as file:
	for line in file:
		print(line.rstrip())
```
#Buffering into a list
```
with open(nf) as file:
	lines = file.readlines()
	for line in lines:
		print(line.rstrip())
```
#Writing to an empty file
```
with open(inf, 'w') as file:
	i = 10
	while i >= 1:
		file.write(f'{i}\n')
		i -= 1

with open(inf) as file:
	print(file.read())
```
#Appending 
```
with open(inf, 'w') as file:
	file.write('0')

with open(inf) as file:
	print(file.read())
```
#Save python variables with shelve
```
import shelve
sf = shelve.open('data')
cats = ['Zen', 'Jack']
sf['cats'] = cats
sf.close()

sf = shelve.open('data')
new_cats = sf['cats']
sf.close()
print(new_cats)
```
#Creating dynamic python scripts and importing them
```
import pprint
cats = [{'name': 'Zen'}]
with open('dynamicCats.py', 'w') as file:
	file.write('cats = ' + pprint.pformat(cats) + "\n")

import dynamicCats
print(dynamicCats.cats[0]['name'])

 ```


## Functions

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


```
#Simple function with doc string
def greet_user():
	"""Greet me"""
	print("Hello!")

greet_user()
```

#### Simple function with parameter
```
def greet_user(name):
	print(f"Hello, {name}!")

greet_user('musab')

####  Keyword arguments

greet_user(name='ismail')
```

Simple function with two parameters, one with a default value
```
def greet_user(name, user_type='musab'):
	print(f"Hello, {name}! You are an {user_type}.")

greet_user('Sam')

#Returning a value
def format_name(name):
	return name.title()

name = format_name('Sam the man')
print(name)
```
#### The contents of lists and dictionaries can be modfied via the reference passed
```
def modify_person(person):
	person['last-name'] = 'Gates'

person = {'first-name': 'Bill', 'last-name': 'Watterson'}
print(person)
modify_person(person)
print(person)

#Arbitary number of arguments. Arguments are stored in a tuple
def print_arguments(*arguments):
	print(arguments)

print_arguments('1', '2', '3')

#Arbitary keyword arguments can be assembled into a dictionary
def build_person(**attributes):
	print(attributes)

build_person(first_name='Adam', last_name='Long')

import modules

#Functions can be used from modules
modules.make_pizza(16, 'cheese', 'pepperoni')

from modules import make_pizza

#They can be referenced via their namespace or directly if specifically imported. 
make_pizza(16, 'cheese', 'sausage')

import modules as m
from modules import make_pizza as mp

#Modules and functions from modules can be assigned an alias
m.make_pizza(16, 'cheese', 'meatballs')
mp(16, 'cheese', 'olives')

from modules import *

#All functions can be imported from a module into the script's namespace
make_pizza(16, 'cheese', 'sausage', 'pepperoni')

#Call Stack Example
def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')
	print('d() returns')

a()

#End program early
import sys
sys.exit()
```


  
```
def name (name):
 print("your name is  " + name)

name("musab ismail")

### retuurn => return value that can store on varible
```
```
def multi (x , y):
 m = x * y
 return m

c = multi(4,3)
print(c)
```
### keyword argument
```
def hello (first , middel , last):
 print("hello " + first +" "+ middel +" "+ last)
 
hello(first="musab", last="ismail" , middel="ibrahim")

```

## Creating Classes in Python 

Introduction Python is an object oriented programming (OOP) language. Almost everything in Python is an object, with its properties and methods. The foundation for all object oriented programming (OOP) languages are Classes. 

To create a class, use the keyword class:
```
class Car :
  model = "Volvo"
  color = "Blue"

car = Car( )

print ( car.model ) #--> Volvo
print ( car.color )   #--> Blue

```

```
class Car:

 #class virable

 wheels = 4

 def __init__(self,make,model,color,year):
 self.make = make
 self.model= model
 self.year = year
 self.color = color

 def drinin(self):
 print("this "+self.model+" is driving")
 
 def stop(self):
 print("this "+self.model+" is stopped")
```


 ### call the class

```
from cars import Car

car1 = Car("2dfd" , "BMW" , 2012 , "blue")
car2 = Car("3cc3" , "ford" , 2020 , "red")

print(car1.make)
print(car1.model)
print(car1.color)
print(car1.year)


car1.wheels = 55 #change value of varible from 4

car1.drinin()
car1.stop()
print(car1.wheels) # call it 55
print(car2.wheels) # 4

```

### Inherit 

- animal  , human=> father can call on any child class
- rabbit , fish , hawk => child can a father class with funcation

- 1- inherit
- 2- multi inherit class
- 3- overwriting method

```
class Animal:

 Alive = True

 def eat(self):
 print("this animal is eating")

 def sleep(self):
 print("this animal is sleeping ")

class Human:

 def food(self):
 print("this human can eat this anaimal")
 
 class Rabbit(Animal , Human): # multi inheriting of class

 def run(self):
 print("this rabbit is running")



class Fish (Animal):

 def swim(self):
 print("this fish is swimming")



class Hawk (Animal):
 def fly(self):
 print("this hawk is flying")

 def eat(self):
 print("this hawk is eating now") # overwriting method

  

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

  

print(rabbit.food()) #call food from human class
print(hawk.eat()) #this hawk is eating now #


print(rabbit.run())
print(fish.swim())
print(hawk.fly())




```
### method chaining = call multi function sequentialy

```  
class Car:

 def turn_on(self):
 print("you start the engin")
 return self


 def driving(self):
 print("you are  drining now")
 return self

 def brake(self):
 print("you are stoping the car now")
 return self

 def turn_off(self):
 print("you stop the engin")
 return self

 #car = Car()

 #moves.turn_on().driving().brake().turn_off()
```

### super() 
funcation used to give access to the method of parent class

 ``` 
class Ractangle :

 def __init__(self,length,width):
 self.length = length
 self.width = width

class Square(Ractangle):
 def __init__(self,length,width):
 super().__init__(length, width)

 
 def area (self):
 return self.length*self.width

  

class Cube(Ractangle):
 def __init__(self,length,width,hight):
 super().__init__(length, width)
 self.hight = hight

 def volum(self):
 return self.length*self.width*self.length


square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volum())

```

```
Inherited class definition


class Animal:
	def __init__(self, name):
		self.name=name

	#Overriden by the method in the child class
	def get_long_name(self):
		return f"{self.name} the Animal"

#Class definition
class Dog(Animal):
	"""Simple model of a dog"""

	#Constructor
	#self argument is automatically passed by method call for every class method
	#class properties are attributes and can be added to self at will
	def __init__(self, name, age):
		#Initializing the parent class
		super().__init__(name)
		#Assigning values to attributes
		self.age=age
		#Default value
		self.breed = 'mixed'

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")

	def get_long_name(self):
		return f"{self.name} the Dog"

	def set_name(self, name):
		self.name=name

#Creating an instance and accessing attributes
dog = Dog('Jack', 6)
print(f"{dog.name} is {dog.age} years old.")

#Modifying attributes
dog.age=12
print(f"{dog.name} is {dog.age} years old.")

#Calling methods
dog.sit()
dog.roll_over()

#Using a getter and setter
dog.set_name('Clover')
print(dog.get_long_name())
```
How to import classes
```
#Whole module
import classes
#Single class to namespace
from classes import Dog
#Multiple classes to namespace
from classes import Animal, Dog
#All classes directly to namespace
from classes import *
#Alias
from classes import Dog as d
```






