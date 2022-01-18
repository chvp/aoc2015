#!/usr/bin/env python3

import sys

message = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

if __name__ == '__main__':
    aunts = []
    with open(sys.argv[2]) as inp:
        for line in inp:
            aunts.append({s.split(': ')[0]: int(s.split(': ')[1]) for s in line.strip().split(': ', maxsplit=1)[1].split(', ')})
    if int(sys.argv[1]) == 1:
        for i, aunt in enumerate(aunts):
            if all(aunt[key] == message[key] for key in aunt):
                print(i + 1)
    else:
        for i, aunt in enumerate(aunts):
            match = True
            for key in aunt:
                if key in ('cats', 'trees'):
                    match = match and aunt[key] > message[key]
                elif key in ('pomeranians', 'goldfish'):
                    match = match and aunt[key] < message[key]
                else:
                    match = match and aunt[key] == message[key]
            if match:
                print(i + 1)

