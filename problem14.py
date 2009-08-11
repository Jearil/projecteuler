#!/usr/bin/python

largestTerm = 0
number = 0

for x in range(999999, 333333, -2):
	y = x
	term = 1
	while(y > 1):
		if(y % 2 == 0):
			y /= 2
		else:
			y = 3 * y + 1
		term += 1
	
	if(term > largestTerm):
		largestTerm = term
		number = x

print "Largest term is " + str(largestTerm) + " starting with " + str(number)