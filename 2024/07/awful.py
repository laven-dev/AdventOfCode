#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()


data = [line.split() for line in data]
for line in data:
    line[0] = int(line[0].removesuffix(":"))
silver = 0
gold = 0

def checksilvercrusty(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    left = line.pop(0)
    right = line.pop(0)
    results = [left + right, left * right]
    while True:
        temp = []
        if line == []:
            break
        right = line.pop(0)
        for i in results:
            temp.append(i + right)
            temp.append(i * right)
        
        results = temp
    
    results = list(set(results))

    return results

def checkgoldcrusty(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    left = line.pop(0)
    right = line.pop(0)
    results = [left + right, left * right, int(f"{left}{right}")]
    while True:
        temp = []
        if line == []:
            break
        right = line.pop(0)
        for i in results:
            temp.append(i + right)
            temp.append(i * right)
            temp.append(int(f"{i}{right}"))
        
        results = temp
    
    results = list(set(results))

    return results

for line in data:
    line = [int(x) for x in line]
    target = line.pop(0)
    if target in checksilvercrusty(line.copy()):
        silver += target
    if target in checkgoldcrusty(line.copy()):
        gold += target

print(f"Silver: {silver}, Gold: {gold}")