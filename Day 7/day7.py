# Name:
# Period:
class File_info:
	def __init__(self,name,num):
		self.name=name
		self.size=num
		
	def set_size(self, num):
		self.size=num
	def __str__(self):
		return self.name+" " +self.size

class Directory:
	def __init__(self, name, prevDirectory=None, num=0):
		self.name = name
		self.directories = []
		self.files = []
		self.previous = prevDirectory
		self.size = 0
	def add_directory(self, directory):
		self.directories.append(directory)
	def add_file(self, newFile):
		self.files.append(newFile)
	def set_size(self, size):
		self.size = size
	def __str__(self):
		return "Current Directory "+self.name

	def find_directory(self, name):
		i = 0
		
		if(name==".."):
			return -1
		if len(self.directories)==0:
			return -2
		for x in self.directories:
			if(x.name==name):
				#print("found",name,"at position",i)
				return i
			i+=1
		print("something wrong! couldn't find ",name)

with open('input.txt') as f:
	lines = f.readlines()
	
	root = Directory("/")
	current = root
	
	for line in lines[2:25]:
		line = line.strip() 
		sub = line[0:3]
		
		if(sub=="dir"):
			#if its a directory
			print("found dir:", line)
			
			name = line[4:]

			current.add_directory(Directory(name,current))

		elif(line[0:4]=="$ cd"):
			#if it a cd
			print("\nfound command:", line)
			print(current,end=" ")
			space = line.rfind(" ")
			name = line[space+1:]
			loc = current.find_directory(name)
			#print("location of directory",loc)
			if(loc==-1):
				current = current.previous
			else:
				current = current.directories[loc]
			print("Now in",current)
		elif(line[0:4]=="$ ls"):
			#if it a ls, ignore
			continue
		else:
			#if its a file
			print("\tfound file:", line)
			
			space = line.find(" ")
			number = int(line[:space])
			name = line[space+1:]
			
			currentFile = File_info(name,number)
			
			current.add_file(currentFile)
			
		
	print(root)
