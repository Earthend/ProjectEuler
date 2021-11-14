#!usr/bin/env python3
import math

# Problem: 
# Find the total amount of paths in a grid if one can only go down or right

# Calculate the total combinations possible.
# e.g. If there are 4 squares (2x2), there's only 2 to choose.
# Thus n = 4 and r = 2, we get C(4, 2) = 6
def countPaths(n):
	objects = n * 2
	return int(math.factorial(objects) / (math.factorial(n) * math.factorial(objects - n)))

# Use pascal's triangle since it's an N x N grid.
# def countPaths(n):
# 	grid = [ [1] ]
#	total = 2
# 	# Loop for the first half of the square; calculate the initial
# 	# growing Pascal Triangle
# 	for i in range(1, n):
# 		row = [ 1 ]
# 		for j in range(1, i):
# 			value = grid[i-1][j-1] + grid[i-1][j]
# 			total += value
# 			row.append(value)
# 		row.append(1)
# 		grid.append(row)
# 		total += 2
# 	for i in range(n, n*2-1):
# 		row = [ ]
# 		for j in range(1, len(grid[i-1])):
# 			value = grid[i-1][j-1] + grid[i-1][j]
# 			total += value
# 			row.append(value)
# 		grid.append(row)
# 	for i in grid:
# 	return total


if __name__ == "__main__":
	print(countPaths(20))
