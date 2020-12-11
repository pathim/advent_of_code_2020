def checkpw1(letter,count_min,count_max,password):
	if count_min<=password.count(letter)<=count_max:
		return True
	return False

def checkpw2(letter,count_min,count_max,password):
	strget=lambda s,i:s[i] if len(s)>i else ''
	if (strget(password,count_min-1)==letter)^(strget(password,count_max-1)==letter):
		return True
	return False

def split_pw(line):
	pol,pw=line.split(': ',1)
	letter=pol[-1]
	count_min,count_max=(int(x) for x in pol[:-2].split('-'))
	return letter,count_min,count_max,pw

count1=0
count2=0
with open('input') as f:
	for line in f:
		s=split_pw(line)
		count1+=checkpw1(*s)
		count2+=checkpw2(*s)
print(f"First solution: {count1}")
print(f"Second solution: {count2}")

