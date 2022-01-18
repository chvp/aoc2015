#!/usr/bin/env python3

import sys

def look_and_see(saw):
    result = ""
    run = saw[0]
    count = 1
    for c in saw[1:]:
        if c == run:
            count += 1
        else:
            result += f"{count}{run}"
            run = c
            count = 1
    result += f"{count}{run}"
    return result

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        saw = inp.read().strip()
    for _ in range(40 if int(sys.argv[1]) == 1 else 50):
        saw = look_and_see(saw)
    print(len(saw))
