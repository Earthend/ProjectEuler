#!usr/bin/env python3

# Could design better with early calculations of the number and
# more edge case checking

# Designed just for counting up to 1000
# Note: No 'u' in forty
def numberLetterSum():
	ones = [ 3, 3, 5, 4, 4, 3, 5, 5, 4] # 1 - 9
	special = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # 10 - 19
	tens = [6, 6, 5, 5, 5, 7, 6, 6] # 20 - 90
	hundreds = 10 # Just the length of "hundred and"
	first_hundred = 7 # The length of "hundred"

	# Simply computes 1-19
	base = sum(ones)
	start_total = base + sum(special)

	total = start_total
	# Calculates 20 - 99
	for i in tens:
		total += (i * 10) + base

	# Now just have to multiply the total amount of times of (___ hundred and) appearing
	# and add it with the current count.
	hundred_count = total
	for i in ones:
		total += i + first_hundred
		total += (hundreds + i) * 99 + hundred_count

	# The shebang: 1000
	total += 11
	return total

if __name__ == '__main__':
	print(numberLetterSum())