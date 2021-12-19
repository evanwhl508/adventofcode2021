from typing import List


class RiskMap:
    def __init__(self, matrix, max_row, max_col):
        self.matrix = matrix
        self.max_row = max_row
        self.max_col = max_col

    def east(self, row, col):
        if col == self.max_col:
            return 999
        else:
            return self.matrix[row][col + 1]

    def south_east(self, row, col):
        if col == self.max_col or row == self.max_row:
            return 999
        else:
            return self.matrix[row + 1][col + 1]

    def south(self, row, col):
        if row == self.max_row:
            return 999
        else:
            return self.matrix[row + 1][col]

    def south_west(self, row, col):
        if row == self.max_row or col == 0:
            return 999
        else:
            return self.matrix[row + 1][col - 1]

    def west(self, row, col):
        if col == 0:
            return 999
        else:
            return self.matrix[row][col - 1]

    def north_west(self, row, col):
        if col == 0 or row == 0:
            return 999
        else:
            return self.matrix[row - 1][col - 1]

    def north(self, row, col):
        if row == 0:
            return 999
        else:
            return self.matrix[row - 1][col]

    def north_east(self, row, col):
        if col == self.max_col or row == 0:
            return 999
        else:
            return self.matrix[row - 1][col + 1]

    def compare_to_adjacent(self, i, j):
        if self.matrix[i][j] < self.east(i, j) and \
                self.matrix[i][j] < self.south_east(i, j) and \
                self.matrix[i][j] < self.south(i, j) and \
                self.matrix[i][j] < self.south_west(i, j) and \
                self.matrix[i][j] < self.west(i, j) and \
                self.matrix[i][j] < self.north_west(i, j) and \
                self.matrix[i][j] < self.north(i, j) and \
                self.matrix[i][j] < self.north_east(i, j):
            return self.matrix[i][j]
        else:
            return -1


class BasinMap:
    def __init__(self, matrix, max_row, max_col):
        self.matrix = matrix
        self.max_row = max_row
        self.max_col = max_col
        self.checked_location: List[tuple] = list()

    def east(self, row, col):
        if col == self.max_col:
            return 9
        else:
            return self.matrix[row][col + 1]

    def south_east(self, row, col):
        if col == self.max_col or row == self.max_row:
            return 9
        else:
            return self.matrix[row + 1][col + 1]

    def south(self, row, col):
        if row == self.max_row:
            return 9
        else:
            return self.matrix[row + 1][col]

    def south_west(self, row, col):
        if row == self.max_row or col == 0:
            return 9
        else:
            return self.matrix[row + 1][col - 1]

    def west(self, row, col):
        if col == 0:
            return 9
        else:
            return self.matrix[row][col - 1]

    def north_west(self, row, col):
        if col == 0 or row == 0:
            return 9
        else:
            return self.matrix[row - 1][col - 1]

    def north(self, row, col):
        if row == 0:
            return 9
        else:
            return self.matrix[row - 1][col]

    def north_east(self, row, col):
        if col == self.max_col or row == 0:
            return 9
        else:
            return self.matrix[row - 1][col + 1]

    def compare_to_adjacent(self, i, j):
        if (i, j) in self.checked_location:
            return []
        self.checked_location.append((i, j))
        if self.matrix[i][j] == 9:
            return []
        basin = [(i, j)]
        if self.east(i, j) < 9:
            basin.extend(self.compare_to_adjacent(i, j + 1))
        if self.south(i, j) < 9:
            basin.extend(self.compare_to_adjacent(i+1, j))
        if self.west(i, j) < 9:
            basin.extend(self.compare_to_adjacent(i, j-1))
        if self.north(i, j) < 9:
            basin.extend(self.compare_to_adjacent(i-1, j))
        return basin


def compare_adjacent_elements(matrix: List[List[int]]):
    low_risk_list = list()
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    risk_map = RiskMap(matrix, max_row, max_col)
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            result = risk_map.compare_to_adjacent(i, j)
            low_risk_list.append(result + 1)
    return sum(low_risk_list)


def part1(data: List[List[int]]):
    return compare_adjacent_elements(data)


def find_basins(matrix: List[List[int]]) -> List[int]:
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    basins_map = BasinMap(matrix, max_row, max_col)
    basins_list = []
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            basin = basins_map.compare_to_adjacent(i, j)
            basins_list.append(len(basin))
    return basins_list


def part2(data: List[List[int]]):
    basins = find_basins(data)
    basins.sort(reverse=True)
    largest_basins = basins[:3]
    result = 1
    for num in largest_basins:
        result *= num
    return result


if __name__ == '__main__':
    with open('data/D9_input.txt') as f:
        data = f.readlines()
    data = [[int(num) for num in d.replace("\n", "")] for d in data]
    res = part1(data)
    print(f"Part 1 = {res}")
    res = part2(data)
    print(f"Part 2 = {res}")

