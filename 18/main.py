import pyparsing as pp
from operator import add,mul

number=pp.Word(pp.nums).setParseAction(lambda t:int(t[0]))
op=pp.oneOf('+ *').setParseAction(lambda t: mul if t[0]=='*' else add)
left = pp.Literal('(').suppress()
right = pp.Literal(')').suppress()
expr=pp.Forward()
atom=number | pp.Group(left+expr+right)
expr<<=atom+pp.ZeroOrMore(op+atom)

def interpret(pr):
	if type(pr)==int:
		return pr
	while len(pr)>=3:
		op1=interpret(pr.pop(0))
		f=pr.pop(0)
		res=f(op1,interpret(pr[0]))
		pr[0]=res
	if type(pr[0])==pp.ParseResults:
		return interpret(pr[0])
	return pr[0]


with open('input') as f:
	first=sum(interpret(expr.parseString(l)) for l in f)

print(f"First solution {first}")