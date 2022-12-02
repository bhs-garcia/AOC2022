# Name:
# Period:

#Functions needs for Part #2
def checkLarger(numbers, num):
	for x in numbers:
		if(num>x):
			return True
	return False
def removeSmall(numbers):
	if(numbers[0]<= numbers[1] and numbers[0]<=numbers[2]):
		numbers.pop(0)
	elif(numbers[1]< numbers[2] and numbers[1]<numbers[0]):
		numbers.pop(1)
	elif(numbers[2]< numbers[0] and numbers[2]<numbers[1]):
		numbers.pop(2)

with open('input.txt') as f:
	lines = f.readlines()
	total = 0
	totals = []
	for line in lines:
		if(len(line)>2):
			#print(line,end=" ")
			number = int(line[:-1])
			#print(number)
			total += number
		else:
			totals.append(total)
			total=0
	'''
	Code for part #1
	max = 0
	for x in range(len(totals)):
		if(totals[x]> totals[max]):
			max = x
	print(max)
	print(totals[max])
	print(totals)'''

	#Code for part #2
	max3 = [0,0,0]
	for x in totals:
		if(checkLarger(max3,x)==True):
			removeSmall(max3)
			max3.append(x)
	print(max3)
	print(max3[0]+max3[1]+max3[2])
