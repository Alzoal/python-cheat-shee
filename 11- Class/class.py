'''
Introduction Python is an object oriented programming (OOP) language. Almost everything in Python is an object, with its properties and methods. The foundation for all object oriented programming (OOP) languages are Classes. 

To create a class, use the keyword class:
'''

'''
class Car :
  model = "Volvo"
  color = "Blue"

car = Car( )

print ( car.model ) #--> Volvo
print ( car.color )   #--> Blue


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
'''


 ###----------------------------------- call the class--------------------------------

'''
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

'''

### ----------------------------------------Inherit -----------------------------------
'''
- animal  , human=> father can call on any child class
- rabbit , fish , hawk => child can a father class with funcation

- 1- inherit
- 2- multi inherit class
- 3- overwriting method

'''
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





###-------------------------------- method chaining = call multi function sequentialy----------------------------------


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


### ------------------------------------------super() ----------------------------------------------------
#funcation used to give access to the method of parent class


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



#-------------------------Inherited class definition -----------------------------------------



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

#---------------------------------------------How to import classes-----------------------------------------
'''
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
'''




