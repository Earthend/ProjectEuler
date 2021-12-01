#!usr/bin/env python3


# Crawls through the triangle from the bottom to the top and each node
# takes the max of their leaf nodes, slowly building the max value 
# of the best path.
def greedyCrawl(triangle):
    depth = len(triangle) - 2
    for level in range(depth, -1, -1):
        for pos in range(0, len(triangle[level])):
            triangle[level][pos] += max(triangle[level+1][pos], triangle[level+1][pos+1])
    return triangle[0][0]

if __name__ == "__main__":
    lines = []
    with open("./p067_triangle.txt", 'r') as f:
        lines = f.readlines()
    data = [[int(x) for x in line.split()] for line in lines]
    print(greedyCrawl(data))