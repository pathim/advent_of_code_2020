def do_turn(data,current,max_val):
	pos=data.index(current)+1
	taken=[]
	for _ in range(3):
		if pos>=len(data):
			pos=0
		taken.append(data.pop(pos))
	dest=current-1
	if dest==0:
		dest=max_val
	while not dest in data:
		dest-=1
		if dest==0:
			dest=max_val
	dest_idx=data.index(dest)+1
	for c  in reversed(taken):
		data.insert(dest_idx,c)
	pos=data.index(current)+1
	if pos>=len(data):
		pos=0
	return data[pos]

def sort_for_result(data):
	idx=data.index(1)
	return data[idx+1:]+data[:idx]

data=[int(x) for x in open('input').read().strip()]
#data=[3, 8,  9,  1,  2,  5,  4,  6,  7]

max_val=max(data)

current=data[0]
data1=data.copy()
for _ in range(100):
	current=do_turn(data1,current,max_val)
first=''.join(str(x) for x in sort_for_result(data1))
print(f"First solution {first}")
