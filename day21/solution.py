#!/usr/bin/env python3

import sys
import heapq
from itertools import combinations

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3 , 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

def combat(player, boss):
    boss = (boss[0] - max(1, player[1] - boss[2]), boss[1], boss[2])
    if boss[0] <= 0:
        return True
    player = (player[0] - max(1, boss[1] - player[2]), player[1], player[2])
    if player[0] <= 0:
        return False
    return combat(player, boss)

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        to_beat = tuple(int(line.strip().split(': ')[1]) for line in inp)

    queue = []
    if int(sys.argv[1]) == 1:
        for w in weapons:
            for a in armor:
                for r1, r2 in combinations(rings, 2):
                    heapq.heappush(queue, tuple(map(sum, zip(w, a, r1, r2))))
        while not combat((100, queue[0][1], queue[0][2]), to_beat):
            heapq.heappop(queue)
        print(queue[0][0])
    else:
        for w in weapons:
            for a in armor:
                for r1, r2 in combinations(rings, 2):
                    buys = tuple(map(sum, zip(w, a, r1, r2)))
                    buys = (-buys[0], buys[1], buys[2])
                    heapq.heappush(queue, buys)
        while combat((100, queue[0][1], queue[0][2]), to_beat):
            heapq.heappop(queue)
        print(-queue[0][0])
