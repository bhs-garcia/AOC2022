# Name:
# Period:
class Grid:
	def __init__(self):
		self.grid = [["."] *100]*100
		#self.visited = [[False] *100]*100
		self.tail = [0,0]
		self.head = [0,0]
		#self.visited[0][0]= True
		start = (0,0)
		self.visited = set()
		self.visited.add(start)
	def move(self, instruction):
		#direction = self.change(instruction[0])
		direction = instruction[0]	
		space = instruction.find(" ")
		number = int(instruction[space+1:])
		
		#self.check()
		#print(f"\norginal instruction {instruction}\t new direction {direction} {number}")
		print(f"\ndirection {direction} {number}")
		
		
		for x in range(number):
			if(direction=="R"):
				self.head[1] += 1
			elif(direction=="L"):
				self.head[1] -= 1
			elif(direction=="U"):
				self.head[0] -=1
			elif(direction=="D"):
				self.head[0] +=1
			
			self.check()
		
	'''def change(self, letter):
		if(letter=="R"):
			return "L"
		elif(letter=="L"):
			return "R"
		elif(letter=="U"):
			return "D"
		elif(letter=="D"):
			return "U"
		print("what?!")'''
	def check(self):
		print(f"head location{self.head} tail location{self.tail}")
		tailrow = self.tail[0]
		tailcol = self.tail[1]
		
		headrow = self.head[0]
		headcol = self.head[1]
		
		rowdif = abs(tailrow-headrow)
		coldif = abs(tailcol-headcol)
		if(rowdif==0 and coldif==0):
			print("They're touching at the same location")
		elif(tailrow==headrow and coldif==1):
			print("They're touching at the row")
		elif(tailcol==headcol and rowdif==1):
			print("They're touching at the col")
		elif(rowdif==1 and coldif==1):
			print("Thye're touching at a diagonal")
		else:
			print("not touching")
			#Same row
			if(rowdif==0 and tailcol-headcol == -2):
				print("Two spots away on same row")
				self.tail[1]+=1
				self.visited.add((self.tail[0],self.tail[1]))
				print(f"Just moved tail. new location {self.tail}")
			elif(rowdif==0 and tailcol-headcol == 2):
				print("Two spots away on same row")
				self.tail[1]-=1
				self.visited.add((self.tail[0],self.tail[1]))
				print(f"Just moved tail. new location {self.tail}")
			#same col
			elif(coldif==0 and tailrow-headrow == -2):
				print("Two spots away on same col")
				self.head[1]+=1
				self.visited.add((self.head[0],self.head[1]))
				print(f"Just moved tail. new location {self.head}")
			elif(coldif==0 and tailrow-headrow == 2):
				print("Two spots away on same col")
				self.head[1]-=1
				self.visited.add((self.head[0],self.head[1]))
				print(f"Just moved tail. new location {self.head}")
			#on diagonal
			elif(coldif!=0 and rowdif!=0):
				print("On different diagonal")
				#to the right
				if(coldif==1 and tailrow-headrow ==2):
					print("to the right and below")
				elif(coldif==1 and tailrow-headrow ==2):
		
with open('input.txt') as f:
	lines = f.readlines()
	
	line = lines[0]
	g = Grid()
	for line in lines[: 20]:
		g.move(line.strip())
	print(g.visited)
