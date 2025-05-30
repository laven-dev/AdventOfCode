#!/usr/bin/env python3

import sys
import itertools
from typing import NamedTuple
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [list(x) for x in data]

# word = str(input("Word to search for: "))
word = 'XMAS'
vectors = [x for x in itertools.permutations([0, 1, -1], 2)] + [(1, 1), (-1, -1)]

class Location(NamedTuple):
    y: int
    x: int
    direction: tuple[int]

def wordSearch(data: list[list[str]], word: str):
    # wordCount = 0
    locations = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            # char = data[y][x]
            for vector in vectors:
                yippee = True
                for i in range(len(word)):
                    if not yippee:
                        continue
                    newy = y + (vector[0] * i)
                    newx = x + (vector[1] * i)

                    if newy < 0 or newy >= len(data):
                        yippee = False
                        continue

                    if newx < 0 or newx >= len(data[y]):
                        yippee = False
                        continue

                    try:
                        char = data[newy][newx]
                    except Exception:
                        yippee = False
                        continue

                    if char != word[i]:
                        yippee = False
                
                if yippee:
                    locations.append(
                        Location(
                            x=x,
                            y=y,
                            direction=vector,
                        )
                    )

    return locations

def gold(locations: list[Location]):
    midpoints = []
    golden = 0
    for i in locations:
        if 0 in i.direction:
            continue
        midpoint = [i.y + i.direction[0], i.x + i.direction[1]]
        if midpoint in midpoints:
            golden += 1
        midpoints.append(midpoint)
    
    return golden

print(f"Silver: {len(wordSearch(data, 'XMAS'))} Gold: {gold(wordSearch(data, 'MAS'))}")
