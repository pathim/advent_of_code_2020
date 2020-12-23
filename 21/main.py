def read_line(line:str):
	line=line.strip().split(' (contains ')
	ingredients=set(line[0].strip().split(' '))
	if len(line)>1:
		allergens=set(line[1][:-1].split(', '))
	else:
		allergens=None
	return (ingredients,allergens)

possible_allergens=dict()
possible_ingredients=dict()
all_ingredients=set()
data=list()
with open('input') as f:
	for line in f:
		ingredients,allergens=read_line(line)
		all_ingredients.update(ingredients)
		data.append((ingredients,allergens))
		if not allergens:
			continue
		for a in allergens:
			i=possible_ingredients.get(a,ingredients.copy())
			i.intersection_update(ingredients)
			possible_ingredients[a]=i

free_ingredients=all_ingredients.copy()
for i in possible_ingredients.values():
	free_ingredients.difference_update(i)

first=sum(len(d[0].intersection(free_ingredients)) for d in data)
print(f"First solution {first}")

finished=False
while not finished:
	finished=True
	for allergen,ingredients in possible_ingredients.items():
		if len(ingredients)==1:
			for a,i in possible_ingredients.items():
				if a==allergen:
					continue
				i.difference_update(ingredients)
		else:
			finished=False

sorted_allergens=sorted(possible_ingredients)
sorted_ingredients=[next(iter(possible_ingredients[x])) for x in sorted_allergens]
second=','.join(sorted_ingredients)
print(f"Second solution {second}")