import math
from typing import List

import numpy as np


def part1(digit_list: List[List[str]]):
    digit_map = {2: "1", 3: "7", 4: "4", 7: "8"}
    count = 0
    for digits in digit_list:
        count += len([d for d in digits if len(d) in digit_map])
    return count


def generate_digit_set(signal_list: List[str]):
    digit_map = dict()
    signal_list = signal_list[0:-1]
    for signal in signal_list:
        length = len(signal)
        if length == 2:
            digit_map["1"] = set(signal)
        elif length == 4:
            digit_map["4"] = set(signal)
        elif length == 3:
            digit_map["7"] = set(signal)
        elif length == 7:
            digit_map["8"] = set(signal)
    for signal in signal_list:
        length = len(signal)
        if length in [2, 3, 4, 7]:
            continue
        elif length == 5:  # 2, 3, 5
            continue
        elif length == 6:  # 0, 6, 9
            if all([char in signal for char in digit_map["4"]]):
                digit_map["9"] = set(signal)
            elif all([char in signal for char in digit_map["1"]]):
                digit_map["0"] = set(signal)
            else:
                digit_map["6"] = set(signal)
    for signal in signal_list:
        length = len(signal)
        if length in [2, 3, 4, 6, 7]:
            continue
        elif length == 5:  # 2, 3, 5
            if all([char in signal for char in digit_map["1"]]):
                digit_map["3"] = set(signal)
            elif all([char in digit_map["6"] for char in signal]):
                digit_map["5"] = set(signal)
            else:
                digit_map["2"] = set(signal)
    return digit_map


def part2(digit_list: List[List[str]]):
    numbers = []
    for analyse, digits in digit_list:
        seven_segment = generate_digit_set(analyse.split(" "))
        number = ""
        for digit in digits.split(" "):
            digit_set = set(digit)
            for key, value in seven_segment.items():
                if digit_set == value:
                    number += key
        numbers.append(int(number))
    return sum(numbers)


if __name__ == '__main__':
    with open('data/D8_input.txt') as f:
        data = f.readlines()
    part1_data = [d.replace("\n", "").split("|")[1].split(" ")[1:] for d in data]
    res = part1(part1_data)
    print(f"Part 1 = {res}")
    part2_data = [d.replace("\n", "").split("|") for d in data]
    res = part2(part2_data)
    print(f"Part 2 = {res}")