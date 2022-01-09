'''
Python has several functions for creating, reading, updating, and deleting files. The key function for working with files in Python is the open() function. 
The open() function takes two parameters; Filename, and Mode. 
There are four different methods (modes) for opening a file: 
• ”x” - Create - Creates the specified file, returns an error if the file exists 
• ”w” - Write - Opens a file for writing, creates the file if it does not exist 
• ”r” - Read - Default value. Opens a file for reading, error if the file does not exist 
• ”a” - Append - Opens a file for appending, creates the file if it does not exist In addition you can specify if the file should be handled as binary or text mode 
• ”t” - Text - Default value. Text mode 
• ”b” - Binary - Binary mode (e.g. images)
'''
### -----------------Check Input ==> if it file or dir--------------------------------------------


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



###  -------------------------------------- Add Text To File ----------------------------------------------------------


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





### -------------------------------------- copy , move and delete ----------------------------------------------------------
#copy file 3 type  copyfile() = copy content of the file
#copy() = copyfile() + permision and destination
#copy2() =  copy() + metadata  (creation + modifaction file )

  

import shutil
# -------------------------------------- copy ---------------------------------------------------------- 

shutil.copyfile("x.txt", "text.txt")
shutil.copyfile("x.txt", "C:\\Users\\ZeroDay\\Desktop\\text.txt")


#-------------------------------------- move ----------------------------------------------------------

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


#-------------------------------------- delete ----------------------------------------------------------

os.remove(path/"file.txt")
os.rmdir(path)




### -------------------------------------- Open file and read line by line ----------------------------------------------------------


m= open("musab1.txt" , "r")
line = m.readline()
cnt = 1

while line:
 print(line.strip())

 line = m.readline()
 cnt += 1


#-------------------------------------- Defining a file path thats windows, mac or linux agnostic -------------------------------
 
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

#---------------------------------------Reading and writing to files with open function---------------------------------------------

nf = Path.cwd() / Path('numbers.txt')
inf = Path.cwd() / Path('inverse-numbers.txt')

#---------------------------------------Reading a file---------------------------------------

with open(nf) as file:
	contents = file.read()
	print(contents.rstrip())

#---------------------------------------#Reading line by line---------------------------------------

with open(nf) as file:
	for line in file:
		print(line.rstrip())

#---------------------------------------Buffering into a list---------------------------------------

with open(nf) as file:
	lines = file.readlines()
	for line in lines:
		print(line.rstrip())

#---------------------------------------Writing to an empty file---------------------------------------

with open(inf, 'w') as file:
	i = 10
	while i >= 1:
		file.write(f'{i}\n')
		i -= 1

with open(inf) as file:
	print(file.read())

#---------------------------------------Appending ---------------------------------------

with open(inf, 'w') as file:
	file.write('0')

with open(inf) as file:
	print(file.read())

#---------------------------------------Save python variables with shelve---------------------------------------

import shelve
sf = shelve.open('data')
cats = ['Zen', 'Jack']
sf['cats'] = cats
sf.close()

sf = shelve.open('data')
new_cats = sf['cats']
sf.close()
print(new_cats)

#---------------------------------------Creating dynamic python scripts and importing them ---------------------------------------

import pprint
cats = [{'name': 'Zen'}]
with open('dynamicCats.py', 'w') as file:
	file.write('cats = ' + pprint.pformat(cats) + "\n")

import dynamicCats
print(dynamicCats.cats[0]['name'])



