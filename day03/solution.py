#!/usr/bin/env python3

import sys

mapping = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0),
}

def do_visits(directions):
    position = 0, 0
    visited = {position}
    for d in directions:
        position = position[0] + mapping[d][0], position[1] + mapping[d][1]
        visited.add(position)
    return visited

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        directions = inp.read().strip()
    if int(sys.argv[1]) == 1:
        visited = do_visits(directions)
    else:
        visited = do_visits(directions[::2]) | do_visits(directions[1::2])
    print(len(visited))
