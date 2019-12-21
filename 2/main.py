import sys

lines = [line for line in open('input.txt')]
prog = lines[0].split(',')
prog = list(map(int, prog))


def ops(x):
    return {
        1: lambda x, y: x + y,
        2: lambda x, y: x * y,
    }.get(x)


def process(_prog, noun, verb) -> int:
    wp = 0
    p = _prog.copy()
    p[1] = noun
    p[2] = verb

    while (wp + 4) < len(p):
        if p[wp] == 99:
            wp += 1
            continue
        # print(f"run op {p[wp]} on: {p[p[wp + 1]]}, {p[p[wp + 2]]} to {p[p[wp + 3]]}")
        p[p[wp + 3]] = ops(p[wp])(p[p[wp + 1]], p[p[wp + 2]])
        wp += 4
    return p[0]


# 6627023

print(process(prog, 12, 2))

for i in range(0, 99):
    for j in range(0, 99):
        if process(prog, i, j) == 19690720:
            print(f"found it:{i},{j}")
            sys.exit()
