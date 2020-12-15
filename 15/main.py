from collections import OrderedDict

def read_numbers(filnename:str)->[int]:
	with open('input') as f:
		return [int(x) for x in f.read().strip().split(',')]

def init_numbers(l:[int])->{int:[int]}:
	res=OrderedDict()
	for n,x in enumerate(l):
		res[x]=[n+1]
	return res

def next_number(nums:OrderedDict,turn:int):
	appearances=next(reversed(nums.values()))
	if len(appearances)==1:
		new_num=0
	else:
		new_num=appearances[-1]-appearances[-2]
	try:
		newval=(nums[new_num][-1],turn)
	except KeyError:
		newval=(turn,)
	nums[new_num]=newval
	nums.move_to_end(new_num)
	return new_num

def nth(num,n):
	turn=0
	for v in num.values():
		turn=max(turn,max(v))
	while turn<n:
		turn+=1
		res=next_number(num,turn)
		if turn%100000==0:
			print(turn)
	return res

first=nth(init_numbers(read_numbers('input')),2020)
print(f"First solution {first}")

second=nth(init_numbers(read_numbers('input')),30000000)
print(f"Second solution {second}")