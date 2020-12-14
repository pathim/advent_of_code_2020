from collections import defaultdict
class Bitmask:
	def __init__(self,mask_str:str):
		self.and_mask=int(mask_str.replace('X','1'),2)
		self.or_mask=int(mask_str.replace('X','0'),2)
		
	def apply(self,val:int):
		return (val&self.and_mask)|self.or_mask
		
class Docking:
	def __init__(self):
		self.mem=defaultdict(int)
		self.bm=Bitmask('X'*36)
		
	def set(self,addr:int,val:int):
		self.mem[addr]=self.bm.apply(val)
		
	def execute(self,cmd:str):
		lhs,rhs=cmd.split('=')
		lhs=lhs.strip()
		rhs=rhs.strip()
		if lhs=='mask':
			self.bm=Bitmask(rhs)
		elif lhs.startswith('mem'):
			addr=int(lhs[4:-1])
			val=int(rhs)
			self.set(addr,val)

class Bitmask2:
	def __init__(self,mask_str:str):
		self.mask=mask_str

	def _apply_one_x(self,x_bit:int,val:[int])->[int]:
		mask=1<<x_bit
		res=[ [v|mask,v&~mask] for v in val]
		return sum(res,[])

	def apply(self,val:int):
		val=[int(self.mask.replace('X','0'),2)|val]
		idx=0
		mask=self.mask[::-1]
		while True:
			try:
				idx=mask.index('X',idx)
			except ValueError:
				return val
			val=self._apply_one_x(idx,val)
			idx+=1
		
class Docking2:
	def __init__(self):
		self.mem=defaultdict(int)
		self.bm=Bitmask2('0'*36)
		
	def set(self,addr:int,val:int):
		addrs=self.bm.apply(addr)
		for a in addrs:
			self.mem[a]=val
		
	def execute(self,cmd:str):
		lhs,rhs=cmd.split('=')
		lhs=lhs.strip()
		rhs=rhs.strip()
		if lhs=='mask':
			self.bm=Bitmask2(rhs)
		elif lhs.startswith('mem'):
			addr=int(lhs[4:-1])
			val=int(rhs)
			self.set(addr,val)

d=Docking()
d2=Docking2()
with open('input') as f:
	for l in f:
		d.execute(l)
		d2.execute(l)

first=sum(d.mem.values())
print(f"First solution: {first}")
second=sum(d2.mem.values())
print(f"Second solution: {second}")
		