### For Loops 
'''A For loop is used for iterating over a sequence. I guess all your programs will use one or more For loops. So if you have not used For loops before, make sure to learn it now. Below you see a basic example how you can use a For loop in Python:

- limited execute code
'''
  
for x in range(1,10) :
   print ( x ) #=>1-9


'''The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. You can also use the range() function like this:
'''

start = 1
stop = 13
step = 2
for x in range(start , stop , step) :
  print ( x ) #==> 1,3,5,7,9,11


#--------------------------------------Example --------------------------------------

for i in range(1,10):
 print(i+1)

#--------------------------------------Example --------------------------------------
for i in range(50,100+2,1):
 print(i)
#--------------------------------------Example --------------------------------------

for i in "musab ismail" :
 print(i)
#--------------------------------------Example --------------------------------------
name = "musab ismail"
for i in name :
 print(i)
#--------------------------------------Example --------------------------------------

import time
for i in range(10,1,-1):
 print(i)
 time.sleep(1)

print("happy new years")



### --------------------------------------Nested For Loops-------------------------------------- 
#In Python and other programming languages you can use one loop inside another loop.


for i in range ( 1 , 10 ) :
   for k in range ( 1 , 10 ) :
       print ( i , k )

#output ==> 1-1 -> 1-9 ,2-1 ->2-9 -->>>> 9-9



raw = int(input("how many raw :? ")) #->3
columns = int(input("how many columns :? ")) #-> 5
symbol= input("Enter the  symbol :? ")#-> *

  
for i in range(raw) :
 for j in range (columns) :
   print(symbol , end="")
 print()

 '''output:
*****
*****
*****
'''


###-------------------------------------- While Loops --------------------------------------
'''The while loop repeats a group of statements an indefinite number of times under control of a logical condition.
- unlimited execute code
'''

m = 8

while m > 2:
  print (m)
  m=m-1

#output= > 8 , 7 -->3



### --------------------------------------loop control ==> break - continus - pass--------------------------------------

#Break

while True :

 name = input("inter your name :")
 if name != "":
   break


#Continue

number="912-121-2213-7"

for i in number:
 if i =="-":
   continue
 else:
   print(i , end="")


#Pass

for i in range(1,20):
 if i == 13 :
   pass
 else :
   print(i , end="")


