from typing import List


def open_close_mapping(sign: str):
    return {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }[sign]


def part1(data: List[str]):
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]
    error_list = []
    for line in data:
        open_bracket_queue = []
        for sign in line:
            if sign in open_brackets:
                open_bracket_queue.append(sign)
            elif sign in close_brackets:
                open = open_bracket_queue.pop()
                close = sign
                if open_close_mapping(close) != open:
                    error_list.append(sign)
                    break
    res = 0
    for s in error_list:
        if s == ")":
            res += 3
        elif s == "]":
            res += 57
        elif s == "}":
            res += 1197
        elif s == ">":
            res += 25137
    return res


def part2(data: List[str]):
    open_brackets = ["(", "[", "{", "<"]
    close_brackets = [")", "]", "}", ">"]
    res_list = []
    for line in data:
        to_be_broken = False
        open_bracket_queue = []
        for sign in line:
            if sign in open_brackets:
                open_bracket_queue.append(sign)
            elif sign in close_brackets:
                open = open_bracket_queue.pop()
                close = sign
                if open_close_mapping(close) != open:
                    to_be_broken = True
                    break
        if to_be_broken:
            continue
        res = 0
        open_bracket_queue.reverse()
        for s in open_bracket_queue:
            res *= 5
            if s == "(":
                res += 1
            elif s == "[":
                res += 2
            elif s == "{":
                res += 3
            elif s == "<":
                res += 4
        res_list.append(res)
    res_list.sort()
    middle = res_list[int(len(res_list)/2)]
    return middle


if __name__ == '__main__':
    with open('data/D10_input.txt') as f:
        data = f.readlines()
    data = [d.replace("\n", "") for d in data]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")
