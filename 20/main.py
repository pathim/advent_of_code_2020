from collections import defaultdict
from itertools import chain
from operator import mul
from functools import reduce

class Tile:
	def __init__(self,tile_id,data):
		self.id=tile_id
		self.data=data
		top=data[0]
		bottom=data[-1]
		dT=[''.join(x) for x in zip(*data)]
		left=dT[0]
		right=dT[-1]
		edges=(top,bottom,left,right)
		reverse_edges=tuple(''.join(reversed(x)) for x in edges)
		self.edges=edges+reverse_edges
	def get_opposite_edge(self,edge):
		idx=self.edges.index(edge)
		if idx%2==0:
			return self.edges[idx+1]
		else:
			return self.edges[idx-1]
	def set_neighbours(self,tiles,edgemap):
		self.neighbours=dict()
		for edge in self.edges:
			other=[x for x in edgemap[edge] if x!=self.id]
			if not other:
				nb=None
			else:
				nb=tiles[other[0]]
			self.neighbours[edge]=nb
	def num_neighbours(self):
		return len({x for x in self.neighbours.values() if x})
	def get_right(self,edge=None):
		dirmap={0:3,1:2,2:0,3:1,4:2,5:3,6:1,7:0}
		if not edge:
			edge=self.orientation
		idx=self.edges.index(edge)
		return self.edges[dirmap[idx]]

def read_single_tile(f):
	try:
		header=next(f).strip()
	except StopIteration:
		return None
	tile_id=int(header.split(' ')[1][:-1])
	data=[]
	for l in chain(f,['']):
		l=l.strip()
		if not l:
			return Tile(tile_id,data)	
		data.append(l)

def read_tiles(f):
	while True:
		if tile:=read_single_tile(f):
			yield tile
		else:
			return

def build_down(start_tile,tiles,edgemap):
	current_tile=start_tile
	bottom=current_tile.get_opposite_edge(current_tile.orientation)
	res=[current_tile]
	while current_tile:=current_tile.neighbours[bottom]:
		bottom=current_tile.get_opposite_edge(bottom)
		res.append(current_tile)
	return res
	
	
edgemap=defaultdict(list)
with open('ex') as f:
	tiles={tile.id:tile for tile in read_tiles(f)}
for tile_id,tile in tiles.items():
	for e in tile.edges:
		edgemap[e].append(tile_id)
for tile in tiles.values():
	tile.set_neighbours(tiles,edgemap)
corners=[t for t in tiles.values() if t.num_neighbours()==2]
first=reduce(lambda a,b:b.id*a,corners,1)
print(f"First solution {first}")

top_left=corners[0]
for bottom in (edge for edge,tile in top_left.neighbours.items() if tile):
	top_left.orientation=top_left.get_opposite_edge(bottom)
	if top_left.neighbours[top_left.get_right()]:
		break
cols=[build_down(top_left,tiles,edgemap)]
while tile:=cols[-1][0].neighbours[cols[-1][0].get_right()]:
	tile.orientation=tile.get_right(cols[-1][0].get_right())
	cols.append(build_down(tile,tiles,edgemap))