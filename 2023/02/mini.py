import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()
    data = [game.removeprefix("Game ").split(" ") for game in data]

# Loaded bag with 12 r, 13 g, 14 b
bag = {"red":12, "green":13, "blue":14}
silver, gold = [], []

# Silver
for game in data:
    maxes = {k: 0 for k in bag.keys()}
    gameID = int(game.pop(0).removesuffix(":"))
    valid = True

    amount = 0
    for i in game:
        if i.isnumeric():
            amount = int(i)
            continue

        if i.endswith((",", ";")): i = i[:-1]

        colour = i
        if maxes[colour] < amount: maxes[colour] = amount
        if amount > bag[colour]: valid = False
    
    silver.append(gameID if valid else 0)
    gold.append(maxes["red"] * maxes["green"] * maxes["blue"])

print(f"Silver: {sum(silver)} Gold: {sum(gold)}")
