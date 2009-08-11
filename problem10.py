from math import sqrt

primes = [2, 3]
psum = 5

def isPrime(n):
	sqrn = sqrt(n)
	for x in primes:
		if(x > sqrn):
			return True
		if(num % x == 0):
			return False
	return True

# for i in range(2, 2000000):
while (primes[-1] < 2000000):
	num = primes[-1] + 2
	while(not isPrime(num)):
		num += 2
	primes.append(num)
	psum += num

print "The last prime is: " + str(primes[-1])
print "second to last: " + str(primes[-2])
psum -= primes[-1] # Last number will be above 2000000 so remove it
print "The sum of all primes below 2 million is " + str(psum)