#Task 1
class dic:
	def __init__(self):
		self.info={}
	def dictionary(self,firstname,lastname,age,city):
		self.info['Firstname:']=firstname
		self.info['Lastname:']=lastname
		self.info['Age:']=age
		self.info['City:']=city
	def print(self):
		for keys in self.info.keys():
			print(keys,self.info[keys],end="\n")
	def add(self,qualification):
		self.info["Qualification:"]=qualification
	def update(self,qualification):
		self.info["Qualification:"]=qualification
	def delete(self,key):
		for keys in self.info.keys():
			if key==keys:
				del self.info[key]
				return self.info
a=dic()
a.dictionary('Insiyah','Talib',17,'Punjab')
a.add('College')
a.print()
print('*******Updated info*********')
a.update('University')
a.print()
a.delete("Qualification:")
print('******After deletion*********')
a.print()
#Task 2
def create():
	n=int(input('Enter the no of cities:'))
	cityname=[]
	cityinfo={}
	info=[]
	while n>0:
		city=str(input('Enter the name of city:'))
		cityname.append(city)
		country=str(input ('Enter the country:'))
		fact=str(input('Enter the fact:'))
		info1=[]
		population=str(input('Enter the population:'))
		info1.append('Country:'+country)
		info1.append('Fact:'+fact)
		info1.append('Population:'+population)
		info.append(info1)
		n=n-1
	for j in range(0,len(cityname)):
		cityinfo[cityname[j]]=info[j]
	print(cityinfo)
#create()
#Task 3
n=int(input ('No of people watching movie:'))
for j in range(n):
	age=int(input ('Enter the age:'))
	charge=None
	if age<=3:
		charge='Free'
		print(charge)
	if age>3 and age<12:
		charge='$10'
		print(charge)
	if age>12:
		charge='$15'
		print(charge)
#Task 4
def fav_book(title):
	print('My favourite book:',title)
fav_book('Alice in the Wonderland')
#Task 5
import random
number=random.randint(1,30)
n=3
status=False
while n>0:
	guess=int(input('Enter the guess:'))
	if guess ==number:
		print('correct!')
		status=True
	elif guess<number:
		print('A greater no!')
	elif guess>number:
		print('A lesser no!')
	n=n-1
if status is True:
	print('You have guessed the number!')
else:
	print('Failed to guess!',number)


	
		
		