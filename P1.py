#!/usr/bin/env python3

# Finds the sum of multiples of 3 or 5 that are below 1000
def main():
	current_num = 3
	total = 0
	while(current_num < 1000):
		if(current_num % 3 == 0 or current_num % 5 == 0):
			total += current_num
		current_num+=1
	print(total)

if __name__ == "__main__":
    main()