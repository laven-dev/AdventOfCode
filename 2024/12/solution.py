#!/usr/bin/env python3

from contextlib import redirect_stderr
from copy import deepcopy
import sys
from typing import NamedTuple
from rich.pretty import pprint

with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [list(x) for x in f.read().splitlines()]

class Plant(NamedTuple):
    y: int
    x: int
    type: str

def sanitize(plant: Plant, new_plant: Plant) -> bool:
    if new_plant.y < 0:
        return False
    if new_plant.y >= len(data):
        return False
    if new_plant.x < 0:
        return False
    if new_plant.x >= len(data[0]):
        return False
    if new_plant.type != plant.type:
        return False
    
    return True

def flood_fill(plant: Plant) -> set[Plant]:
    if plant.type == "_":
        return set()

    region = set()

    new_plants = []

    try:
        new_plants.append(Plant(plant.y + 1, plant.x, data[plant.y + 1][plant.x]))
    except:
        pass
    try:
        new_plants.append(Plant(plant.y - 1, plant.x, data[plant.y - 1][plant.x]))
    except:
        pass
    try:
        new_plants.append(Plant(plant.y, plant.x + 1, data[plant.y][plant.x + 1]))
    except:
        pass
    try:
        new_plants.append(Plant(plant.y, plant.x - 1, data[plant.y][plant.x - 1]))
    except:
        pass
    region.add(plant)
    for nplant in new_plants:
        if not sanitize(plant, nplant):
            continue
        
        region.add(nplant)

        data[nplant.y][nplant.x] = "_"
        for flood in flood_fill(nplant):
            region.add(flood)
    
    return region

def perimeter(region: set[Plant]) -> list[Plant]:
    # total = 0
    perim = []
    for plant in region:
        new_plants = []

        try:
            new_plants.append(Plant(plant.y + 1, plant.x, plant.type))
        except:
            pass
        try:
            new_plants.append(Plant(plant.y - 1, plant.x, plant.type))
        except:
            pass
        try:
            new_plants.append(Plant(plant.y, plant.x + 1, plant.type))
        except:
            pass
        try:
            new_plants.append(Plant(plant.y, plant.x - 1, plant.type))
        except:
            pass
        
        for nplant in new_plants:
            if nplant not in region:
                perim.append(nplant)
                # total += 1

    return perim

def sides(region: set[Plant]) -> int:
    min_y = min([x.y for x in region])
    max_y = max([x.y for x in region])
    min_x = min([x.x for x in region])
    max_x = max([x.x for x in region])

    region = [(p.y, p.x) for p in region]

    x_entries = []
    am_i_in = False
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (y, x) in region and am_i_in == False:
                am_i_in = True
                x_entries.append((y, x, True))

            if (y, x) not in region and am_i_in == True:
                am_i_in = False
                x_entries.append((y, x, False))

    y_entries = []
    am_i_in = False
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            if (y, x) in region and am_i_in == False:
                am_i_in = True
                y_entries.append((y, x, True))

            if (y, x) not in region and am_i_in == True:
                am_i_in = False
                y_entries.append((y, x, False))

    
    groups = []
    while x_entries:
        og = x_entries.pop(0)
        tmp = [og]
        for i in range(1, 10000):
            target = (og[0] + i, og[1], og[2])
            if target in x_entries:
                tmp.append(x_entries.pop(x_entries.index(target)))
            else:
                break
        
        groups.append(tmp)

    while y_entries:
        og = y_entries.pop(0)
        tmp = [og]
        for i in range(1, 10000):
            target = (og[0], og[1] + i, og[2])
            if target in y_entries:
                tmp.append(y_entries.pop(y_entries.index(target)))
            else:
                break
        
        groups.append(tmp)

    return len(groups)

silver = 0
gold = 0

for y in range(len(data)):
    for x in range(len(data[y])):
        temp = flood_fill(Plant(y, x, data[y][x]))
        if temp != set():
            area = len(temp)
            perim = perimeter(temp)
            side_count = sides(temp)
            # pprint(f"Region: {list(temp)[0].type}, Area: {area}, Sides: {side_count}")
            silver += area * len(perim)
            gold += area * side_count

pprint(f"Silver: {silver}, Gold: {gold}")