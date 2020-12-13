from functools import reduce
from operator import mul

def extended_euclid(a,b): #From wikipedia
	if b==0: return (a,1,0)
	d1,s1,t1=extended_euclid(b, a%b)
	d,s,t=d1,t1,s1-(a//b)*t1
	return (d,s,t)

def chinese_remainder(a,m):
	M=reduce(mul,m,1)
	Mi=[M//x for x in m]
	e=[extended_euclid(m,mi)[2]*mi for m,mi in zip(m,Mi)]
	ae=[aa*ee for aa,ee in zip(a,e)]
	res=sum(ae)
	if res<0:
		res+=-(res//M)*M
	return res


def schedule2rem(sched):
	busses=[int(x) if x!='x' else None for x in sched.split(',')]
	rem_des=[(x-i)%x for i,x in enumerate(busses) if x]
	return [x for x in busses if x],rem_des

with open('input') as f:
	earliest=int(next(f).strip())
	sched=next(f).strip()
	busses,rem_des=schedule2rem(sched)

wait_times=[x-(earliest%x) for x in busses]
min_time=min(wait_times)
min_bus=busses[wait_times.index(min_time)]

def find_time(start, step, factor, rem_des):
	num=start
	while num%factor!=rem_des:
		num+=step
	return num

def solve_second(busses,rem_des):
	start=0
	step=1
	for b,r in zip(busses,rem_des):
		start=find_time(start,step,b,r)
		step*=b
	return start

first=min_time*min_bus
print(f"First solution {first}")
second=chinese_remainder(rem_des,busses)
second=solve_second(busses,rem_des)
print(f"Second solution {second}")