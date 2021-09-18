#!/usr/bin/env python3

# Could likely improve memory by using pointers in C/C++ and creating a manually linked list.
# Transactions may be more costly though?
def get_primes(size):
	# Create a bytearray of 1's from 0 to size to reduce memory and make comparisons simple
	primes = bytearray([1] * size)
	# Begin zero-ing non-prime values in the list starting at the first prime 2
	for i in range(2, size):
		if primes[i] == 1:
			for j in range(i, size):
				if i * j < size:
					primes[i*j] = 0
				else:
					break
	return primes


def nthPrime(n):
	# Used to slowly increment the size of the potential prime values list
	# since the size is unkown
	size_multiplier = 2

	# Keeps track of the prime values so we know if we found the nth value
	total_primes = 0

	while total_primes < n:
		list_size = n * size_multiplier
		primes = get_primes(list_size)
		total_primes = sum(primes[2:])
		size_multiplier += 1
	# Now we return the nth prime
	n_value = 0
	for index in range(2, len(primes)):
		n_value += primes[index]
		if n_value == n:
			return index


def main():
	print(nthPrime(10001))

if __name__ == "__main__":
    main()