# Assuming N is an integer
def largestPalindrome(n):
	# Set upper and lower limits depending on the number of digits N
	upper_limit = (10**n) - 1
	lower_limit = 10**(n-1)

	# Track
	max_palindrome = 0

	# Loop through from the max to the min, calculating the max possible palindrome
	for i in range(upper_limit, lower_limit, -1):
		for j in range(i, lower_limit, -1):
			product = i * j
			# End the loop if the remaining numbers won't be greater than our current max
			if (product < max_palindrome):
				break
			# Set variables and begin reversing current product to see if it's a palindrome
			temp = product
			reverse = 0

			while (temp):
				reverse = reverse * 10 + temp % 10
				temp = temp // 10
			if (product == reverse and product > max_palindrome):
				max_palindrome = product

	return max_palindrome

n = 3
print(largestPalindrome(n))