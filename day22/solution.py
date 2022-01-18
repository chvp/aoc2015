#!/usr/bin/env python3

import sys
import heapq

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        to_beat = tuple(int(line.strip().split(': ')[1]) for line in inp)

    states = [(0, True, 500, 50, 0, 0, 0, *to_beat)]
    while states[0][7] >= 0:
        state = heapq.heappop(states)
        newstate = list(state)
        if state[5]:
            newstate[7] = newstate[7] - 3
        if state[6]:
            newstate[2] = newstate[2] + 101
        newstate[1] = not newstate[1]
        newstate[4] = max(0, newstate[4] - 1)
        newstate[5] = max(0, newstate[5] - 1)
        newstate[6] = max(0, newstate[6] - 1)
        if state[1]:
            if int(sys.argv[1]) == 2:
                newstate[3] = newstate[3] - 1
            if newstate[3] > 0:
                if newstate[2] >= 53:
                    to_add = list(newstate)
                    to_add[0] = to_add[0] + 53
                    to_add[2] = to_add[2] - 53
                    to_add[7] = to_add[7] - 4
                    heapq.heappush(states, tuple(to_add))
                if newstate[2] >= 73:
                    to_add = list(newstate)
                    to_add[0] = to_add[0] + 73
                    to_add[2] = to_add[2] - 73
                    to_add[3] = to_add[3] + 2
                    to_add[7] = to_add[7] - 2
                    heapq.heappush(states, tuple(to_add))
                if newstate[2] >= 113 and not newstate[4]:
                    to_add = list(newstate)
                    to_add[0] = to_add[0] + 113
                    to_add[2] = to_add[2] - 113
                    to_add[4] = 6
                    heapq.heappush(states, tuple(to_add))
                if newstate[2] >= 173 and not newstate[5]:
                    to_add = list(newstate)
                    to_add[0] = to_add[0] + 173
                    to_add[2] = to_add[2] - 173
                    to_add[5] = 6
                    heapq.heappush(states, tuple(to_add))
                if newstate[2] >= 229 and not newstate[6]:
                    to_add = list(newstate)
                    to_add[0] = to_add[0] + 229
                    to_add[2] = to_add[2] - 229
                    to_add[6] = 5
                    heapq.heappush(states, tuple(to_add))
        else:
            newstate[3] = newstate[3] - max(1, newstate[8] - (7 if state[4] else 0))
            if newstate[3] > 0:
                heapq.heappush(states, tuple(newstate))
    print(states[0][0])
            
