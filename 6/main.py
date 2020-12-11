count=0
count_every=0
with open('input') as f:
	current=set()
	every_letter=set(chr(ord('a')+x) for x in range(26))
	everyone=set(every_letter)
	for line in f:
		line=line.strip()
		if not line:
			count+=len(current)
			current=set()
			count_every+=len(everyone)
			everyone=set(every_letter)
			continue
		current.update(set(line))
		everyone.intersection_update(set(line))
	count+=len(current)
	count_every+=len(everyone)
print(f"First solution {count}")
print(f"Second solution {count_every}")