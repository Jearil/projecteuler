x = 999
y = 999
z = x * y
ax = 0
ay = 0
answer = 0


def ispali(n):
	zstring = '%(z)03d' % {'z': n}
	result = 0;
	for x in range(len(zstring)):
		if(zstring[x] != zstring[-x - 1]):
			result = result + 1;
	return result;

def findNextPali(x, y):
	z = x * y
	result = ispali(z)
	while (result != 0):
		x = x - 1
		z = x * y
		result = ispali(z)
	return z, x, y


while(y > 0):
	x = 999;
	y = y - 1;
	temp, tx, ty = findNextPali(x, y)
	if(temp > answer):
		answer = temp
		ax = tx
		ay = ty
	
print '%(#)03d is a Palidrome' % {'#': answer}
print 'x = %(#)03d' % {'#': ax}
print 'y = %(#)03d' % {'#': ay}