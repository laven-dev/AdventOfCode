import sys
from rich.pretty import pprint

data = [1750884, 193, 866395, 7, 1158, 31, 35216, 0]

def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    
    str_stone = str(stone)
    if len(str(stone)) % 2 == 0:
        return [int(str_stone[:len(str_stone) // 2]), int(str_stone[len(str_stone) // 2:])]
    
    return [stone * 2024]

memory = {}

def solve(stone: int, turns_left: int) -> int:
    if turns_left == 0:
        return 1
    
    args = (stone, turns_left)
    if args in memory:
        return memory[args]

    new_stones = blink(stone)
    output = 0
    for run_it_back in new_stones:
        output += solve(run_it_back, turns_left - 1)

    memory[args] = output
    return output

pprint(f"Silver: {sum([solve(stone, 25) for stone in data])}, "
       f"Gold: {sum([solve(stone, 75) for stone in data])}")