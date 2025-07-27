import sys
from typing import NamedTuple
from rich.pretty import pprint
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [[int(i) for i in x] for x in f.read().strip().splitlines()]

class Coordinate(NamedTuple):
    y: int
    x: int

trails = []

def inbounds(coord: Coordinate) -> bool:
    if coord.y >= len(data) or coord.x >= len(data[0]):
        return False
    if coord.y < 0 or coord.x < 0:
        return False
    
    return True

def find_trails(coord: Coordinate) -> list[list[Coordinate]]:
    whoami = data[coord.y][coord.x]
    if whoami == 9:
        return [[coord]]

    temp_trails = []
    moves = [
        Coordinate(coord.y + 1, coord.x),
        Coordinate(coord.y - 1, coord.x),
        Coordinate(coord.y, coord.x + 1),
        Coordinate(coord.y, coord.x - 1),
    ]
    
    for move in moves:
        if not inbounds(move):
            continue
        if data[move.y][move.x] != whoami + 1:
            continue

        output = find_trails(move)

        for out in output:
            temp_trails.append([coord] + out)
    
    return temp_trails

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] != 0:
            continue

        trails += find_trails(Coordinate(y, x))

def silver(trails: list[list[Coordinate]]) -> int:
    mapping = {}
    for trail in trails:
        start, end = trail[0], trail[-1]
        if start not in mapping:
            mapping[start] = set()
        
        mapping[start].add(end)
        
    return sum([len(x) for x in mapping.values()])

pprint(f"Silver: {silver(trails)}, Gold: {len(trails)}")
