#!/usr/bin/env python
from subprocess import call

def main():
	count = 120
	if(count == 120):
		call('git stash', shell = True)
		call('git pull', shell = True)
		call('git stash pop', shell = True)
		call('git commit -am "updating data"', shell = True)
		call('git push', shell = True)
		count = -1
	count += 1

if __name__=="__main__":
	main()
