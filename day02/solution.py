#!/usr/bin/env python3

import sys

def paper_needed(l, w, h):
    areas = (l * w, w * h, h * l)
    return 2 * sum(areas) + min(areas)

def ribbon_needed(l, w, h):
    perimeters = (l + w, w + h, h + l)
    return 2 * min(perimeters) + l * w * h

if __name__ == '__main__':
    function = paper_needed if int(sys.argv[1]) == 1 else ribbon_needed
    total = 0
    with open(sys.argv[2]) as inp:
        for line in inp:
            total += function(*map(int, line.strip().split('x')))
    print(total)
