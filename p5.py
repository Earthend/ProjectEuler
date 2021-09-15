# Puts all prime factors of a number into a dictionary (Could skip 
# adding the 1's for this problem, but I'm putting it in  
# just in case we need to import this function for later uses)

def primeFactors(n):
	# Edge case - returns 0 if it's 0
	if (not n):
		return 0
	primes = {1: 1}; current_number = n; i = 2
	while (current_number != 1):
		# If it's a prime factor, add it to the dict and reset to 2
		if (current_number % i == 0):
			current_number = current_number / i
			# Either update the value if it exists or add it to the dictionary
			if i in primes:
				primes[i] = primes[i] + 1
			else:
				primes[i] = 1
			# Reset to 2 and start looping again
			i = 2
			continue
		i = i + 1
	return primes

def smallestMultiple(n):
	# Create a dictionary of every relevant value and their prime factors
	values = {}
	# Skipping half the values since they don't matter when using Prime Factors Method
	for i in range(n // 2 + 1, n+1, 1):
		values[i] = primeFactors(i)
	# Combine the dictionaries of all values to determine the prime factors of the LCM
	final_primes = {}
	for value in values:
		for prime in values[value]:
			if prime in final_primes:
				final_primes[prime] = max(values[value][prime], final_primes[prime])
			else:
				final_primes[prime] = values[value][prime]
	# Now we multiply it all to get our final answer
	smallest_multiple = 1
	for value in final_primes:
		smallest_multiple = smallest_multiple * (value ** final_primes[value])
	return smallest_multiple



print(smallestMultiple(20))