sq = 0
ss = 0
for i in range(1, 101):
	sq += i * i
	ss += i

ss = ss * ss
print "Answer: " + str(ss - sq)