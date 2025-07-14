#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()


data = [line.split() for line in data]
for line in data:
    line[0] = int(line[0].removesuffix(":"))
silver = 0
gold = 0

def checksilver(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    left = line.pop(0)
    right = line.pop(0)
    addlist = [left + right] + line
    multlist = [left * right] + line
    return checksilver(addlist) + checksilver(multlist)

def checkgold(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    if len(line) == 0:
        return []
    left = line.pop(0)
    right = line.pop(0)
    addlist = [left + right] + line
    multlist = [left * right] + line
    concatlist = [int(f"{left}{right}")] + line
    return checkgold(addlist) + checkgold(multlist) + checkgold(concatlist)

for line in data:
    line = [int(x) for x in line]
    target = line.pop(0)
    if target in checksilver(line.copy()):
        silver += target
    if target in checkgold(line.copy()):
        gold += target

print(f"Silver: {silver}, Gold: {gold}")