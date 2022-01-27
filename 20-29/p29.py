#!usr/bin/env python3

# Brute force getting the count of distinct terms

def distinctPowers(low, high):
    terms = set()
    for a in range(low, high+1):
        for b in range(low, high+1):
            terms.add(a ** b)
    print(len(terms))

if __name__ == "__main__":
    distinctPowers(2, 100)