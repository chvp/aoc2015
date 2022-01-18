#!/usr/bin/env python3

import sys
import itertools

if __name__ == '__main__':
    distances = {}
    all_cities = set()
    with open(sys.argv[2]) as inp:
        for line in inp:
            cities, distance = line.strip().split(' = ')
            c1, c2 = cities.split(' to ')
            distances[(c1, c2)] = int(distance)
            distances[(c2, c1)] = int(distance)
            all_cities.add(c1)
            all_cities.add(c2)
    generator = (sum(distances[m] for m in zip(p, p[1:])) for p in itertools.permutations(all_cities))
    if int(sys.argv[1]) == 1:
        print(min(generator))
    else:
        print(max(generator))
