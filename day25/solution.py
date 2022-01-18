#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        gr, gc = [int(s[:4]) for s in inp.read().strip().split() if s[0].isdigit()]
    
    r, c = 1, 1
    num = 20151125
    while r != gr or c != gc:
        if r == 1:
            r, c = c + 1, 1
        else:
            r, c = r - 1, c + 1
        num = (num * 252533) % 33554393

    print(num)
