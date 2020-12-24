import re

def read_line(line):
	regex=re.compile('(e|se|sw|w|nw|ne)')
	result=[]
	while line:
		m=regex.match(line)
		end=m.end()
		result.append(line[:end])
		line=line[end:]
	return result

def movements_to_coords(mov):
	x=0
	y=0
	for m in mov:
		if m=='e':
			x+=1
		elif m=='w':
			x-=1
		elif m=='se':
			x+=1
			y-=1
		elif m=='sw':
			y-=1
		elif m=='nw':
			y+=1
			x-=1
		elif m=='ne':
			y+=1
	return (x,y)

black=set()

with open('input') as f:
	for line in f:
		coords=movements_to_coords(read_line(line.strip()))
		black^={coords}
print(f"First solution: {len(black)}")