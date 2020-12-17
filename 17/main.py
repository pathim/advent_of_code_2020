from functools import lru_cache,reduce
from itertools import product
from operator import or_,add

def load_input(filename:str,dims=3) -> {(int,...)}:
	res=set()
	with open(filename) as f:
		for x,l in enumerate(f):
			for y,c in enumerate(l.strip()):
				if c=='#':
					res.add((x,y)+(0,)*(dims-2))
	return res

@lru_cache(maxsize=None)
def get_neighbors(cell:(int,...))->{int,...}:
	dims=len(cell)
	deltas=product(*[[-1,0,1]]*dims)
	res={tuple(c+d for c,d in zip(cell,delta)) for delta in deltas}
	res.remove(cell)
	return res

def count_active(cells:set,to_count:set)->int:
	return len(cells.intersection(to_count))

def next_gen(cells:{(int,...)})->{(int,...)}:
	while True:
		candidates=reduce(or_,(get_neighbors(x) for x in cells))
		new_cells=set()
		for c in candidates:
			active_neighbors=count_active(cells,get_neighbors(c))
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