from typing import List

import numpy as np


def check_rows_all_1(arr):
    result = np.all((arr == 1), axis=1)
    for i in range(len(result)):
        if result[i]:
            return result[i]
    return None


def check_cols_all_1(arr):
    result = np.all((arr == 1), axis=0)
    for i in range(len(result)):
        if result[i]:
            return result[i]
    return None


def get_unmark(ref_board, arr) -> List:
    unmark = []
    rows, cols = np.where(ref_board == 0)

    for row, col in zip(rows, cols):
        unmark.append(arr[row][col])
    return unmark


def part1(board_list: List[List[List[int]]], drawn_num: List[int]):
    ref_board_list = [np.zeros((len(board), len(board[0]))) for board in board_list]
    for num in drawn_num:
        for i, board in enumerate(board_list):
            arr = board
            rows, cols = np.where(arr == num)
            if len(rows) > 0:
                ref_board_list[i][rows, cols] = 1
            row = check_rows_all_1(ref_board_list[i])
            if row:
                res = get_unmark(ref_board_list[i], arr)
                return sum(res) * num
            col = check_cols_all_1(ref_board_list[i])
            if col:
                res = get_unmark(ref_board_list[i], arr)
                return sum(res) * num
    return 0


def part2(board_list: List[List[List[int]]], drawn_num: List[int]):
    ref_board_list = [np.zeros((len(board), len(board[0]))) for board in board_list]
    won_boards_index = []
    for num in drawn_num:
        for i, board in enumerate(board_list):
            if i in won_boards_index:
                continue
            arr = board
            rows, cols = np.where(arr == num)
            if len(rows) > 0:
                ref_board_list[i][rows, cols] = 1
            row = check_rows_all_1(ref_board_list[i])
            if row:
                res = get_unmark(ref_board_list[i], arr)
                won_boards_index.append(i)
                if len(won_boards_index) == len(board_list):
                    return sum(res) * num
                continue
            col = check_cols_all_1(ref_board_list[i])
            if col:
                res = get_unmark(ref_board_list[i], arr)
                won_boards_index.append(i)
                if len(won_boards_index) == len(board_list):
                    return sum(res) * num
                continue
    return 0


if __name__ == '__main__':
    with open('data/D4_input.txt') as f:
        data = f.readlines()
    drawn_num = [int(d) for d in data[0].split(",") if d != "\n"]
    board_data = data[2:]
    temp = []
    board_list = []
    for d in board_data:
        if d == "\n":
            board_list.append(temp)
            temp = []
            continue
        temp.append([int(n) for n in d.replace("\n", "").split(" ") if n != ""])
    else:
        board_list.append(temp)
    board_list = [np.array(board) for board in board_list]
    res = part1(board_list, drawn_num)
    print(f"Part 1 = {res}")
    res = part2(board_list, drawn_num)
    print(f"Part 2 = {res}")

