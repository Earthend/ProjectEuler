#!usr/bin/env python3

def nthFib(n):
    index = 3
    prev = 1
    curr = 2
    while len(str(curr)) < n:
        temp = curr
        curr += prev
        prev = temp
        index += 1
    print(index)

if __name__ == "__main__":
    nthFib(1000)