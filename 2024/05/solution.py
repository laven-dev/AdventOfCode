#!/usr/bin/env python3

import sys
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

rules = []
books = []
silver, gold = 0, 0

# Format the data correctly
for line in data:
    if line.find('|') > 0:
        rules.append(line.split("|"))
    
    if line.find('|') == -1:
        books.append(line.split(","))

# The grand int'ing
rules = [[int(x) for x in y] for y in rules]
books = [[int(x) for x in y] for y in books[1:]]
leftovers = []

# Silver
for book in books:
    valid = True
    for rule in rules:
        left, right = rule
        # If a rule is broken, make valid False
        if left in book and right in book:
            if book.index(left) > book.index(right):
                valid = False
                break
    
    # Calculates silver and speparates invalid books
    if valid:
        silver += book[len(book) // 2]
    else:
        leftovers.append(book)

# Gold
for book in leftovers:
    # Repeats until the book is valid
    while True:
        valid = True

        for rule in rules:
            left, right = rule
            if left in book and right in book:
                leftindex, rightindex = book.index(left), book.index(right)

                # Swaps positions of the numbers that broke the rule
                if leftindex > rightindex:
                    book[leftindex] = right
                    book[rightindex] = left
                    valid = False

        if valid:
            break

    # Calculate gold
    gold += book[len(book) // 2]

print(f"Silver: {silver}, Gold: {gold}")