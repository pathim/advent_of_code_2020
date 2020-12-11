rules=dict()
rules2=dict()

def parse_phrase(ph):
	ph=ph.split(' ')
	name=' '.join(ph[1:3])
	try:
		count=int(ph[0])
	except ValueError:
		count=0
	return name,count
	
with open('input') as f:
	for line in f:
		outer,inner=line.split(" bags contain ")
		inner=[parse_phrase(x) for x in inner.split(', ')]
		if not outer in rules:
			rules[outer]=set()
		if inner[0][1]:
			rules2[outer]=inner
		for i in inner:
			try:
				x=rules[i[0]]
			except KeyError:
				x=set()
				rules[i[0]]=x
			x.add(outer)

def traverse(tree,node):
	result=set()
	for x in tree[node]:
		result.add(x)
		result.update(traverse(tree,x))
	return result
first=len(traverse(rules,'shiny gold'))

def traverse_count(tree,node):
	try:
		n=tree[node]
	except KeyError:
		return 0
	count=0
	for a in n:
		count+= a[1]*(traverse_count(tree,a[0])+1)
	return count
		
second=traverse_count(rules2,'shiny gold')
	
print(f"First solution {first}")
print(f"Second solution {second}")