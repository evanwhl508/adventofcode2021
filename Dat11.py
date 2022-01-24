from typing import List

import numpy as np


class Octopus:
    def __init__(self, matrix, max_row, max_col):
        self.matrix = matrix
        self.max_row = max_row - 1
        self.max_col = max_col - 1
        self.total_flashes = 0

    def east(self, row, col):
        if col == self.max_col:
            pass
        else:
            if self.matrix[row][col + 1] > 0:
                self.matrix[row][col + 1] += 1

    def south_east(self, row, col):
        if col == self.max_col or row == self.max_row:
            pass
        else:
            if self.matrix[row + 1][col + 1] > 0:
                self.matrix[row + 1][col + 1] += 1

    def south(self, row, col):
        if row == self.max_row:
            pass
        else:
            if self.matrix[row + 1][col] > 0:
                self.matrix[row + 1][col] += 1

    def south_west(self, row, col):
        if row == self.max_row or col == 0:
            pass
        else:
            if self.matrix[row + 1][col - 1] > 0:
                self.matrix[row + 1][col - 1] += 1

    def west(self, row, col):
        if col == 0:
            pass
        else:
            if self.matrix[row][col - 1] > 0:
                self.matrix[row][col - 1] += 1

    def north_west(self, row, col):
        if col == 0 or row == 0:
            pass
        else:
            if self.matrix[row - 1][col - 1] > 0:
                self.matrix[row - 1][col - 1] += 1

    def north(self, row, col):
        if row == 0:
            pass
        else:
            if self.matrix[row - 1][col] > 0:
                self.matrix[row - 1][col] += 1

    def north_east(self, row, col):
        if col == self.max_col or row == 0:
            pass
        else:
            if self.matrix[row - 1][col + 1] > 0:
                self.matrix[row - 1][col + 1] += 1

    def update_adjacent_octopus(self, row, col):
        self.east(row, col)
        self.south_east(row, col)
        self.south(row, col)
        self.south_west(row, col)
        self.west(row, col)
        self.north_west(row, col)
        self.north(row, col)
        self.north_east(row, col)

    def check_flash(self):
        while True:
            again = False
            for row in range(self.max_row + 1):
                for col in range(self.max_col + 1):
                    if self.matrix[row][col] > 9:
                        self.matrix[row][col] = 0
                        self.total_flashes += 1
                        self.update_adjacent_octopus(row, col)
                        again = True
                    elif self.matrix[row][col] == 0:
                        continue
            if not again:
                break


def part1(data: List[str]):
    data = [[int(integer) for integer in str_list] for str_list in data]
    matrix = np.array(data)
    steps = 100
    row_len = len(matrix)
    col_len = len(matrix[0])
    octopus_map = Octopus(matrix, row_len, col_len)
    for i in range(steps):
        octopus_map.matrix = octopus_map.matrix + 1
        octopus_map.check_flash()

    return octopus_map.total_flashes


def part2(data: List[str]):
    data = [[int(integer) for integer in str_list] for str_list in data]
    matrix = np.array(data)
    row_len = len(matrix)
    col_len = len(matrix[0])
    octopus_map = Octopus(matrix, row_len, col_len)
    steps = 1
    while True:
        init_total_flashes = octopus_map.total_flashes
        octopus_map.matrix = octopus_map.matrix + 1
        octopus_map.check_flash()
        final_total_flashes = octopus_map.total_flashes
        if final_total_flashes - init_total_flashes == row_len * col_len:
            break
        steps += 1
    return steps


if __name__ == '__main__':
    with open('data/D11_input.txt') as f:
        data = f.readlines()
    data = [d.replace("\n", "") for d in data]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")
