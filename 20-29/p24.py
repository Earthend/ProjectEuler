#!usr/bin/env python3
import math

# Calculates the millionth lexicographic value of the range 0-9
def main():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    answer = ""
    possibilities = 10**6-1
    for i in range(1, 11):
        digit = math.floor(possibilities/math.factorial(10-i))
        answer += str(numbers[digit])
        numbers.pop(digit)
        possibilities -= (digit * math.factorial(10-i))
    print(answer)


if __name__ == "__main__":
    main()


# 10! possibilities, so find the 9! to figure out  first digit
# floor((10^6 - 1)/9!) for first digit
# subtract the possibilities covered by the digit from the remaining possibilities
# loop