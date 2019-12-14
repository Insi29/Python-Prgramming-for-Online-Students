import random
#Task 1
def factorial(n):
	assert n>0, "Negative Number"
	if n<=1:
		return 1
	else:
		return n*factorial (n-1)
print(factorial (7))
#Task 2
def count_cases(string):
	string=string.replace(" ","")
	upper=list(string.upper())
	lower=list(string.lower())
	low=0
	up=0
	for cases in string:
		if cases in upper:
			low+=1
		else:
			up+=1
	print("Lower case count:{} \nUpper case count:{}". format (low,up))
count_cases("Programming Classes")
#Task 3
def even(data):
	for no in data:
		if no%2==0:
			print(no,end="\n")
n=int(input("Enter the no is list:"))
data_list=[]
for j in range(n):
	data_list.append(random.randint(1,50))
print("Given list:",data_list)
even(data_list)

#Task4
def palindrome(words):
	rev=words[::-1]
	if words.lower()==rev.lower():
		print(words,"Is a palindrome!")
	else:
		print(words,"Is not palindrome!")
palindrome("Racecar")

#Task 5
def prime (n):
	if n>1:
		for a in range(2,n):
			if n%a==0:
				print("It's not prime!")
				break
			else:
				print("It is a prime!")
				break
n=int(input ("Enter the number:"))
prime(n)

#Task 6
def shop_list():
	user_list=list()
	while True:
		stuff=str(input ("Enter things user buys:"))
		if stuff=="finish"or stuff=="F":
			break
		else:
			user_list.append(stuff)
	print("Shopping list",user_list)
	
shop_list()