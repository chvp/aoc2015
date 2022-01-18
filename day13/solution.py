#!/usr/bin/env python3

import sys
import itertools

if __name__ == '__main__':
    modifiers = {}
    names = set()
    with open(sys.argv[2]) as inp:
        for line in inp:
            ws = line.strip().split()
            modifiers[(ws[0], ws[-1][:-1])] = int(ws[3]) if ws[2] == "gain" else -int(ws[3])
            names.add(ws[0])
    if int(sys.argv[1]) == 1:
        print(max(sum(modifiers[n1, n2] + modifiers[n2, n1] for n1, n2 in zip(p, p[-1:] + p[:-1])) for p in itertools.permutations(names)))
    else:
        print(max(sum(modifiers[n1, n2] + modifiers[n2, n1] for n1, n2 in zip(p, p[1:])) for p in itertools.permutations(names)))

