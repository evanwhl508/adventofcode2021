import math
from typing import List

import numpy as np


def part1(fish_queue: List[int]):
    days = 80
    temp_fish_queue = fish_queue.copy()
    fish_list = [[fish for fish in temp_fish_queue if fish == i] for i in range(9)]
    for day in range(days):
        born_fish = fish_list.pop(0)
        fish_list[6].extend(born_fish)
        fish_list.append(born_fish)
    return sum([len(fish) for fish in fish_list])


def part2(fish_queue: List[int]):
    days = 256
    temp_fish_queue = fish_queue.copy()
    fish_list = [[fish for fish in temp_fish_queue if fish == i] for i in range(9)]
    fish_list = [len(fish) for fish in fish_list]
    for day in range(days):
        born_fish = fish_list.pop(0)
        fish_list[6] += born_fish
        fish_list.append(born_fish)
    return sum(fish_list)


if __name__ == '__main__':
    with open('data/D6_input.txt') as f:
        data = f.readlines()
    data = [int(d) for d in data[0].replace("\n", "").split(",")]
    print(f'initial fish = {len(data)}')
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")