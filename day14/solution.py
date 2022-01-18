#!/usr/bin/env python3

import sys

def position_at(speed, run_time, rest_time, time):
    return speed * run_time * (time // (run_time + rest_time)) + speed * min(run_time, time % (run_time + rest_time))

if __name__ == '__main__':
    reindeer = []
    with open(sys.argv[2]) as inp:
        for line in inp:
            words = line.strip().split()
            reindeer.append((int(words[3]), int(words[6]), int(words[13])))

    if int(sys.argv[1]) == 1:
        print(max(position_at(*r, 2503) for r in reindeer))
    else:
        results = [0] * len(reindeer)
        for i in range(1, 2504):
            m = 0, 0
            for j, v in enumerate(position_at(*r, i) for r in reindeer):
                if v > m[1]:
                    m = j, v
            results[m[0]] += 1
        print(max(results))

