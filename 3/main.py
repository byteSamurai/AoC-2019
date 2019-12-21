from copy import deepcopy

import numpy

lines = [line.rstrip('\n') for line in open('input.txt')]
w1 = lines[0].split(',')
w2 = lines[1].split(',')

dim = 15000
grid = numpy.zeros((dim, dim))


def mark_way(g, start: (int, int, int), _dir: str, _dis: int, ign_crosses=False, until=None) -> (int, int, int):
    t = [start[0], start[1], start[2]]
    while t[2] < (start[2] + _dis):
        if until is not None:
            if t[0] == until[0] and t[1] == until[1]:
                return t

        if _dir == 'U':
            t[0] -= 1
        elif _dir == 'D':
            t[0] += 1
        elif _dir == 'L':
            t[1] -= 1
        elif _dir == 'R':
            t[1] += 1

        t[2] += 1

        if ign_crosses:
            g[t[0]][t[1]] = 1
        else:
            g[t[0]][t[1]] += 1

    return tuple(t)


#         x     y
origin = (int(dim / 2), int(dim / 2), 0)

for wire in [(w1, True), (w2, False)]:
    pointer = deepcopy(origin)
    for s in wire[0]:
        dir = s[0]
        dis = int(s[1:])
        pointer = mark_way(grid, pointer, dir, dis, wire[1])

idx = numpy.where(grid > 1)
grid[origin[0], origin[1]] = 99

distances = []
for m in range(0, len(idx[0])):
    distances.append(abs(origin[0] - idx[0][m]) + abs(origin[1] - idx[1][m]))

print("Closest Manhatten distance to the closest distance: " + str(numpy.min(distances)))

x_points = []

for m in range(0, len(idx[0])):
    x_points.append((idx[0][m], idx[1][m]))

signal_delays = []
print("looking for " + str(len(x_points)) + " points")
x = 0
for x_point in x_points:
    signal_delay = 0
    x += 1
    for wire in [w1, w2]:
        grid_temp = numpy.zeros((dim, dim))
        pointer = deepcopy(origin)
        for s in wire:
            dir = s[0]
            dis = int(s[1:])
            pointer2 = mark_way(grid_temp, pointer, dir, dis, True, x_point)
            if pointer2 == pointer:
                print("{:04.2f}%".format(x/len(x_points)*100))
                break
            else:
                pointer = pointer2
        signal_delay += pointer[2]
    signal_delays.append(signal_delay)

print(numpy.min(signal_delays))
