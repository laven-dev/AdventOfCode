import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()
    data = [game.removeprefix("Game ").split(" ") for game in data]

# Loaded bag with 12 r, 13 g, 14 b
bag = {"red":12, "green":13, "blue":14}
silver = 0
gold = 0

# Silver
for game in data:
    gameID = int(game.pop(0).removesuffix(":"))
    valid = True

    amount = 0
    for i in game:
        if i.isnumeric():
            amount = int(i)
            continue
        if i.endswith(","):
            colour = i.removesuffix(",")
            if amount > bag[colour]:
                valid = False
            continue
        if i.endswith("d") or i.endswith("n") or i.endswith("e"):
            colour = i
            if amount > bag[colour]:
                valid = False
            continue
        if i.endswith(";"):
            colour = i.removesuffix(";")
            if amount > bag[colour]:
                valid = False
            continue
    
    if valid:
        silver += gameID

# Gold
for game in data:
    minimum = {"red":0, "green":0, "blue":0}
    for i in game:
        if i.isnumeric():
            amount = int(i)
            continue
        if i.endswith(","):
            colour = i.removesuffix(",")
            if minimum[colour] < amount:
                minimum[colour] = amount
            continue
        if i.endswith("d") or i.endswith("n") or i.endswith("e"):
            colour = i
            if minimum[colour] < amount:
                minimum[colour] = amount
            continue
        if i.endswith(";"):
            colour = i.removesuffix(";")
            if minimum[colour] < amount:
                minimum[colour] = amount
            continue
    gold += minimum["red"] * minimum["green"] * minimum["blue"]

print(f"Silver: {silver} Gold: {gold}")
