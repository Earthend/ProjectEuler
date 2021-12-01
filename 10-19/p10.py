#!/usr/bin/env python3
# Uses modified 'O(n)' Sieve of Eratosthenes to find the primes

def soe(n):
    isPrime = [True] * (n+1)
    primes = []
    smallest_prime_factor = [None] * (n+1)
    # Base Case
    isPrime[0] = isPrime[1] = False

    # Loop to find remaining prime numbers
    for i in range(2, n):
        if isPrime[i] == True:
            # Puts prime into our primes array and adds itself to its associated
            # location in the 'smallest prime factor' array
            primes.append(i)
            smallest_prime_factor[i] = i
        # We now loop through the primes to remove their multiples
        # and edit their associated smallest prime factor value to match
        # so it can repeat the process at higher values, reducing overall loops
        j = 0
        while(j < len(primes) and 
                i * primes[j] < n and
                primes[j] <= smallest_prime_factor[i]):
            isPrime[i * primes[j]] = False
            smallest_prime_factor[i * primes[j]] = primes[j]
            j+=1
    return primes

if __name__ == "__main__":
    n = 2000000
    sum = 0
    primes = soe(n)
    i=0
    while i < len(primes):
        sum += primes[i]
        i+=1
    print(sum)
