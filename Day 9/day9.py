# Name:
# Period:
class Grid:
	def __init__(self):
		#self.grid = [["."] *100]*100
		self.visited = [[False] *100]*100
		self.tail = [0,0]
		self.head = [0,0]
		self.visited[0][0]= True
	def move(self, instruction):
		
		direction = self.change(instruction[0])	
		space = instruction.find(" ")
		number = int(instruction[space+1:])
		
		for x in range(number):
			if(letter=="R"):
				self.head[1] += 1
			elif(letter=="L"):
				self.head[1] -= 1
			elif(letter=="U"):
				self.head[0] +=1
			elif(letter=="D"):
				self.head[0] -=1
		
		print(f"org instruction {instruction}\ndirection {direction} {number}")
	def change(self, letter):
		if(letter=="R"):
			return "L"
		elif(letter=="L"):
			return "R"
		elif(letter=="U"):
			return "D"
		elif(letter=="D"):
			return "U"
		print("what?!")
	#def check(self):
		
with open('input.txt') as f:
	lines = f.readlines()
	
	
	line = lines[0]
	g = Grid()
	for line in lines[: 50]:
		g.move(line.strip())
