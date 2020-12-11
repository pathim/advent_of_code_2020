target=2020
data=[]
with open('input') as f:
	for line in f:
		data.append(int(line))
for i,a in enumerate(data):
	for j,b in enumerate(data[i+1:]):
		if a+b>target:
			continue
		if a+b==target:
			print(f"First solution: {a*b}")
			continue
		for c in data[j+1:]:
			if a+b+c==target:
				print(f"Second solution: {a*b*c}")

