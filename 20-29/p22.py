#!usr/bin/env python3
import string

def nameScores(path):
    file = open(path, 'r')
    names = file.read().replace('"','').split(",")
    names.sort()
    total = 0
    index = 1
    for name in names:
        score = 0
        for char in name:
            score += string.ascii_uppercase.index(char) + 1
        score *= index
        total += score
        index += 1
    return total

if __name__ == "__main__":
    print(nameScores('p022_names.txt'))