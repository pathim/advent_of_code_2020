import numpy as np
from scipy.signal import convolve2d
from scipy.sparse import coo_matrix

def load_input(filename='input'):
	data=[]
	with open(filename) as f:
		for l in f:
			l=[True if x=='L' else False for x in l.strip()]
			data.append(l)
	return np.array(data)
	
def update(state,seat_map):
	kernel=np.array([[1]*3,[1,0,1],[1]*3])
	c=convolve2d(state,kernel,'same')
	state=state.copy()
	state[c>=4]=0
	state[(c==0)&(seat_map)]=1
	return state
	
def find_next_seat(seatmap,pos,direction):
	pos=np.array(pos)
	while True:
		pos+=direction
		if (pos<0).any():return None
		try:
			if seatmap[pos[0],pos[1]]:
				return tuple(pos)		
		except IndexError:
			return None
			
def check_dir(state,seatmap,pos,direction):
	pos=pos.copy()
	while True:
		pos+=direction
		if (pos<0).any():
			return False
		try:
			if not seat_map[pos[0],pos[1]]:
				continue
			if state[pos[0],pos[1]]:
				return True
			return False
		except IndexError:
			return False
	
def get_visible_seats(seatmap,pos):
	dirs=[(x,y) for x in range(-1,2) for y in range(-1,2) if x or y]
	return {x for x in [find_next_seat(seatmap,pos,d) for d in dirs] if x}
	
def prepare_line_of_sight(seatmap):
	res=dict()
	count=0
	for y in range(seatmap.shape[0]):
		for x in range(seatmap.shape[1]):
			pos=(y,x)
			if not seatmap[pos]:
				continue
			res[pos]=(count,get_visible_seats(seatmap,pos))
			count+=1
	return res
	
def los2mat(los):
	size=len(los)
	#res=np.zeros((size,size))
	row=[]
	col=[]
	data=[]
	for pos in los:
		for v in los[pos][1]:
			row.append(los[v][0])
			col.append(los[pos][0])
			data.append(1)
			#res[los[v][0],los[pos][0]]=1
	res=coo_matrix((data,(row,col)),shape=(size,size))
	return res
	
	
def count_visible_slow(state,seat_map):
	dirs=[(x,y) for x in range(-1,2) for y in range(-1,2) if x or y]
	c=np.zeros_like(state)
	height,width=state.shape
	for y in range(height):
		for x in range(width):
			if not seat_map[y,x]:
				continue
			pos=np.array((y,x))
			c[y,x]=sum(check_dir(state,seat_map,pos,d) for d in dirs)
	return c

def count_visible(state,seat_map,los):
	c=np.zeros_like(state)
	height,width=state.shape
	for y in range(height):
		for x in range(width):
			if not seat_map[y,x]:
				continue
			pos=(y,x)
			c[pos]=sum(state[v] for v in los[pos][1])
	return c

def update2(state,seat_map,los):
	c=count_visible(state,seat_map,los)
	state=state.copy()
	state[c>=5]=0
	state[(c==0)&(seat_map)]=1
	return state
	
def update_matrix(state,m):
	c=m@state
	state=state.copy()
	state[c==0]=1
	state[c>=5]=0
	return state
	
def render(state,seat_map):
	im=np.zeros_like(state,str)
	im[state==0]='L'
	im[state!=0]='#'
	im[seat_map==False]='.'
	for x in im:
		print(''.join(x))

seat_map=load_input('input')
state=np.zeros_like(seat_map,dtype=int)
while True:
	new_state=update(state,seat_map)
	if (new_state==state).all():
		break
	state=new_state
first=state.sum()
print(f"First solution {first}")

los=prepare_line_of_sight(seat_map)
mat=los2mat(los)
state=np.zeros(mat.shape[1])
while True:
	new_state=update_matrix(state,mat)
	if (new_state==state).all():
		break
	state=new_state
second=int(state.sum())
print(f"Second solution {second}")