from itertools import product

def load_input(filename:str,dims=3) -> {(int,...)}:
	res=set()
	with open(filename) as f:
		for x,l in enumerate(f):
			for y,c in enumerate(l.strip()):
				if c=='#':
					res.add((x,y)+(0,)*(dims-2))
	return res

def get_neighbors(cell:(int,...))->{int,...}:
	dims=len(cell)
	deltas=product(*[[-1,0,1]]*dims)
	res={tuple(c+d for c,d in zip(cell,delta)) for delta in deltas}
	res.remove(cell)
	return res

def next_gen(cells:{(int,...)})->{(int,...)}:
	while True:
		nb={}
		for c in cells:
			for n in get_neighbors(c):
				try:
					nb[n]+=1
				except KeyError:
					nb[n]=1
		new_cells=set()
		for c in nb:
			active_neighbors=nb[c]
			if active_neighbors==3 or (active_neighbors==2 and c in cells):
				new_cells.add(c)
		cells=new_cells
		yield cells

def next_gens(cells:{(int,...)},n:int)->{(int,...)}:
	for x,_ in zip(next_gen(cells),range(n)):
		pass
	return x

cells=load_input('input')
first=len(next_gens(cells,6))
print(f"First solution {first}")
cells=load_input('input',dims=4)
second=len(next_gens(cells,6))
print(f"Second solution {second}")