from operator import mul
from functools import reduce

data=[0]
def create_segments(d):
	res=[]
	while d:
		idx=d.index(3)
		if idx>=2:
			res.append(idx-1)
		d=d[idx+1:]
	return res

# In general this should map n to the number of
# n-bit numbers that have no more that two consecutive zeros 
number_to_ways={1:2,2:4,3:7}

with open('input') as f:
	for l in f:
		data.append(int(l.strip()))
data.sort()
diffs=[]
for a,b in zip(data,data[1:]):
	diffs.append(b-a)
diffs.append(3)
ones=diffs.count(1)
threes=diffs.count(3)
first=ones*threes
print(f"First solution: {first,ones,threes}")
second=reduce(mul,(number_to_ways[x] for x in create_segments(diffs)),1)
print(f"Second solution: {second}")