#!/usr/bin/env python3

# Finding a pythagorean triplet - the rules of them are:
# a < b < c
# a^2 + b^2 = c^2

# Some noteworthy properties to consider when programming a better solution: 
# - Exactly one of a, b is divisible by 2 (is even), but never c.
# - Exactly one of a, b is divisible by 3, but never c.
# - The largest number that always divides abc is 60


# Crude solution:
def findTripletProduct(n):
	for a in range(2, n//3):
		for b in range(a+1, n//2):
			c = n - a - b
			if (a**2 + b**2 == c**2):
				return a*b*c

def main():
	n = 1000
	print(findTripletProduct(1000))

if __name__ == "__main__":
    main()