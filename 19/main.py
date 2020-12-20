import re

class Rule_Lit:
	def __init__(self,char):
		self.char=char
	def to_regex(self,rules):
		return self.char
	def __repr__(self):
		return self.char
class Rule_Cat:
	def __init__(self,rule_list):
		self.rule_list=rule_list
	def to_regex(self,rules):
		return ''.join(rules[r].to_regex(rules) for r in self.rule_list)
	def __repr__(self):
		return f'Cat({self.rule_list})'
class Rule_Or:
	def __init__(self,rule_cat1,rule_cat2):
		self.c1=rule_cat1
		self.c2=rule_cat2
	def to_regex(self,rules):
		regex1=self.c1.to_regex(rules)
		regex2=self.c2.to_regex(rules)
		return f"({regex1}|{regex2})"
	def __repr__(self):
		return f"Or({self.c1},{self.c2})"

def parse_rule(rule):
	if rule[0]=='"':
		return Rule_Lit(rule[1])
	elif '|' in rule:
		r1,r2=rule.split(" | ")
		return Rule_Or(parse_rule(r1),parse_rule(r2))
	else:
		return Rule_Cat([int(x) for x in rule.split(' ')])

def read_rules(f):
	rules=dict()
	for l in f:
		l=l.strip()
		if not l:
			return rules
		number,rule=l.split(': ')
		rules[int(number)]=parse_rule(rule)

def check_data(f,rules):
	rule0=re.compile(rules[0].to_regex(rules))
	return sum(1 for x in f if rule0.fullmatch(x.strip()))

def count_matches(r,s):
	idx=0
	res=0
	while True:
		m=r.match(s[idx:])
		if not m:
			return res,s[idx:]
		idx+=m.end()
		res+=1
	return
	
def check_data2(f,rules):
	# manually build rule[0]
	# rule[8]=42 | 42 8 = 42+
	# rule[11]=42 31 | 42 11 31 =42+ 31+ (same amount of both)
	# rule[0]=8 11 = x times 42 then y times 31 with x>y
	r42=re.compile(rules[42].to_regex(rules))
	r31=re.compile(rules[31].to_regex(rules))
	result=0
	for l in f:
		x,rest=count_matches(r42,l)
		y,rest=count_matches(r31,rest)
		if rest=='' and y>0 and x>y:
			result+=1
	return result

with open('input') as f:
	rules=read_rules(f)
	lines=[l.strip() for l in f]
	first=check_data(lines,rules)
	second=check_data2(lines,rules)
print(f"First solution {first}")
print(f"Second solution {second}")
