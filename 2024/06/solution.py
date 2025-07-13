#!/usr/bin/env python3

import sys
from copy import deepcopy
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [list(x) for x in data]

# Define Directions
directions = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}

position = []
linecount = 0

# Define Starting Position
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

# Silver
while True:
    # Add Current Position to Silver
    silver.append(tuple(position))

    # Define newpos
    newpos = [
        position[0] + directions[direction][0],
        position[1] + directions[direction][1]
    ]

    # Foldback Edgecase Fix
    if (
        newpos[0] >= len(data) or
        newpos[0] < 0 or
        newpos[1] >= len(data[0]) or
        newpos[1] < 0
    ):
        break

    # Turn if run into Obstruction
    if data[newpos[0]][newpos[1]] == "#":
        directionchars = list(directions.keys())
        direction = directionchars[(directionchars.index(direction) + 1) % 4]
    else:
        position = newpos

# Checks if a dataset loops
def checkgold(data: list[list[str]], startpos: tuple[int]) -> bool:
    direction = "^"
    position = list(startpos)
    seent = set()
    while True:
        # If this state has been seen before, data loops.
        state = (*position, direction)
        if state in seent:
            return True
        
        # Adds current state to a set
        seent.add(state)

        # Define newpos
        newpos = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]

        # Foldback Edgecase Fix
        if (
            newpos[0] >= len(data) or
            newpos[0] < 0 or
            newpos[1] >= len(data[0]) or
            newpos[1] < 0
        ):
            return False

        # Turn if run into Obstruction
        if data[newpos[0]][newpos[1]] == "#":
            directionchars = list(directions.keys())
            direction = directionchars[(directionchars.index(direction) + 1) % 4]
        else:
            position = newpos

# Checks every possible new obstruction for loop
for i, newobst in enumerate(set(silver), start=1):
    # print(f"{i}/{len(set(silver))}")
    if tuple(newobst) == startpos:
        continue
    datacopy = deepcopy(data)
    datacopy[newobst[0]][newobst[1]] = "#"
    if checkgold(datacopy, startpos):
        gold += 1

print(f"Silver: {len(set(silver))}, Gold: {gold}")