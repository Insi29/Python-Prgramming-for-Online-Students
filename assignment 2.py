#Task 1
grades={}
grades['Maths:']=int(input('Enter the math marks:'))
grades['Science:']=int(input('Enter the science marks:'))
grades['English:']=int(input('Enter the english marks:'))
grades['Computer:']=int(input('Enter the computer marks:'))
grades['Urdu:']=int(input('Enter the urdu marks:'))
sum=0
for i in grades.keys():
	sum+=grades[i]
	print('The marks obtained in {} are :{}'.format(i,grades[i]))
print('The percentage:',sum/5)

#Task 2
a=int(input('Enter the input to be checked:'))
if a %2==0:
	print('The number is even!')
else:
	print('The number is odd!')
#Task 3
def length(lists):
	count=0
	for i in lists:
		count+=1
	return count
print('The length of list is:',length([1,2,3,4,5,6,7,8,9,10]))
#Task 4
l=[2,3,'a',6,7,8,'b','c',5]
sum=0
for i in l:
	if i.__class__.__name__=='int':
		sum+=i
print('The sum of integer elements of list:',sum)
#Task 5
def largest(arr):
	arr.sort()
	largest=arr[0]
	for i in range (len(arr)):
		if arr[0]<arr[i]:
			largest=arr[i]
		else:
			largest=arr[0]
	return largest
print('The largest element of list:',largest([1,2,12,35,64,73,82,10,91,45]))
#Task 6
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
	if i <5:
		print(i,end=' ')

		