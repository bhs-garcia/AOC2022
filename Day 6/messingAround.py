# Name:
# Period:
with open('input.txt') as f:
	lines = f.read()
	with open('output.txt', 'w') as f2:
		for x in range(0,len(lines),10):
			f2.write(lines[x:x+10]+"\n")
		f2.close()
		
