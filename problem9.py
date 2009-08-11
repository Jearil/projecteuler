#!/usr/bin/python

a = 1
b = 2
c = 997

while(a < 332):
	while(b < c):
		if(a**2 + b**2 == c**2):
			print "Found it: " + str(a * b * c)
			print "a=" + str(a) + " b=" + str(b) + " c=" + str(c)
			exit()
		b = b + 1
		c = c - 1
	a += 1
	b = a + 1
	c = 1000 - (a + b)