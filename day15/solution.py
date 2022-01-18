#!/usr/bin/env python3

import sys

def product(num, m=100):
    if num == 1:
        yield (m,)
    else:
        for i in range(m + 1):
            for p in product(num - 1, m - i):
                yield (i,) + p


if __name__ == '__main__':
    ingredients = []
    with open(sys.argv[2]) as inp:
        for line in inp:
            ingredients.append(tuple(int(s.split()[1]) for s in line.strip().split(': ')[1].split(', ')))
    part = int(sys.argv[1])
    m = 0
    for amounts in product(len(ingredients)):
        attrs = [0] * 5
        for i in range(len(ingredients)):
            for j in range(5):
                attrs[j] += amounts[i] * ingredients[i][j]
        val = max(attrs[0], 0) * max(attrs[1], 0) * max(attrs[2], 0) * max(attrs[3], 0)
        if val > m and (part == 1 or attrs[4] == 500):
            m = val
    print(m)
