#!/usr/bin/env python3

# Notes: Pretty greedy algorithm since it only considers the first zeros for the special case.  
# If adjusted to track if there was a zero and the index of the last zero in the adjacents, then it would 
# be much more efficient at skipping instances.

# e.g. Fails to properly skip efficiently if the number is 10000000000001

# Best version:  Find the first sequence that includes all non-zero numbers and store that with a head and tail.
# Step one by one, dividing the previous head from the product and multiply the product by the new tail.  If there's
# a zero, we must repeat the first step of finding a sequence including all non-zero numbers, then go back to stepping.


# Finds the n-adjacent digits and their largest product that create the greatest product in an m-digit number
def largestAdjacents(number, n, m):
	# Keep track of the largest product value and the index of where it came from
	largest_product = 0
	best_adjacents = -1

	# Tracks the current digit's location to aid in moving the head & tail a set amount
	# whenever we come across a zero
	index = 0
	head = 0
	tail = n
	while tail < m:
		current_product = 1
		# Loop through the n adjacents
		for digit in number[head:tail]:
			digit = int(digit)
			# Special case: automatically skip calculations if there's a zero
			if not digit:
				difference = index - head
				head += difference
				tail += difference
				break
			current_product *= digit
			index += 1
		# Update the location of the adjacents producing the largest product
		if current_product > largest_product:
			best_adjacents = head
			largest_product = current_product
		head += 1
		tail += 1
		index = head

	return (number[best_adjacents:best_adjacents+n], largest_product)


def main():
	long_number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	digits = 13
	length = 1000
	print(largestAdjacents(long_number, digits, length))

if __name__ == "__main__":
    main()