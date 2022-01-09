'''
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here: 


>>> 10 ∗ ( 1 / 0 ) 
>>> Traceback ( mostre cent call last ) : 
>>>  Zero Division Error : division by zero
```
'''

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


