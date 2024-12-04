#!/usr/bin/env python3
"""Day 4. Ceres Search."""

import operator

from aocd import get_data

puzzle_input = get_data(day=4, year=2024)


print("# ---- Part 1 ----")


def count_search_diagonal(
    grid: list[str],
    target_str: str,
    direction: str = "tlbr",
) -> int:
    """Count occurences of a target string in the grid along diagonals.

    Args:
        grid (list[str]): The grid of characters.
        target_str (str): The string to search for.
        direction (str, optional): The direction of the diagonal to search.
            "tlbr" for top-left to bottom-right.
            "bltr" for bottom-left to top-right.
            Defaults to "tlbr"

    Returns:
        int: The number of times the target string or its reverse is found along
            the specified diagonal.

    """
    rows = len(grid)
    cols = len(grid[0])
    target_len = len(target_str)
    col_range = range(cols - target_len + 1)
    if direction == "tlbr":
        row_range = range(rows - target_len + 1)
        op_f = operator.add
    elif direction == "bltr":
        row_range = range(target_len - 1, rows)
        op_f = operator.sub

    counter: int = 0
    for r in row_range:
        for c in col_range:
            diagonal_str = "".join([grid[op_f(r, i)][c + i] for i in range(target_len)])
            if diagonal_str == target_str or diagonal_str[::-1] == target_str:
                counter += 1

    return counter


grid = puzzle_input.splitlines()
rows: int = len(grid)
cols: int = len(grid[0])
TARGET_STR: str = "XMAS"
TARGET_LEN: int = len(TARGET_STR)
count_occurence: int = 0

# Count horizontal and reverse horizontal
for r in range(rows):
    for c in range(cols - TARGET_LEN + 1):
        horizontal_str = grid[r][c : c + TARGET_LEN]
        if horizontal_str == TARGET_STR or horizontal_str[::-1] == TARGET_STR:
            count_occurence += 1

# Count vertical and reverse vertical
for c in range(cols):
    for r in range(rows - TARGET_LEN + 1):
        vertical_str = "".join([grid[r + i][c] for i in range(TARGET_LEN)])
        if vertical_str == TARGET_STR or vertical_str[::-1] == TARGET_STR:
            count_occurence += 1

# Count diagonal and reverse diagonal
for direction in ["tlbr", "bltr"]:
    count_occurence += count_search_diagonal(grid, TARGET_STR, direction)

print(f"Number of {TARGET_STR} occurences: {count_occurence}")


def search_diag_bltr(
    grid: list[str],
    start_row: int,
    start_col: int,
    target_str: str,
) -> bool:
    """Search for a target string in the grid along the diagonal from bottom-left to top-right.

    Args:
        grid (list[str]): The grid of characters.
        start_row (int): The starting row index.
        start_col (int): The starting column index.
        target_str (str): The string to search for.

    Returns:
        bool: True if the target string or its reverse is found along the diagonal, False otherwise.

    """  # noqa: E501
    target_len = len(target_str)
    diagonal_str = "".join(
        [grid[start_row - i][start_col + i] for i in range(target_len)],
    )
    return bool(diagonal_str == target_str or diagonal_str[::-1] == target_str)


TARGET_STR: str = "MAS"
TARGET_LEN: int = len(TARGET_STR)
count_occurence: int = 0
for r in range(rows - TARGET_LEN + 1):
    for c in range(cols - TARGET_LEN + 1):
        diagonal_str = "".join([grid[r + i][c + i] for i in range(TARGET_LEN)])
        if diagonal_str != TARGET_STR and diagonal_str[::-1] != TARGET_STR:
            continue
        if search_diag_bltr(grid, r + 2, c, TARGET_STR):
            count_occurence += 1

print("# ---- Part 2 ----")
print(f"Number of X-MAS occurences: {count_occurence}")
