#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

data = [x.split() for x in data]
left = sorted([int(x[0]) for x in data])
right = sorted([int(x[1]) for x in data])

diff = 0
for (l, r) in zip(left, right):
    diff += abs(l - r)

print(f"Silver: {diff}")

sim = 0
for l in left:
    sim += (l * right.count(l))

print(f"Gold: {sim}")
