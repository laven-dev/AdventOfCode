#!/usr/bin/env python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [list(x) for x in data]

directions = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}

position = []
linecount = 0

for line in data:
    if "^" in line:
        position.append(linecount)
        position.append(line.index("^"))
    else:
        linecount += 1

startpos = tuple(position)
direction = data[position[0]][position[1]]
silver = []
gold = 0

while True:
    silver.append(tuple(position))

    newpos = [
        position[0] + directions[direction][0],
        position[1] + directions[direction][1]
    ]

    if (
        newpos[0] >= len(data) or
        newpos[0] < 0 or
        newpos[1] >= len(data[0]) or
        newpos[1] < 0
    ):
        break

    if data[newpos[0]][newpos[1]] == "#":
        directionchars = list(directions.keys())
        direction = directionchars[(directionchars.index(direction) + 1) % 4]
    else:
        position = newpos

def checkgold(data: list[list[str]], startpos: tuple[int], toggle: list[int, int]) -> bool:
    loop = None
    direction = "^"
    position = list(startpos)
    seent = set()
    data[toggle[0]][toggle[1]] = "#"
    while True:
        state = (*position, direction)
        if state in seent:
            loop = True
            break
        seent.add(state)

        newpos = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]

        if (
            newpos[0] >= len(data) or
            newpos[0] < 0 or
            newpos[1] >= len(data[0]) or
            newpos[1] < 0
        ):
            loop = False
            break

        if data[newpos[0]][newpos[1]] == "#":
            directionchars = list(directions.keys())
            direction = directionchars[(directionchars.index(direction) + 1) % 4]
        else:
            position = newpos

    data[toggle[0]][toggle[1]] = "."
    return loop

from multiprocessing import pool, cpu_count

arguments = []
for i, newobst in enumerate(set(silver), start=1):
    if tuple(newobst) == startpos:
        continue
    arguments.append((data, startpos, tuple(newobst)))

for result in pool.Pool(cpu_count()).starmap(checkgold, arguments):
    if result:
        gold += 1

print(f"Silver: {len(set(silver))}, Gold: {gold}")