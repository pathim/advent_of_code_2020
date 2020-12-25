import itertools

def transform(subject,loop_size):
	value=1
	for _ in range(loop_size):
		value*=subject
		value%=20201227
	return value

def find_key(val):
	value=1
	for ls in itertools.count(1):
		value*=7
		value%=20201227
		if value==val:
			return ls

with open('input') as f:
	pubkey1=int(next(f).strip())
	pubkey2=int(next(f).strip())
first=transform(pubkey2,find_key(pubkey1))
print(f"First solution {first}")