# def expmod(a,b, mod = 1e9 + 7):
#     res = ((a**(b/2))%mod) * ((a**(b/2))%mod) 
#     return res
# a,b = input().split()
# print('%.0f' %expmod(int(a), int(b)))

# d = {}
# def fast_exp(a,b, mod = 1e9 + 7):
#     if b == 0 or a == 1:
#         d[(a,b)] = 1
#     if (a,b) not in d:
#         d[(a,b)] = (a * fast_exp(a,b-1))
#     return d[(a,b)] %mod

# print(fast_exp(10,20))

# Iterative Python3 program
# to compute modular power

# Iterative Function to calculate
# (x^y)%p in O(log y)
def power(x, y, p) :
	res = 1	 # Initialize result

	# Update x if it is more
	# than or equal to p
	x = x % p
	
	if (x == 0) :
		return 0

	while (y > 0) :
		
		# If y is odd, multiply
		# x with result
		if ((y & 1) == 1) :
			res = (res * x) % p

		# y must be even now
		y = y >> 1	 # y = y/2
		x = (x * x) % p
		
	return res
	

# Driver Code

x = 203   ; y = 10929093034; p = 1e9+7
print("Power is ", power(x, y, p))


# This code is contributed by Nikita Tiwari.
