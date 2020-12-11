def decode_bin(val,chars):
	val=val.replace(chars[0],'0')
	val=val.replace(chars[1],'1')
	return int(val,2)
	
def decode_line(line):
	row_raw=line[:-3]
	col_raw=line[-3:]
	row=decode_bin(row_raw,'FB')
	col=decode_bin(col_raw,'LR')
	return (row,col)
	
def get_id(row,col):
	return 8*row+col
	
with open('input') as f:
	ids=[get_id(*decode_line(l.strip())) for l in f]
first=max(ids)
ids.sort()
diff=[x-y for x,y in zip(ids[1:],ids)]
second=ids[diff.index(2)]+1
print(f"First solution {first}")
print(f"Second solution {second}")
		