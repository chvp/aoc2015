#!/usr/bin/env python3

import sys
import json

def sum_numbers(j):
    if isinstance(j, dict):
        return sum(sum_numbers(el) for el in j.values())
    if isinstance(j, list):
        return sum(sum_numbers(el) for el in j)
    if isinstance(j, int):
        return j
    return 0

def sum_numbers_no_red(j):
    if isinstance(j, dict):
        return 0 if "red" in j.values() else sum(sum_numbers_no_red(el) for el in j.values())
    if isinstance(j, list):
        return sum(sum_numbers_no_red(el) for el in j)
    if isinstance(j, int):
        return j
    return 0

if __name__ == '__main__':
    with open(sys.argv[2]) as inp:
        data = json.load(inp)
    if int(sys.argv[1]) == 1:
        print(sum_numbers(data))
    else:
        print(sum_numbers_no_red(data))
