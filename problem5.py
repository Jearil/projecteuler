num = 20

while(1 == 1):
	passes = 1
	for x in range(1, 21):
		if (num % x != 0):
			passes = 0
			break
	if(passes == 1):
		print "You're looking for " + str(num);
		break
	num = num + 20
