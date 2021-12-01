#!usr/bin/env python3

# Returns the total number of divisors
def total_divisors(n):
	remaining = n
	i = 2
	total = 1
	# Base case
	if n == 1:
		return 1
	# The number of the divisors can be calculated by
	# the sum of (e_i + 1) from i=1 to k.
	while i * i <= remaining:
		count = 1
		while remaining % i == 0:
			remaining /= i
			count += 1
		i += 1
		total *= count

	if n == remaining or (remaining > 1):
		total *= 2
	return total

# Finds the first triangle number to have over N divisors
def triangle_number_dividers(n):
	next_natural = 1
	current_triangle = 1
	while total_divisors(current_triangle) <= n:
		next_natural += 1
		current_triangle += next_natural
	return current_triangle

if __name__ == "__main__":
	print(triangle_number_dividers(500))