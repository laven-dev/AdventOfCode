#!/usr/bin/env python3

import sys
import re
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

rules = []
instructions = []

# Format the data correctly
for line in data:
    if line.find('|') > 0:
        rules.append(line.split("|"))
    
    if line.find('|') == -1:
        instructions.append(line.split(","))

rules = [[int(x) for x in y] for y in rules]
instructions = [[int(x) for x in y] for y in instructions[1:]]

def ruleCheck(rules, instructions):
    

print(instructions)