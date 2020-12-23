from itertools import count
def read_deck(f):
	deck=[]
	next(f) # Skip header
	for l in f:
		l=l.strip()
		if not l:
			break
		deck.append(int(l))
	return deck

def play_round(deck1,deck2):
	c1=deck1.pop(0)
	c2=deck2.pop(0)
	if c1>c2:
		deck1.extend([c1,c2])
	else:
		deck2.extend([c2,c1])

def play(deck1,deck2):
	d1=deck1.copy()
	d2=deck2.copy()
	while d1 and d2:
		play_round(d1,d2)
	return max(score(d1),score(d2))

def score(deck):
	return sum(a*b for a,b in zip(reversed(deck),count(1)))
		
with open('input') as f:
	deck1=read_deck(f)
	deck2=read_deck(f)

first=play(deck1,deck2)
print(f"First solution {first}")