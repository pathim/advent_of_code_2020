def read_input():
	def line_to_code(l):
		opcode,value=l.strip().split(' ')
		value=int(value)
		return opcode,value
		
	with open('input') as f:
		return [line_to_code(l) for l in f]
		
def execute(code,visited,acc=0,ip=0,branch=False):
	while True:
		if ip in visited:
			return (acc, True)
		visited.add(ip)
		try:
			op,val=code[ip]
		except IndexError:
			return (acc, False)
		ip+=1
		if op=='nop':
			if branch:
				last_acc,looped=execute(code,visited.copy(),acc,ip-1+val,False)
				if not looped:
					return last_acc,False
		if op=='acc':
			acc+=val
		if op=='jmp':
			if branch:
				last_acc,looped=execute(code,visited.copy(),acc,ip,False)
				if not looped:
					return last_acc,False
			ip+=val-1
			
code=read_input()
first=execute(code,set())
print(f"First solution {first[0]}")
second=execute(code,set(),0,0,True)
print(f"Second solution {second[0]}")
