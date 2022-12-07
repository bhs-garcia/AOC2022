# Name:
# Period:
def letters(word, number):
	#print("sub letters",word[0:number]+word[number+1:])
	return word[0:number]+word[number+1:]
def found(word, number):
	letter = word[number]
	sub = letters(word, number)

	if(letter in sub):
		return True
	else:
		print("\ninside the else")
		print("letter",letter)
		print("lettters to check", sub)
		return False
def findUnique(word):
	for i in range(4):
		if(found(word, i)):
			#print("i",i)
			return False
	print("i",i)
	print("word",word)
	return True
with open('input.txt') as f:
	lines = f.read()
	#print(lines)
	print(len(lines))
	for x in range(0,len(lines)-3):
		word = lines[x:x+4]
		print(word)
		if(findUnique(word)):
			print("Found it!")
			print("location",x+1)
			break
		#print(letters(lines[x:x+4],1))

#1621 is wrong		
#1626 is too high

#location 1622
#word lhvf
