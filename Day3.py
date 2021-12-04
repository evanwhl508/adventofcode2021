from typing import List


def part1(data: List[str]) -> tuple:
    data_dict = dict()
    for d in data:
        for i, char in enumerate(d):
            if i not in data_dict:
                data_dict[i] = list(char)
            else:
                data_dict[i].append(char)
    gamma = ""
    epsilon = ""
    for key in data_dict:
        if data_dict[key].count("0") > data_dict[key].count("1"):
            gamma = f"{gamma}{0}"
            epsilon = f"{epsilon}{1}"
        else:
            gamma = f"{gamma}{1}"
            epsilon = f"{epsilon}{0}"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma, epsilon


def check_most_common_bit(data: List[str], position):
    list_0 = [d for d in data if d[position] == "0"]
    if len(list_0) > int(len(data) / 2):
        return "0"
    return "1"


def check_least_common_bit(data: List[str], position):
    list_0 = [d for d in data if d[position] == "0"]
    if len(list_0) <= int(len(data) / 2):
        return "0"
    return "1"


def part2(data: List[str]) -> tuple:
    oxygen_list = data.copy()
    co2_list = data.copy()
    for index in range(len(data[0])):
        oxygen_list = [d for d in oxygen_list if d[index] == check_most_common_bit(oxygen_list, index)] if len(oxygen_list) > 1 else oxygen_list
        co2_list = [d for d in co2_list if d[index] == check_least_common_bit(co2_list, index)] if len(co2_list) > 1 else co2_list
    oxygen = oxygen_list[0]
    co2 = co2_list[0]
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)
    return oxygen, co2


if __name__ == '__main__':
    with open('data/D3_input.txt') as f:
        data = f.readlines()
    data = [d.replace("\n", "") for d in data]
    gamma, epsilon = part1(data)
    print(f"Part 1 = {gamma*epsilon}")
    oxygen, co2 = part2(data)
    print(f"Part 2 = {oxygen*co2}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
