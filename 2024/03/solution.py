#!/usr/bin/env python3

import sys
import re
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = "".join(f.read().splitlines())

mulList = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)
# print(mulList)
def mult(data: str) -> int:
    data = data.removeprefix("mul(")
    data = data[:-1]
    left, right = [int(x) for x in data.split(",")]
    result = left * right
    return result

silver = 0
gold = 0
yeppers = True
for item in mulList:
    if item == "do()":
        yeppers = True
        continue
    if item == "don't()":
        yeppers = False
        continue

    if yeppers:
        gold += mult(item)
    
    silver += mult(item)

print(f"Silver: {silver}, Gold: {gold}")
