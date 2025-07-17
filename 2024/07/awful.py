#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

# Format the Data
data = [line.split() for line in data]
for line in data:
    line[0] = int(line[0].removesuffix(":"))
    
# Define silver and gold
silver = 0
gold = 0

# Silver Function
def checksilvercrusty(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    # Define left and right as the first two numbers
    left = line.pop(0)
    right = line.pop(0)
    # Define results as the first two possibilities
    results = [left + right, left * right]
    # Loops until all possible results calculated
    while True:
        temp = []
        # Break if no more numbers to run through
        if line == []:
            break
        # Get the next number
        right = line.pop(0)
        # Calculate all possible results
        for i in results:
            temp.append(i + right)
            temp.append(i * right)
        # Update the possible results list
        results = temp
    # Remove duplicates
    results = list(set(results))
    return results

def checkgoldcrusty(line: list[int]) -> list[int]:
    if len(line) == 1:
        return [line[0]]
    # Define left and right as the first two numbers
    left = line.pop(0)
    right = line.pop(0)
    # Define results as the first three possibilities
    results = [left + right, left * right, int(f"{left}{right}")]
    while True:
        temp = []
        # Break if no more numbers to run through
        if line == []:
            break
        # Get the next number
        right = line.pop(0)
        # Calculate all possible results
        for i in results:
            temp.append(i + right)
            temp.append(i * right)
            temp.append(int(f"{i}{right}"))
        # Update the possible results list
        results = temp
    # Remove duplicates
    results = list(set(results))
    return results

# For each line, if target in results, add target to silver/gold
for line in data:
    line = [int(x) for x in line]
    target = line.pop(0)
    if target in checksilvercrusty(line.copy()):
        silver += target
    if target in checkgoldcrusty(line.copy()):
        gold += target

print(f"Silver: {silver}, Gold: {gold}")