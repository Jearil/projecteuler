x = 999
y = 999
z = x * y


def pali(n):
	zstring = '%(z)03d' % {'z': n}
	result = 0;
	for x in range(len(zstring)):
		if(zstring[x] != zstring[-x - 1]):
			result = result + 1;
	return result;

result = pali(z)
while(result != 0):
	x = x - 1
	z = x * y
	result = pali(z)
	
if(result == 0):
	print '%(#)03d is a Palidrome' % {'#': z}
	print 'x = %(#)03d' % {'#': x}
	print 'y = %(#)03d' % {'#': y}
else:
	print '%(#)03d is NOT a Palidrome' % {'#': z}