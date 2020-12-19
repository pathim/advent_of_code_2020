class Rule_Lit:
	def __init__(self,char):
		self.char=char
	def to_regex(self,rules):
		return self.char
class Rule_Cat:
	def __init__(self,rule_list):
		self.rule_list=rule_list
	def to_regex(self,rules):
		return ''.join(rules[r].to_regex(rules) for r in self.rule_list)
class Rule_Or:
	def __init__(self,rule_cat1,rule_cat2):
		self.c1=rule_cat1
		self.c2=rule_cat2
	def to_regex(self,rules):
		regex1=self.c1.to_regex(rules)
		regex2=self.c2.to_regex(rules)
		return f"({regex1}|{regex2})"

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
	import re
	rule0=re.compile(rules[0].to_regex(rules))
	return sum(1 for x in f if rule0.fullmatch(x.strip()))

with open('input') as f:
	rules=read_rules(f)
	first=check_data(f,rules)
print(f"First solution {first}")