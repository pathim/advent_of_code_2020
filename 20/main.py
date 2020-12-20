from collections import defaultdict
from itertools import chain
from operator import mul
from functools import reduce

def read_single_tile(f):
	try:
		header=next(f).strip()
	except StopIteration:
		return None
	tile_id=int(header.split(' ')[1][:-1])
	top=None
	bottom=None
	left=''
	right=''
	for l in chain(f,['']):
		l=l.strip()
		if not top:
			top=l
		if not l:
			bottom=last
			edges=(top,bottom,left,right)
			reverse_edges=tuple(''.join(reversed(x)) for x in edges)
			all_edges=tuple(int(x.replace('.','0').replace('#','1'),2) for x in edges+reverse_edges)
			return (tile_id,all_edges)
		left+=l[0]
		right+=l[-1]
		last=l
	

def read_tiles(f):
	while True:
		if tile:=read_single_tile(f):
			yield tile
		else:
			return
	
def find_corners(em):
	tilemap=defaultdict(int)
	for tiles in em.values():
		if len(tiles)!=1:
			continue
		tilemap[tiles[0]]+=1
	corners=[]
	for tile,count in tilemap.items():
		if count==4:
			corners.append(tile)
	return corners

def is_outer(edgemap,edge):
	return len(edgemap[edge])==1

edgemap=defaultdict(list)
with open('input') as f:
	tiles={tile_id:edges for tile_id,edges in read_tiles(f)}
for tile_id,edges in tiles.items():
	for e in edges:
		edgemap[e].append(tile_id)
first=reduce(mul,find_corners(edgemap))

print(f"First solution {first}")