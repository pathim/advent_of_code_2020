from operator import and_,mul,or_
from functools import reduce

class Fields:
	def __init__(self):
		self.fields=dict()
	def add(self,name,ranges):
		self.fields[name]=ranges
	def check_single(self,name,val):
		r1,r2=self.fields[name]
		return r1[0]<=val<=r1[1] or r2[0]<=val<=r2[1]
	def check(self,val):
		return {name for name in self.fields if self.check_single(name,val)}

class Ticket:
	def __init__(self, nums, fields):
		self.candidates=[(num,fields.check(num)) for num in nums]
	def find_invalid(self):
		return [x[0] for x in self.candidates if not x[1]]
	def get_possible_fields(self,index):
		return self.candidates[index][1]

def read_fields(f):
	fields=Fields()
	for l in f:
		l=l.strip()
		if not l:
			return fields
		name,ranges=l.split(': ')
		r1,r2=ranges.split(' or ')
		fields.add(name,([int(x) for x in r1.split('-')],[int(x) for x in r2.split('-')]))
	return fields

def read_tickets(f,fields):
	next(f) # skip first line containing 'your' or 'nearby' tickets
	tickets=[]
	for l in f:
		l=l.strip()
		if not l:
			return tickets
		nums=[int(x) for x in l.split(',')]
		tickets.append(Ticket(nums,fields))
	return tickets

def read_file(filename):
	with open(filename) as f:
		fields=read_fields(f)
		my_ticket=read_tickets(f,fields)[0]
		other_tickets=read_tickets(f,fields)
	return my_ticket, other_tickets

def solve_one(possible_fields):
	fieldlist=reduce(or_,possible_fields)
	for f in fieldlist:
		c=[]
		for n,pf in enumerate(possible_fields):
			if f in pf:
				c.append(n)
		if len(c)==1:
			idx=c[0]
			for n,pf in enumerate(possible_fields):
				pf.difference_update({f})
			possible_fields[idx]={f}

def is_solved(possible_fields):
	return max(len(x) for x in possible_fields)==1

def solve(possible_fields):
	possible_fields=possible_fields.copy()
	while not is_solved(possible_fields):
		solve_one(possible_fields)
	return [next(iter(x)) for x in possible_fields]



my,other=read_file('input')
first=sum(sum(x.find_invalid()) for x in other)
print(f"First solution {first}")
valid_tickets=[x for x in other if not x.find_invalid()]+[my]

possible_fields=[]
for n in range(len(my.candidates)):
	field=reduce(and_,(x.get_possible_fields(n) for x in valid_tickets))
	possible_fields.append(field)
fieldnames=solve(possible_fields)

second=reduce(mul,(x[0] for name,x in zip(fieldnames,my.candidates) if name.startswith('departure')))
print(f"Second solution {second}")
