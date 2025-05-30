import sys
import regex
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().splitlines()

silver = 0
gold = 0
for i in data:
    twoDigit = 0
    numbers = regex.findall(r"[0-9]", i)
    if len(numbers) == 1:
        numbers.append(numbers[0])
    twoDigit = int(''.join([numbers.pop(0), numbers.pop(-1)]))
    silver += twoDigit

for j in data:
    twoDigit = 0
    numbers = regex.findall(r"one|two|three|four|five|six|seven|eight|nine|[0-9]", j, overlapped = True)
    if len(numbers) == 1:
        numbers.append(numbers[0])
    for k in range(len(numbers)):
        if numbers[k] == 'one':
            numbers[k] = '1'
        if numbers[k] == 'two':
            numbers[k] = '2'
        if numbers[k] == 'three':
            numbers[k] = '3'
        if numbers[k] == 'four':
            numbers[k] = '4'
        if numbers[k] == 'five':
            numbers[k] = '5'
        if numbers[k] == 'six':
            numbers[k] = '6'
        if numbers[k] == 'seven':
            numbers[k] = '7'
        if numbers[k] == 'eight':
            numbers[k] = '8'
        if numbers[k] == 'nine':
            numbers[k] = '9'
    twoDigit = int(''.join([numbers.pop(0), numbers.pop(-1)]))
    gold += twoDigit

print(f"Silver: {silver} Gold: {gold}")