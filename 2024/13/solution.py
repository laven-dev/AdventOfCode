import sys
import re
from rich.pretty import pprint

with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x.split() for x in f.read().splitlines()]

temp_data = []
temp = []
for line in data:
    if line != []:
        temp += line
    else:
        temp_data += tuple(temp)
        temp = []

def make_machine(data: list[str]) -> list[list]:
    button_a = [int(re.sub(r'\D', '', data[2])), int(re.sub(r'\D', '', data[3]))]
    button_b = [int(re.sub(r'\D', '', data[6])), int(re.sub(r'\D', '', data[7]))]
    target = [int(re.sub(r'\D', '', data[9])), int(re.sub(r'\D', '', data[10]))]

    for i in range(0, 11):
        temp_data.pop(0)
    return [button_a, button_b, target]

# Brute Force
def silver_solve(input: list[list[int]]) -> int:
    tokens = 0
    temp = []
    dest_x, dest_y = 0, 0
    for a in range(0, 101):
        for b in range(0, 101):
            dest_x = (input[0][0] * a) + (input[1][0] * b)
            dest_y = (input[0][1] * a) + (input[1][1] * b)
            if dest_x == input[2][0] and dest_y == input[2][1]:
                temp.append(a*3 + b)
    
    if temp != []:
        # pprint(f"Target ({input[2][0]}, {input[2][1]}) passed with {min(temp)} tokens!")
        return min(temp)
    else:
        return 0

import sympy

# Simultaneous Equations
def gold_solve(input: list[list[int]]) -> int:
    a = sympy.Symbol('a',integer=True)
    b = sympy.Symbol('b',integer=True)
    x_equ = sympy.Eq((input[0][0] * a) + (input[1][0] * b), input[2][0] + 10000000000000)
    y_equ = sympy.Eq((input[0][1] * a) + (input[1][1] * b), input[2][1] + 10000000000000)
    result = sympy.solve([x_equ, y_equ], (a,b))

    if result:
        return result[a]*3 + result[b]
    else:
        return 0

silver = 0
gold = 0
while temp_data:
    macheen = make_machine(temp_data)
    silver += silver_solve(macheen)
    gold += gold_solve(macheen)

pprint(f"Silver: {silver}, Gold: {gold}")