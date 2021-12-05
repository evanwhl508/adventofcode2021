from typing import List
import numpy as np


def part1(data: List[List[List[str]]]):
    map = np.zeros((1000, 1000))
    for coord_start, coord_end in data:
        x_start = int(coord_start[0])
        y_start = int(coord_start[1])
        x_end = int(coord_end[0])
        y_end = int(coord_end[1])
        if x_start == x_end:
            row = x_start
            if y_start > y_end:
                start = y_end
                end = y_start + 1
            else:
                start = y_start
                end = y_end + 1
            for col in range(start, end):
                map[row, col] += 1
        elif y_start == y_end:
            col = y_start
            if x_start > x_end:
                start = x_end
                end = x_start + 1
            else:
                start = x_start
                end = x_end + 1
            for row in range(start, end):
                map[row, col] += 1
    rows, cols = np.where(map >= 2)
    return len(rows)


def part2(data: List[List[List[str]]]):
    map = np.zeros((1000, 1000))
    for coord_start, coord_end in data:
        x_start = int(coord_start[0])
        y_start = int(coord_start[1])
        x_end = int(coord_end[0])
        y_end = int(coord_end[1])
        if x_start == x_end:
            row = x_start
            if y_start > y_end:
                start = y_end
                end = y_start + 1
            else:
                start = y_start
                end = y_end + 1
            for col in range(start, end):
                map[row, col] += 1
        elif y_start == y_end:
            col = y_start
            if x_start > x_end:
                start = x_end
                end = x_start + 1
            else:
                start = x_start
                end = x_end + 1
            for row in range(start, end):
                map[row, col] += 1
        else:
            row = x_start
            col = y_start
            while True:
                if x_start > x_end > row or x_start < x_end < row or y_start > y_end > col or y_start < y_end < col:
                    break
                map[row, col] += 1
                if x_start > x_end:
                    row -= 1
                else:
                    row += 1
                if y_start > y_end:
                    col -= 1
                else:
                    col += 1
    rows, cols = np.where(map >= 2)
    return len(rows)


if __name__ == '__main__':
    with open('data/D5_input.txt') as f:
        data = f.readlines()
    data = [[cor.split(",") for cor in d.replace("\n", "").split(" -> ")] for d in data]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")
