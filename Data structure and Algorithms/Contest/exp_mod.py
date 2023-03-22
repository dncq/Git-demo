import sys
def power(x, y, p = 1e9 + 7) :
	res = 1	 
	x = x % p
	
	if (x == 0) :
		return 0

	while (y > 0) :
	
		if ((y & 1) == 1) :
			res = (res * x) % p

		y = y >> 1	 
		x = (x * x) % p
		
	return res
	
def Input():
    [a,b] = [int(x) for x in sys.stdin.readline().split()]
    return a,b

a,b = Input()
print('%.0f' % power(a,b))
