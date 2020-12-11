from collections import deque

def is_valid(num,num_list):
	for i,n1 in enumerate(num_list):
		for n2 in num_list[i:]:
			if n1!=n2 and n1+n2==num:
				return True
	return False
	
def find_fist_invalid(d):
	checknumbers=d[:25]
	for num in d[25:]:
		if is_valid(num,checknumbers):
			checknumbers.pop(0)
			checknumbers.append(num)
		else:
			return num

def find_contiguous_simple(num,d):
	checknumbers=[]
	for x in d:
		while (s:=sum(checknumbers))>num:
			checknumbers.pop(0)
		if s==num:
			return min(checknumbers)+max(checknumbers)
		checknumbers.append(x)
		
def find_contiguous_cumsum(num,d):
	cumsum=[0]
	begin=0
	for end in range(len(d)):
		while (s:=cumsum[end]-cumsum[begin])>num:
			begin+=1
		if s==num:
			return min(d[begin:end])+max(d[begin:end])
		cumsum.append(cumsum[-1]+d[end])
	
data=[]
with open('input') as f:
	for l in f:
		data.append(int(l.strip()))
first=find_fist_invalid(data)
print(f"First solution {first}")
second=find_contiguous_simple(first,data)
second2=find_contiguous_cumsum(first,data)
print(f"Second solution (simple) {second}")
print(f"Second solution (cumsum) {second2}")