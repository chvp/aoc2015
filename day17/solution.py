#!/usr/bin/env python3

import sys
from itertools import product

if __name__ == '__main__':
    sizes = []
    with open(sys.argv[2]) as inp:
        for line in inp:
            sizes.append(int(line.strip()))
    count = 0
    minused = len(sizes), 0
    for used in product((0, 1), repeat=len(sizes)):
        if sum(s * b for s, b in zip(sizes, used)) == 150:
            count += 1
            if sum(used) < minused[0]:
                minused = sum(used), 1
            elif sum(used) == minused[0]:
                minused = minused[0], minused[1] + 1
    if int(sys.argv[1]) == 1:
        print(count)
    else:
        print(minused[1])
