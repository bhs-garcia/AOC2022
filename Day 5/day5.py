#Method used for Part #1
def moveCrates(stacks, number, fromStack, toStack):
	for x in range(number):
		item = stacks[fromStack].pop()
		stacks[toStack].append(item)
#Method used for Both Parts
def convert(info):
	numbers = []
	for let in info:
		numbers.append(int(let))
	return numbers
#Method used for Both Parts
def top(stacks):
	letters = ""
	for stack in stacks:
		letters += stack[-1]	
	print(letters)

#Extra method used for debugging
def print_stack(stacks):
	num = 1
	for stack in stacks:
		print("Stack #",num," ", end="")
		for number in stack:
			print(number, end="")	
		num += 1
		print()

#Method used for Part #2
def moveCrates2(stacks, number, fromStack, toStack):
	loc = len(stacks[fromStack])-number
	for x in range(number):
		item = stacks[fromStack].pop(loc)
		stacks[toStack].append(item)
		
with open('input.txt') as f:
	lines = f.readlines()
	stacks = [[],[],[],[],[],[],[],[],[]]
	
	#slice starts at line 8, counting backwards by -1, to the beginning part of the list
	for line in lines[7::-1]:
		line = line.strip("\n")
		stack = 0
		for x in range(1,len(line),4):
		#	print(line[x], end="")
			if(line[x]!=" "):
				stacks[stack].append(line[x])
			stack +=1
		#print()
	
	#print_stack(stacks)
	for line in lines[10:]:
		#Remove the \n character at the end
		line = line.strip("\n") 
		
		#Remove all of the extra words
		line = line.replace("move ","")
		line = line.replace("from ","")
		line = line.replace("to ","")
		
		#Split by the spaces and convert to an integer list
		info = line.split(" ")
		info = convert(info)
		
		#print(info)
		moveCrates2(stacks, info[0],info[1]-1,info[2]-1)
		#print_stack(stacks)
		
	print_stack(stacks)
	top(stacks)
