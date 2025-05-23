#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [x.split() for x in data]
data = [[int(x) for x in y] for y in data]

def solve(data):
    safeCount = 0
    for line in data:
        passed = True
        diffs = []
        
        for i in range(len(line) - 1):
            left = line[i]
            right = line[i + 1]
            diff = left - right
            diffs.append(diff)
            if abs(diff) > 3:
                passed = False
            if diff == 0:
                passed = False
        
        for j in range(len(diffs) -1):
            left = diffs[j]
            right = diffs[j + 1]
            if left * right < 0:
                passed = False
        
        if passed == True:
            safeCount += 1
    return safeCount

def gold(data):
    golden = 0
    for line in data:
        import copy
        subset = []
        for i in range(len(line)):
            new = copy.copy(line)
            del new[i]
            subset.append(new)
        
        temp = solve(subset)
        if temp > 0:
            golden += 1

    return golden

print(f"Silver: {solve(data)} Gold: {gold(data)}")