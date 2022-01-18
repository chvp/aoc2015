#!/usr/bin/env python3

import functools
import itertools
import sys

def can_divide_three(items, expected_total):
    for n in range(len(items) // 3):
        for comb in itertools.combinations(items, n):
            if sum(comb) == expected_total and can_divide_two(items - set(comb), expected_total):
                return True
    return False

def can_divide_two(items, expected_total):
    for n in range(len(items) // 2):
        for comb in itertools.combinations(items, n):
            if sum(comb) == expected_total:
                return True
    return False

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        weights = [int(l.strip()) for l in inp]

    expected_total = sum(weights) // (3 if int(sys.argv[1]) == 1 else 4)
    can_divide = can_divide_two if int(sys.argv[1]) == 1 else can_divide_three
    for i in range(len(weights))
        for items in itertools.combinations(weights, i):
            if sum(items) == expected_total and can_divide(set(weights) - set(items), expected_total):
                print(functools.reduce(lambda x, y: x * y, items))
                sys.exit(0)

