# Name:
# Period:
def checkTrees(mat):
	count = 0
	
	for row in range(1,len(mat)-1):
		for col in range(1,len(mat[row])-1):
			if(checkSpot(mat,row,col)):
				count +=1
				
	count += (len(mat)*2)+((len(mat[0])-2)*2)
	return count
				
def checkSpot(mat, r, c):
	check = True
	tree = mat[r][c]
	
	#if(r==0 or c==0 or r==len(mat)-1 or c==len(mat[r])-1:
	#	return True
	
	
	#go north
	for i in range(r - 1, -1, -1):
		if(mat[i][c]>=tree):
			#print(f"\tlocation {r} {c} not visible going North {tree} vs {mat[i][c]}")
			check = False
			break
	if(check):
		#print(f"location {r} {c} is visable going north")
		return True
	
	#go west
	check= True
	for i in range(c - 1, -1, -1):
		if(mat[r][i]>=tree):
			#print(f"\tlocation {r} {c} not visible going west {tree} vs {mat[r][i]}")
			check = False
			break
	if(check):
		#print(f"location {r} {c} is visable going west")
		return True
	
	#go south
	check= True
	for i in range(r + 1, len(mat)):
		if(mat[i][c]>=tree):
			#print(f"\tlocation {r} {c} not visible going south {tree} vs {mat[i][c]}")
			check = False
			break
	if(check):
		#print(f"location {r} {c} is visable going south")
		return True
	
	#go east
	check= True
	for i in range(c + 1, len(mat[r])):
		if(mat[r][i]>=tree):
			#print(f"\tlocation {r} {c} not visible going east {tree} vs {mat[r][i]}\n")
			check = False
			break
	if(check):
		#print(f"location {r} {c} is visable going east")
		return True
		
	return False
# Period:
def checkTrees2(mat):
	count = 0
	max = (-1,-1,-1)
	for row in range(1,len(mat)-1):
		for col in range(1,len(mat[row])-1):
			view = checkSpot2(mat,row,col)
			if( view > max[0]):
				max = (view, row, col)
	print("tree", max ,mat[max[1]][max[2]])
	return max[0]
def checkSpot2(mat, r, c):

	tree = mat[r][c]
	count = 0
	total = 0
		
	#go north
	for i in range(r - 1, -1, -1):
		count+=1
		if(mat[i][c]>=tree):
			#print(f"\tlocation {r} {c} not visible going North {tree} vs {mat[i][c]}")
			break
	total = count
	
	#go west
	count=0
	for i in range(c - 1, -1, -1):
		count+=1
		if(mat[r][i]>=tree):
			#print(f"\tlocation {r} {c} not visible going west {tree} vs {mat[r][i]}")
			break		
	total *= count
	
	#go south
	count=0
	for i in range(r + 1, len(mat)):
		count+=1
		if(mat[i][c]>=tree):
			#print(f"\tlocation {r} {c} not visible going south {tree} vs {mat[i][c]}")
			break
	total *= count
	
	#go east
	count=0
	for i in range(c + 1, len(mat[r])):
		count+=1
		if(mat[r][i]>=tree):
			#print(f"\tlocation {r} {c} not visible going east {tree} vs {mat[r][i]}\n")
			check = False
			break
	total *= count
	
	return total
with open('input.txt') as f:
	lines = f.readlines()
	mat = []
	for line in lines:
		mat.append([int(x) for x in line.strip()])
	#print(mat)
	checkTrees(mat)
	#print(f"how many rows {len(mat)}")
	#print(f"how many cols {len(mat[0])}")
	
	#Part #1
	print("Part 1 answer")
	print(f"how many trees visible {checkTrees(mat)}\n")
	
	#Part #2
	print("Part 2 answer")
	print("most scenic", checkTrees2(mat))
	
#9801 is too high
#2906 is too high
#1726 is too high
#1168 is not right
