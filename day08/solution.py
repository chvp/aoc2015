#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    scount = 0
    bcount = 0
    rcount = 0
    with open(sys.argv[2]) as inp:
        for line in inp:
            scount += len(line.strip())
            bcount += len(eval(line.strip()))
            rcount += len('"' + line.strip().replace('\\', '\\\\').replace('"', '\\"') + '"')
    if int(sys.argv[1]) == 1:
        print(scount - bcount)
    else:
        print(rcount - scount)
