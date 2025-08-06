import sys
from rich.pretty import pprint

with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = [x for x in f.read().splitlines()]

for i in range(len(data)):
    data[i] = [[int(x) for x in coord[2:].split(",")] for coord in data[i].split(" ")]

width, height = 101, 103

def tick(position: list[int], vector: list[int]) -> list[list[int]]:
    new_position = [(position[0] + vector[0]) % width, (position[1] + vector[1]) % height]
    return [new_position, vector]

NW, NE, SW, SE = 0, 0, 0, 0

for _ in range(20000):
    data = [tick(*robot) for robot in data]

    if _ == 99:
        for robot in data:
            x, y = robot[0]
            x_mid, y_mid = (width // 2), (height // 2)
            if x == x_mid or y == y_mid:
                continue
            if x < x_mid and y < y_mid:
                NW += 1

            if x > x_mid and y < y_mid:
                NE += 1

            if x < x_mid and y > y_mid:
                SW += 1
            
            if x > x_mid and y > y_mid:
                SE += 1

        pprint(f"Silver: {NW * NE * SW * SE}")

    if _ % width != 3 or _ % height != 75:
        continue

    pprint(f"Gold: {_ + 1}")
    for h in range(height):
        line = []
        for w in range(width):
            coord = [w, h]
            if coord in [x[0] for x in data]:
                line.append("X")
            else:
                line.append(".")
        
        print("".join(line))

    print("")
    break