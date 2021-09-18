#!/usr/bin/env python3

# Protentially a more efficient way to do this?
def sumSquareDiff(n):
	sum_of_squares = 0
	square_of_sums = 0
	# Calculate both during this single loop
	for i in range(1, n+1, 1):
		sum_of_squares = sum_of_squares + (i ** 2)
		square_of_sums = square_of_sums + i
	square_of_sums = square_of_sums ** 2
	return  square_of_sums - sum_of_squares


def main():
	print(sumSquareDiff(100))

if __name__ == "__main__":
    main()