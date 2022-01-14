#!usr/bin/env python3
import math

# Brute Force calculation of divisors
def sumDiv(n):
    i = 1
    total = 0
    while i <= math.sqrt(n):
        if n % i == 0:
            total += i
            if n / i != i and i != 1:
                total += (n / i)
        i+=1
    return total

# brute force find all that can't
def nonAbundantSums(n):
    abundant = set()
    for i in range(1, n):
        if sumDiv(i) > i:
            abundant.add(i)

    sums = [True] * (n+1)
    for x in abundant:
        for y in abundant:
            if x+y <= n:
                sums[x+y] = False

    total = 0
    for i in range(1, n+1):
        if sums[i]:
            total += i
    return total

if __name__ == "__main__":
    #print(nonAbundantSums(100))
    print(nonAbundantSums(28123))