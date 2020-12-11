def check(s):
	needed=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
	found=[x in s for x in needed]
	return all(found)

def check_with_values(s):
	if not check(s): return False
	try:
		if not 1920<=int(s['byr'])<=2002: return False
		if not 2010<=int(s['iyr'])<=2020: return False
		if not 2020<=int(s['eyr'])<=2030: return False
		if s['hgt'][-2:]=="cm":
			if not 150<=int(s['hgt'][:-2])<=193: return False
		elif s['hgt'][-2:]=="in":
			if not 59<=int(s['hgt'][:-2])<=76: return False
		else:
			return False
		if s['hcl'][0]!='#': return False
		if len(s['hcl'])!=7: return False
		if not all(x in '0123456789abcdef' for x in s['hcl'][1:]): return False
		if not s['ecl'] in ["amb","blu", "brn","gry","grn","hzl","oth"]: return False
		if not len(s['pid'])==9: return False
		if not all(x in '0123456789' for x in s['pid']): return False
		return True
	except:
		return False


count=0
count_with_values=0
with open('input') as f:
	current=dict()
	for line in f:
		line=line.strip()
		if not line:
			if check(current):
				count+=1
			if check_with_values(current):
				count_with_values+=1
			current=dict()
			continue
		fields=line.split(' ')
		for f in fields:
			n,v=f.split(':')
			current[n]=v
	if check(current):
		count+=1
	if check_with_values(current):
		count_with_values+=1
print(f"First solution {count}")
print(f"Second solution {count_with_values}")
