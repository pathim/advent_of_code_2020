from itertools import count
from copy import deepcopy
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

def play_recursive(deck1,deck2):
	decks=(deck1.copy(),deck2.copy())
	history=[]
	while decks[0] and decks[1]:
		if decks in history:
			return 0,score(decks[0])
		history.append(deepcopy(decks))
		cards=[decks[0].pop(0),decks[1].pop(0)]
		if cards[0]<=len(decks[0]) and cards[1]<=len(decks[1]):
			new_decks=[decks[i][:c] for i,c in enumerate(cards)]
			winner,_=play_recursive(*new_decks)
		else:
			winner=cards.index(max(cards))
		decks[winner].append(cards.pop(winner))
		decks[winner].append(cards[0])
	if decks[0]:
		return 0,score(decks[0])
	return 1,score(decks[1])


def score(deck):
	return sum(a*b for a,b in zip(reversed(deck),count(1)))
		
with open('input') as f:
	deck1=read_deck(f)
	deck2=read_deck(f)

first=play(deck1,deck2)
print(f"First solution {first}")
_,second=play_recursive(deck1,deck2)
print(f"Second solution {second}")