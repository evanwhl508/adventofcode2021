from typing import List


def part1(data: List[int]):
    counter = 0
    last_value = None
    for d in data:
        if not last_value:
            last_value = d
            continue
        cur_value = d
        if cur_value > last_value:
            counter += 1
        last_value = cur_value
    return counter


def part2(data: List[int]):
    new_data = [sum([data[i], data[i+1], data[i+2]]) for i, d in enumerate(data) if i < len(data) - 2]
    res = part1(new_data)
    return res


if __name__ == '__main__':
    with open('data/D1_input.txt') as f:
        data = f.readlines()
    data = [int(d.replace("\n", "")) for d in data]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
