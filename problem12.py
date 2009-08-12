#!/usr/bin/python
from math import sqrt

def countDivisors(t):
	count = 0
	sqrn = int(sqrt(t))
	for j in range(1, sqrn):
		if (t % j == 0):
			if (t == j):
				count += 1
			else:
				count += 2
	return count

terms = 0
i = 1
found = False

while(found == False):
	terms += i
	if(i > 500):
		if(countDivisors(terms) > 500):
			found = True
	i += 1

print "Term found: " + str(terms)
