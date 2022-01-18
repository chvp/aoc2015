#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    program = []
    with open(sys.argv[2]) as inp:
        for line in inp:
            inst, args = line.strip().split(maxsplit=1)
            args = tuple(args.split(', '))
            program.append((inst,) + args)
    if int(sys.argv[1]) == 1:
        state = (0, 0, 0)
    else:
        state = (0, 1, 0)
    while state[0] < len(program):
        inst = program[state[0]]
        if inst[0] == "hlf":
            if inst[1] == 'a':
                state = (state[0] + 1, state[1] // 2, state[2])
            else:
                state = (state[0] + 1, state[1], state[2] // 2)
        elif inst[0] == "tpl":
            if inst[1] == 'a':
                state = (state[0] + 1, state[1] * 3, state[2])
            else:
                state = (state[0] + 1, state[1], state[2] * 3)
        elif inst[0] == "inc":
            if inst[1] == 'a':
                state = (state[0] + 1, state[1] + 1, state[2])
            else:
                state = (state[0] + 1, state[1], state[2] + 1)
        elif inst[0] == "jmp":
            state = (state[0] + int(inst[1]), state[1], state[2])
        elif inst[0] == "jie":
            if state[1 + ord(inst[1]) - ord('a')] % 2 == 0:
                state = (state[0] + int(inst[2]), state[1], state[2])
            else:
                state = (state[0] + 1, state[1], state[2])
        else:
            if state[1 + ord(inst[1]) - ord('a')] == 1:
                state = (state[0] + int(inst[2]), state[1], state[2])
            else:
                state = (state[0] + 1, state[1], state[2])
    print(state[2])
            
            
