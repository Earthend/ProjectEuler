#!usr/bin/env python3

powers = []
for i in range(0, 10):
    powers.append(i ** 5)

def sumPowers(n):
    total = 0
    while n > 0:
        total += powers[n % 10]
        n = int(n // 10)
    return total 

def fifthPowers(upper):
    total = 0
    for i in range(2, upper + 1):
        if i == sumPowers(i):
            total += i
    print(total)


if __name__ == "__main__":
    # 10 ^ d-1 <= d * 9^5 < 10^d
    # At most 6 digits, so the upper bound can be 6 * 9 ^ 5 = 354294
    fifthPowers(354294)