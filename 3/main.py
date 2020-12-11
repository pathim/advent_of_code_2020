from operator import mul
from functools import reduce

data=[]
with open('input') as f:
	for line in f:
		data.append(line.strip())

def count_trees(right,down):
	pos=0
	treecount=0
	for l in data[::down]:
		if l[pos]=='#':
			treecount+=1
		pos=(pos+right)%len(l)
	return treecount

print(f"First solution {count_trees(3,1)}")

second_directions=[(1,1),(3,1),(5,1),(7,1),(1,2)]
trees=[count_trees(*x) for x in second_directions]

result=reduce(mul,trees,1)
print(f"Second solution {result}")
