import math
from typing import List

import numpy as np


def part1(submarines_position: List[int]):
    max_position = max(submarines_position)
    min_position = min(submarines_position)
    least_fuels = None
    for target in range(min_position, max_position + 1):
        total_fuels = sum([abs(position - target) for position in submarines_position])
        if least_fuels is None:
            least_fuels = total_fuels
        elif total_fuels < least_fuels:
            least_fuels = total_fuels
    return least_fuels


def part2(submarines_position: List[int]):
    max_position = max(submarines_position)
    min_position = min(submarines_position)
    least_fuels = None
    for target in range(min_position, max_position + 1):
        # n * (n + 1) / 2 = 1 + 2 + 3 + ... + n
        total_fuels = sum([int((abs(position - target) + 1) * abs(position - target) / 2) for position in submarines_position])
        if least_fuels is None:
            least_fuels = total_fuels
        elif total_fuels < least_fuels:
            least_fuels = total_fuels
    return least_fuels


if __name__ == '__main__':
    with open('data/D7_input.txt') as f:
        data = f.readlines()
    data = [int(d) for d in data[0].replace("\n", "").split(",")]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")