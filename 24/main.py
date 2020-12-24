import re
from collections import defaultdict

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

def neighbours(coords):
	nb=[(1,0),(-1,0),(1,-1),(0,-1),(-1,1),(0,1)]
	res={tuple(a+b for a,b in zip(n,coords)) for n in nb}
	return res

def generation(current):
	nb_count=defaultdict(int)
	for c in current:
		for n in neighbours(c):
			nb_count[n]+=1
	new={k for k,v in nb_count.items() if v==2}
	keep={k for k,v in nb_count.items() if v==1 and (k in current)}
	return new|keep


black=set()

with open('input') as f:
	for line in f:
		coords=movements_to_coords(read_line(line.strip()))
		black^={coords}
print(f"First solution: {len(black)}")

for _ in range(100):
	black=generation(black)
print(f"Second solution: {len(black)}")