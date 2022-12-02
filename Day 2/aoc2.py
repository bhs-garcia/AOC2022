# Name:
# Period:

#FUNCTIONS FOR PART #1	
def winner(opp,me):
	if(opp=="A" and me =="X"):
		return 3
	elif(opp=="B" and me =="Y"):
		return 3
	elif(opp=="C" and me =="Z"):
		return 3
	#Rock vs SC
	elif(opp=="A" and me =="Z"):
		return 0	
	#Paper VS rock
	elif(opp=="B" and me =="X"):
		return 0
	#Scissors vs paper
	elif(opp=="C" and me =="Y"):
		return 0
	else:
		return 6
		
		
def objectPoints(me):
	if(me=="X"):
		return 1
	elif(me=="Y"):
		return 2
	elif(me=="Z"):
		return 3
	else:
		print("what did you do?", me)
		return 0

#FUNCTIONS FOR PART #2
def objectPoints2(opp, me):
	if(me=="X"):
		if(opp=="A"):
			return 3
		elif(opp=="B"):
			return 1
		elif(opp=="C"):
			return 2
	elif(me=="Y"):
		if(opp=="A"):
			return 1
		elif(opp=="B"):
			return 2
		elif(opp=="C"):
			return 3
	elif(me=="Z"):
		if(opp=="A"):
			return 2
		elif(opp=="B"):
			return 3
		elif(opp=="C"):
			return 1
	else:
		print("what did you do?", me)
		return 0
def winner2(opp,me):
	if(me=="X"):
		return 0
	elif(me=="Y"):
		return 3
	elif(me=="Z"):
		return 6


with open('input2.txt') as f:
	lines = f.readlines()
	total = 0
	for line in lines:
		opp = line[0]
		me = line[2]
		total += winner2(opp,me) + objectPoints2(opp, me)
		print(total)
