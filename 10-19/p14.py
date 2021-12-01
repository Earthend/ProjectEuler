#!usr/bin/env python3
import math

# Finds the longest Collatz sequence under 1 mil. 
# Designed for only values of 10's
def longestCollatz(n):
	# Start with the digit just before the highest possible, with that
	# value being 8 because it is either 8 or 9 as the first digit with
	# the longest chain in range. 
	digits = int(math.log10(n))
	start = 8 * 10**(digits-1) if digits > 2 else 1
	
	longest, longest_length = 0, 0

	for number in range(start, n):
		length = 0
		i = number
		while i != 1:
			if i % 2 == 0:
				i = i / 2
			else:
				i = i * 3 + 1
			length += 1
		# Only update if it's a new longest-chain
		if max(longest_length, length) != longest_length:
			longest_length = length
			longest = number
	return longest

if __name__ == "__main__":
	print(longestCollatz(1000000))
