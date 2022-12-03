#PART #1 METHODS
def find(first, second):
	for letter in first:
		if(letter in second):
			return letter
	print("something wrong")	
def priority(letter):
	number =  ord(letter)
	#print(letter)
	if(number>=65 and number<=90):
		return number - 64 +26
	if(number>=97 and number<=122):
		return number - 96

#PART #2 Methods
def find2(first, second, third):
	for letter in first:
		if(letter in second and letter in third):
			return letter
	print("something wrong")	
''' Part #1 main
with open('input.txt') as f:
	lines = f.readlines()
	total = 0
	for line in lines:
		line = line.strip()
		first_half = line[0:len(line)//2]
		second_half = line[len(line)//2:]
		print("first ", first_half)
		print("second ", second_half)
		total +=(priority(find(first_half, second_half)))
	print("total", total)
'''

with open('input.txt') as f:
	lines = f.readlines()
	total = 0
	for loc in range(0,len(lines),3):
		line1 = lines[loc].strip()
		line2 = lines[loc+1].strip()
		line3 = lines[loc+2].strip()

		total +=(priority(find2(line1,line2,line3)))
	print("total", total)
