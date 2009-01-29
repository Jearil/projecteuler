primes = [2, 3]

def isPrime(n):
	for x in primes:
		if(num % x == 0):
			return False
	return True

for i in range(2, 10001):	
	num = primes[-1] + 2
	while(not isPrime(num)):
		num += 2
	primes.append(num)

print "The 10001th prime is: " + str(primes[-1])