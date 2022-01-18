#!/usr/bin/env python3

import functools
import sys

if __name__ == '__main__':
    signals = {}
    with open(sys.argv[2]) as inp:
        for line in inp:
            operation, destination = line.strip().split(' -> ')
            if 'NOT' in operation:
                signals[destination] = ('NOT', operation[4:])
            elif 'AND' in operation:
                signals[destination] = ('AND', *operation.split(' AND '))
            elif 'OR' in operation:
                signals[destination] = ('OR', *operation.split(' OR '))
            elif 'LSHIFT' in operation:
                signals[destination] = ('LSHIFT', *operation.split(' LSHIFT '))
            elif 'RSHIFT' in operation:
                signals[destination] = ('RSHIFT', *operation.split(' RSHIFT '))
            else:
                signals[destination] = ('VAL', operation)

    @functools.cache
    def get_value(key, version=1):
        if key.isnumeric():
            return int(key)
        if signals[key][0] == 'VAL':
            return get_value(signals[key][1], version)
        if signals[key][0] == 'NOT':
            return ~get_value(signals[key][1], version)
        if signals[key][0] == 'AND':
            return get_value(signals[key][1], version) & get_value(signals[key][2], version)
        if signals[key][0] == 'OR':
            return get_value(signals[key][1], version) | get_value(signals[key][2], version)
        if signals[key][0] == 'LSHIFT':
            return get_value(signals[key][1], version) << get_value(signals[key][2], version)
        if signals[key][0] == 'RSHIFT':
            return get_value(signals[key][1], version) >> get_value(signals[key][2], version)
        return 0

    if int(sys.argv[1]) == 1:
        print(get_value('a'))
    else:
        signals['b'] = ('VAL', str(get_value('a')))
        print(get_value('a', 2))
