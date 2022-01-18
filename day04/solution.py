#!/usr/bin/env python3

import sys
from hashlib import md5

def hasher(data):
    m = md5()
    m.update(data.encode())
    return m.hexdigest()

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        data = inp.read().strip()
    prefix = "00000" if int(sys.argv[1]) == 1 else "000000"
    counter = 0
    while hasher(f"{data}{counter}")[:len(prefix)] != prefix:
        counter += 1
    print(counter)
