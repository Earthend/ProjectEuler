#!usr/bin/env python3

def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i+=1
    return True


def main(n):
    highest = 0
    highest_a = 0
    highest_b = 0

    for a in range(-n, n):
        for b in range(-n, n):
            count = 0
            while isPrime(count * count + count * a +  b):
                count += 1
            if count > highest:
                highest = count
                highest_a = a
                highest_b = b
    print("A: ", highest_a, " B: ", highest_b, " Product: ", (highest_a * highest_b))


if __name__ == "__main__":
    main(1000)