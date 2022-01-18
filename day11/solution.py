#!/usr/bin/env python3

import sys
import functools

def to_bytes(value):
    return [(value // (26 ** i)) % 26 for i in range(7, -1, -1)]

def to_password(value):
    return ''.join(chr(i + ord('a')) for i in to_bytes(value))

def valid(value):
    bs = to_bytes(value)
    if ord('i') - ord('a') in bs or ord('l') - ord('a') in bs or ord('o') - ord('a') in bs:
        return False
    pairs = set()
    run = False
    for i, b in enumerate(bs[:-1]):
        if i < len(bs) - 2 and bs[i + 1] == b + 1 and bs[i + 2] == b + 2:
            run = True
        if b == bs[i + 1]:
            pairs.add(b)
    return run and len(pairs) > 1

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        data = list(map(lambda c: ord(c) - ord('a'), inp.read().strip()))
    value = functools.reduce(lambda c1, c2: c1 * 26 + c2, data, 0)
    while not valid(value):
        value += 1
    if int(sys.argv[1]) == 2:
        value += 1
    while not valid(value):
        value += 1
    print(to_password(value))
