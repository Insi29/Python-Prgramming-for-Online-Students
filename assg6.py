'''Question1 
OOP is basically data structuring  it helps in structuring your code, manipulating in different forms, hiding the main idea and showing the purpose only.'''

'''Question 2
Benefits of OOP:
	1. reduces work
	2.can break work into modules
	3.hiding the main code
	4.changes form for every object
	5.allows inheritance,abstraction, overriding
	'''
'''Question 3 A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences. The method is implicitly used for an object for which it is called. The method is accessible to data that is contained within the class'''

'''Question 4
class: is data type to which any object belongs to
   object: is a variable which initializes the class 
   attribute: Are the features of class
   behaviour: Is how each method works or performs... Represents nature'''
 # Question 5
 
class Car:
	def __init__(self,name,colour,model,tyre,no_of_seats):
		self.name=name
		self.colour=colour
		self.model=model
		self.tyre=tyre
		self.no=no_of_seats
	def print_info(self):
		print("Name:",self.name,'\n',"Colour:",self.colour,'\n',"Model:",self.model,'\n',"Tyres:",self.tyre,'\n',"No of seats:",self.no)
	def update(self,clr):
		self.colour=clr
		print('Colour changed',self.colour)
a=Car("Chevrolet","red","4590","4","5")
a.print_info()
a.update("Purple")