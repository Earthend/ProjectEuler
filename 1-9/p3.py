#!/usr/bin/env python3

import math
 
# Finds the largest prime factors of a given number n 
def primeFactors(n):
    factors = []
    remaining = n
    while(remaining % 2 == 0):
        factors.append(2)
        remaining = remaining / 2
    for i in range(3,int(math.sqrt(remaining))+1,2):
        while(remaining % i == 0):
            factors.append(i)
            remaining = remaining / i
    if(remaining > 2):
        factors.append(remaining)
    return factors


def main():
    n = 600851475143
    print(primeFactors(n))

if __name__ == "__main__":
    main()
