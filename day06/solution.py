#!/usr/bin/env python3

import sys

def apply(grid, x1, y1, x2, y2, fun):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = fun(grid[x][y])

def parse_coordinates(s):
    c1, c2 = s.split(' through ')
    x1, y1 = map(int, c1.split(','))
    x2, y2 = map(int, c2.split(','))
    return x1, y1, x2, y2

if __name__ == '__main__':
    grid = [[0] * 1000 for i in range(1000)]
    if int(sys.argv[1]) == 1:
        actions = {'on': lambda _: 1, 'off': lambda _: 0, 'toggle': lambda x: not x}
    else:
        actions = {'on': lambda x: x + 1, 'off': lambda x: max(x - 1, 0), 'toggle': lambda x: x + 2}
    with open(sys.argv[2]) as inp:
        for line in inp:
            if line.startswith('turn on'):
                apply(grid, *parse_coordinates(line[8:]), actions['on'])
            elif line.startswith('turn off'):
                apply(grid, *parse_coordinates(line[9:]), actions['off'])
            else:
                apply(grid, *parse_coordinates(line[7:]), actions['toggle'])
    print(sum(sum(l) for l in grid))
