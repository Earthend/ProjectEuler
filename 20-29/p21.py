#!usr/bin/env python3
import math

# Brute Force calculation of divisors
def sumDiv(n):
	i = 1
	total = 0
	while i <= math.sqrt(n):
		if n % i == 0:
			total += i
			if n / i != i and i != 1:
				total += (n / i)
		i+=1
	return total

# Finds the sum of all the amicable numbers under the value n
# Improve by adding memoization
def sumAmicable(n):
	checked = set()
	total = 0
	for a in range(1, n):
		if a not in checked:
			checked.add(a)
			b = int(sumDiv(a))
			if a != b and int(sumDiv(b)) == a:
				checked.add(b)
				total += a + b
	return total


if __name__ == "__main__":
	print(sumAmicable(10000))
 