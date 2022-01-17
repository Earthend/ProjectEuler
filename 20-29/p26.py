#!usr/bin/env python3

def longestCycle(d):
    length = 0
    value = 0
    for i in range(d, 1, -1):
        if length > i:
            break
        remainders = [0] * i
        digit = 1
        position = 0
        while remainders[digit] == 0 and digit != 0:
            remainders[digit] = position
            digit *= 10
            digit %= i
            position += 1

        if (position - remainders[digit]) > length:
            length = position - remainders[digit]
            value = i
    print(length, value)


if __name__ == "__main__":
    longestCycle(1000)