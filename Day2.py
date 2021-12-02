from typing import List


def part1(data: List[tuple]) -> tuple:
    total = 0
    value = 0
    for direction, moving_unit in data:
        if direction == "forward":
            total += moving_unit
        elif direction == "up":
            value -= moving_unit
        elif direction == "down":
            value += moving_unit
    return total, value


def part2(data: List[tuple]) -> tuple:
    total = 0
    aim = 0
    depth = 0
    for direction, moving_unit in data:
        if direction == "forward":
            total += moving_unit
            depth += aim * moving_unit
        elif direction == "up":
            aim -= moving_unit
        elif direction == "down":
            aim += moving_unit
    return total, depth


if __name__ == '__main__':
    with open('data/D2_input.txt') as f:
        data = f.readlines()
    data = [d.replace("\n", "").split(" ") for d in data]
    data = [(d[0], int(d[1])) for d in data]
    total, value = part1(data)
    print(f"Part 1 = {total*value}")
    total, aim = part2(data)
    print(f"Part 2 = {total*aim}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
