#!/usr/bin/env python3

import sys

def step_el2(e, i, j, grid):
    total = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if (not (ii == 0 and jj == 0)) and 0 <= i + ii < len(grid) and 0 <= j + jj < len(grid[i + ii]) and grid[i + ii][j + jj]:
                total += 1
    if (i == 0 and j == 0) or (i == 0 and j == len(grid[i]) - 1) or (i == len(grid) - 1 and j == 0) or (i == len(grid) - 1 and j == len(grid[i]) - 1):
        return True
    if e:
        return total in (2, 3)
    return total == 3

def step_el(e, i, j, grid):
    total = 0
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            if (not (ii == 0 and jj == 0)) and 0 <= i + ii < len(grid) and 0 <= j + jj < len(grid[i + ii]) and grid[i + ii][j + jj]:
                total += 1
    if e:
        return total in (2, 3)
    return total == 3

def do_step(grid):
    return [[step(e, i, j, grid) for j, e in enumerate(row)] for i, row in enumerate(grid)]

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        grid = [[True if c == '#' else False for c in line.strip()] for line in inp]
    if int(sys.argv[1]) == 1:
        step = step_el
    else:
        step = step_el2
        grid[0][0] = True
        grid[0][-1] = True
        grid[-1][0] = True
        grid[-1][-1] = True
    for i in range(100):
        grid = do_step(grid)
    print(sum(sum(1 if e else 0 for e in row) for row in grid))
