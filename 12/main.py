class Navi:
	def __init__(self,pos0=0+0j,dir0=1+0j):
		self.pos=pos0
		self.dir=dir0
	
	def do_cmd(self,cmd):
		char=cmd[0]
		val=int(cmd[1:])
		if char=='F':
			self.pos+=self.dir*val
		elif char=='N':
			self.pos+=1j*val
		elif char=='S':
			self.pos+=-1j*val
		elif char=='E':
			self.pos+=val
		elif char=='W':
			self.pos+=-val
		elif char=='R':
			self.dir*=(-1j)**(val/90)
		elif char=='L':
			self.dir*=(1j)**(val/90)
		else:
			raise ValueError(f'Unknown command {cmd}')
		
class Navi2:
	def __init__(self,pos0=0+0j,dir0=10+1j):
		self.pos=pos0
		self.dir=dir0
	
	def do_cmd(self,cmd):
		char=cmd[0]
		val=int(cmd[1:])
		if char=='F':
			self.pos+=self.dir*val
		elif char=='N':
			self.dir+=1j*val
		elif char=='S':
			self.dir+=-1j*val
		elif char=='E':
			self.dir+=val
		elif char=='W':
			self.dir+=-val
		elif char=='R':
			self.dir*=(-1j)**(val/90)
		elif char=='L':
			self.dir*=(1j)**(val/90)
		else:
			raise ValueError(f'Unknown command {cmd}')
		
n=Navi()
n2=Navi2()
with open('input') as f:
	for l in f:
		cmd=l.strip()
		n.do_cmd(cmd)
		n2.do_cmd(cmd)
first=int(abs(n.pos.real)+abs(n.pos.imag))
print(f"First solution {first}")
second=int(abs(n2.pos.real)+abs(n2.pos.imag))
print(f"Second solution {second}")