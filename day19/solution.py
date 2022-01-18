#!/usr/bin/env python3

import sys
import random

def find_e(molecule, rules, depth=0):
    if molecule == 'e':
        return depth
    molecules = set()
    for d, s in rules:
        pos = molecule.find(s)
        while pos > -1:
            molecules.add(molecule[:pos] + d + molecule[pos + len(s):])
            pos = molecule.find(s, pos + 1)
    
    for m in sorted(molecules, key=lambda _: random.random()):
        if (founddepth := find_e(m, rules, depth + 1)) is not None:
            return founddepth

    return None

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        data = inp.read()
    rules, molecule = data.split('\n\n')
    rules = tuple(map(lambda x: tuple(x.split(' => ')), rules.strip().split('\n')))
    molecule = molecule.strip()
    if int(sys.argv[1]) == 1:
        molecules = set()
        for s, d in rules:
            pos = molecule.find(s)
            while pos > -1:
                molecules.add(molecule[:pos] + d + molecule[pos + len(s):])
                pos = molecule.find(s, pos + 1)
        print(len(molecules))
    else:
        print(find_e(molecule, rules))
