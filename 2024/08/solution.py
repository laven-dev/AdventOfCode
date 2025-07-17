#!/usr/bin/env python3

import sys
from typing import NamedTuple
import itertools
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [list(x) for x in data]

class Antenna(NamedTuple):
    char: str
    y: int
    x: int

class Antinode(NamedTuple):
    y: int
    x: int

# Create a list of all antennas
def find_antennas(data: list[list[str]]) -> list[Antenna]:
    y, x = 0, 0
    antennas = []
    for line in data:
        x = 0
        for node in line:
            if node != ".":
                antennas.append(
                    Antenna(
                        char = node,
                        y = y,
                        x = x,
                    )
                )
                x += 1
            else:
                x += 1
        y += 1
        
    return antennas

# Create a list of all antinodes
def find_antinodes(antennas: list[Antenna], gold: bool) -> list[Antinode]:
    antinodes = []
    for antenna1, antenna2 in itertools.combinations(antennas, 2):
        vector = []
        if antenna1.char == antenna2.char:
            vector = [antenna2.y - antenna1.y, antenna2.x - antenna1.x]

            # Calculate repeated antinodes until worst-case scenario
            if gold:
                for k in range(len(data)):
                    # Out of Bounds check
                    if (
                        0 <= antenna1.y - (vector[0] * k) < len(data) and
                        0 <= antenna1.x - (vector[1] * k) < len(data[0])
                    ):
                        antinodes.append(
                            Antinode(
                                y = antenna1.y - (vector[0] * k),
                                x = antenna1.x - (vector[1] * k),
                            )
                        )

                    # Out of Bounds check
                    if (
                        0 <= antenna2.y + (vector[0] * k) < len(data) and
                        0 <= antenna2.x + (vector[1] * k) < len(data[0])
                    ):
                        antinodes.append(
                            Antinode(
                                y = antenna2.y + (vector[0] * k),
                                x = antenna2.x + (vector[1] * k),
                            )
                        )

            # Only calculate 1st order antinode
            else:
                # Out of Bounds check
                if (
                    0 <= antenna1.y - vector[0] < len(data) and
                    0 <= antenna1.x - vector[1] < len(data[0])
                ):
                    antinodes.append(
                        Antinode(
                            y = antenna1.y - vector[0],
                            x = antenna1.x - vector[1],
                        )
                    )

                # Out of Bounds check
                if (
                    0 <= antenna2.y + vector[0] < len(data) and
                    0 <= antenna2.x + vector[1] < len(data[0])
                ):
                    antinodes.append(
                        Antinode(
                            y = antenna2.y + vector[0],
                            x = antenna2.x + vector[1],
                        )
                    )
    return antinodes

print(f"Silver: {len(set(find_antinodes(find_antennas(data), False)))}, Gold: {len(set(find_antinodes(find_antennas(data), True)))}")