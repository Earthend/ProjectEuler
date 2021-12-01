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
    data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    data = [[int(x) for x in line.split()] for line in data.split('\n')]
    print(greedyCrawl(data))