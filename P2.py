#!/usr/bin/env python3

# Finds the sum of even-valued terms in the fibonacci sequence below 4 million
def main():
	prev = 1
	current = 2
	i = 0
	total = 0

	while(current < 4000000):
		if(current % 2 == 0):
			total += current 
		i = current
		current = current + prev
		prev = i

	print(total)

if __name__ == "__main__":
    main()