#!/usr/bin/env python3

import sys

def nice1(s):
    if ("ab" in s) or ("cd" in s) or ("pq" in s) or ("xy" in s):
        return False
    vowels = 0
    twice = False
    for i, c in enumerate(s):
        if c in "aeiou":
            vowels += 1
        if i < len(s) - 1 and c == s[i + 1]:
            twice = True
    return vowels >= 3 and twice

def nice2(s):
    pair = False
    repeat = False
    for i, c in enumerate(s):
        if i < len(s) - 1 and (c + s[i + 1]) in s[i+2:]:
            pair = True
        if i < len(s) - 2 and c == s[i + 2]:
            repeat = True
    return pair and repeat

if __name__ == '__main__':
    nice = nice1 if int(sys.argv[1]) == 1 else nice2
    counter = 0
    with open(sys.argv[2]) as inp:
        for line in inp:
            counter += 1 if nice(line.strip()) else 0
    print(counter)

