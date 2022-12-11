#Method for part #1
def check(info):
	r1 = range(info[0],info[1]+1)
	r2 = range(info[2],info[3]+1)
	if(info[2] in r1 and info[3] in r1):
		#print(r1,r2)
		return True
	elif(info[0] in r2 and info[1] in r2):
		#print(r1,r2)
		return True
	return False

#Method used in both parts
def convert(info):
	numbers = []
	for let in info:
		numbers.append(int(let))
	return numbers
	
#Method used in part #2
def check2(info):
	r1 = range(info[0],info[1]+1)
	r2 = range(info[2],info[3]+1)
	if(info[2] in r1 or info[3] in r1):
		#print(r1,r2)
		return True
	elif(info[0] in r2 or info[1] in r2):
		#print(r1,r2)
		return True
	return False	

#Main part of the code

with open('input.txt') as f:
	lines = f.readlines()
	count=0
	for line in lines:
		#Replaced all of the , with -
		#so I can split all of the info
		info = line.strip().replace(",","-").split("-")
		info  = convert(info)
		
		if(check2(info)):
			count+=1
	print("count",count)
