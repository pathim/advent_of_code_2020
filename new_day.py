#!/usr/bin/env python3
import datetime
import os
import urllib.request

def check_dir(d):
	try:
		os.stat(os.path.join(d,'input'))
	except (FileNotFoundError, NotADirectoryError):
		return False
	return True

def create_day(d,cookie):
	if not os.path.exists(d):
		os.mkdir(d)
	req=urllib.request.Request(f"https://adventofcode.com/2020/day/{d}/input",headers={'Cookie':cookie})
	input_data=urllib.request.urlopen(req).read()
	with open(os.path.join(d,'input'),"wb") as f:
		f.write(input_data)

def create_all_days(year):
	today=datetime.date.today()
	day=today.day if today.year<=year else 25
	
	days=set(str(x) for x in range(1,day+1))
	dirs={x for x in os.listdir() if check_dir(x)}
	
	days.difference_update(dirs)
	
	if not days:
		return
	with open('cookie') as f:
		cookie=f.read().strip()
	for d in days:
		create_day(d,cookie)

if __name__=='__main__':
	create_all_days(2020)
