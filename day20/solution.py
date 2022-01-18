#!/usr/bin/env python3

import sys
import math

def divisors(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            yield n // i

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        minpresents = int(inp.read().strip())
    n = 0
    if int(sys.argv[1]) == 1:
        minpresents /= 10
        while sum(divisors(n)) < minpresents:
            n += 1
    else:
        minpresents /= 11
        while sum(divisor for divisor in divisors(n) if n / divisor <= 50) < minpresents:
            n += 1
    print(n)
    

