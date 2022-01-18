#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        data = inp.read()
    if int(sys.argv[1]) == 1:
        print(data.count('(') - data.count(')'))
    else:
        counter = 0, 0
        while counter[0] >= 0:
            counter = (counter[0] + (1 if data[counter[1]] == '(' else -1), counter[1] + 1)
        print(counter[1])
