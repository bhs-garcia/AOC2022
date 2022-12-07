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
#Extra method used for debugging 
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

#Extra methods created to have non-hard coded input.
#Finds the line number of where the stack numbers are and
#returns that number
def stack_line(lines):
	x = 0
	for line in lines:
		line = line.strip()
		info = line.split(" ")
		if(info[0]=="1"):
			return x
		x += 1
	return -1
#Find the line number and returns the number of the last stack
def stack_count(lines):
	x = 0
	for line in lines:
		line = line.strip()
		info = line.split(" ")
		if(info[0]=="1"):
			return int(info[-1])
		x += 1
	return -1	

with open('input.txt') as f:
	lines = f.readlines()
	#stacks = [[],[],[],[],[],[],[],[],[]]
	stacks = []
	stack_line_number = stack_line(lines)
	
	for x in range(stack_count(lines)):
		stacks.append([])
	
	#slice starts at below the stack_line_number, 
	#counting backwards by -1, to the beginning part of the input
	for line in lines[stack_line_number-1::-1]:
		line = line.strip("\n")
		stack = 0
		for x in range(1,len(line),4):
			if(line[x]!=" "):
				stacks[stack].append(line[x])
			stack +=1
	
	for line in lines[stack_line_number+2:]:
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
