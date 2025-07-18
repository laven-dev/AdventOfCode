import sys
from typing import NamedTuple
from rich.pretty import pprint
with open(sys.argv[1] if len(sys.argv) > 1 else "input.txt") as f:
    data = f.read().strip()

example = "2333133121414131402"

class Block(NamedTuple):
    file_id: int | None
    length: int

def create_fs(data: str) -> list[int | None]:
    filesystem = []
    for i, digit in enumerate(data):
        # filesystem += [(i // 2) if i % 2 == 0 else None] * int(digit)
        digit = int(digit)
        if i % 2 == 0:
            temp = [i // 2] * digit
        else:
            temp = [None] * digit

        filesystem += temp

    return filesystem

def clean_fs(filesystem: list[int | None]) -> list[int]:
    while None in filesystem:
        while filesystem[-1] is None:
            filesystem.pop(-1)

        i = filesystem.index(None)
        filesystem[i] = filesystem.pop(-1)

    return filesystem

def checksum_fs(filesystem: list[int]) -> int:
    checksum = 0
    for i, digit in enumerate(filesystem):
        checksum += (i * digit)
    
    return checksum

def create_gold_fs(data: str) -> list[int | None]:
    filesystem = []
    for i, digit in enumerate(data):
        # filesystem += [(i // 2) if i % 2 == 0 else None] * int(digit)
        digit = int(digit)
        if i % 2 == 0:
            block = Block(i // 2, digit)
        else:
            block = Block(None, digit)

        filesystem.append(block)

    return filesystem

def clean_gold_fs(filesystem: list[Block]) -> list[Block]:
    for i in range(filesystem[-1].file_id, -1, -1):
    # for i in reversed(list(range(filesystem[-1].file_id + 1))):
        target_file = [block for block in filesystem if block.file_id == i][0]

        empties = [block for block in filesystem
                    if block.file_id == None and
                    block.length >= target_file.length]
        
        if not empties:
            continue

        file_position = filesystem.index(target_file)
        empty0 = filesystem.index(empties[0])

        if empty0 > file_position:
            continue
        
        delta = empties[0].length - target_file.length

        filesystem[empty0] = filesystem.pop(file_position)
        filesystem.insert(file_position, Block(None, target_file.length))

        if delta > 0:
            filesystem.insert(empty0 + 1, Block(None, delta))

    return filesystem

def gold_checksum(filesystem: list[Block]) -> int:
    big_array = []
    for block in filesystem:
        blockid = block.file_id or 0
        big_array += [blockid] * block.length

    return checksum_fs(big_array)

pprint(f"Silver :{checksum_fs(clean_fs(create_fs(data)))}, Gold :{gold_checksum(clean_gold_fs(create_gold_fs(data)))}")
