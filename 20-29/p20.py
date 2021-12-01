#!usr/bin/env python3
import math

# Finds the sum of the digits of a value n to the power i
def sumDigits(n):
	number = math.factorial(n)
	total = 0
	for c in map(int, str(number)):
		total += c
	return total

if __name__ == "__main__":
	print(sumDigits(100))
 