#!usr/bin/env python3

def sumDiagonals(n):
    num = list(range(1, n*n + 1))
    index = 0
    total = 1
    numbers_added = 1
    corner_count = 1
    layer = 1
    while numbers_added < n * 2 - 1:
        index += 2 * layer
        total += num[index]
        numbers_added += 1
        corner_count += 1
        if corner_count > 4:
            corner_count = 1
            layer += 1
    print(total)



if __name__ == "__main__":
    sumDiagonals(1001)