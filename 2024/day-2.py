#!/usr/bin/env python3
"""Day 2. Red-Nosed Reports."""

from copy import deepcopy
from itertools import pairwise

from aocd import get_data

puzzle_input = get_data(day=2, year=2024)


def parse_puzzle_input(raw_data_str: str) -> list[int]:
    """Parse a string containing lines of space-separated integers into a list of integer lists.

    Args:
        raw_data_str (str): A string where each line contains space-separated integers.

    Returns:
        list[int]: A list of lists, where each inner list contains integers parsed from a line.

    """  # noqa: E501
    return [list(map(int, line.split())) for line in raw_data_str.splitlines()]


def is_increasing(values: list[int]) -> bool:
    """Test if the values in the list are increasing.

    Args:
        values (list[int]): The values to test.

    Returns:
        bool: True if the values in the list are increasing, False otherwise.

    """
    return all(i < j for i, j in pairwise(values))


def is_decreasing(values: list[int]) -> bool:
    """Test if the values in the list are decreasing.

    Args:
        values (list[int]): The values to test.

    Returns:
        bool: True if the values in the list are decreasing, False otherwise.

    """
    return all(i > j for i, j in pairwise(values))


def is_diff_safe(values: list[int], min_diff: int = 1, max_diff: int = 3) -> bool:
    """Test if the difference in all value pairs are safe.

    Args:
        values (list[int]): The values to test.
        min_diff (int, optional): The minimum difference. Defaults to 1.
        max_diff (int, optional): The maximum difference. Defaults to 3.

    Returns:
        bool: True if the difference for all values is safe, False otherwise.

    """
    return all(min_diff <= abs(i - j) <= max_diff for i, j in pairwise(values))


def is_safe_report(values: list[int]) -> bool:
    """Test if the given report is safe.

    A report is safe if both of the following values are true:
    - The levels are either *all increasing* or *all descending*.
    - Any two adjacent levels differ by *at least one* and *at most three*.

    Args:
        values (list[int]): The values to test.

    Returns:
        bool: True if the report is safe, False otherwise.

    """
    return bool(
        (is_increasing(values) or is_decreasing(values)) and is_diff_safe(values),
    )


def is_safe_report_tolerate_single(values: list[int]) -> bool:
    """Test if the given report is safe but tolerates a single bad level.

    A report is safe if both of the following values are true:
    - The levels are either *all increasing* or *all descending*.
    - Any two adjacent levels differ by *at least one* and *at most three*.

    Args:
        values (list[int]): The values to test.

    Returns:
        bool: True if the report is safe, False otherwise.

    """
    if is_safe_report(values):
        return True

    for i in range(len(values)):
        tolerated_values = deepcopy(values)
        _ = tolerated_values.pop(i)
        if is_safe_report(tolerated_values):
            return True

    return False


print("# ---- Part 1 ----")

count_safe_reports: int = 0
for value_list in parse_puzzle_input(puzzle_input):
    if is_safe_report(value_list):
        count_safe_reports += 1

print(f"Number of safe reports: {count_safe_reports}")

# ---- Part 2 ----
print("# ---- Part 2 ----")


count_safe_reports_tolerated: int = 0
for value_list in parse_puzzle_input(puzzle_input):
    if is_safe_report_tolerate_single(value_list):
        count_safe_reports_tolerated += 1

print(
    "Number of safe reports after tolerating a "
    f"single bad level: {count_safe_reports_tolerated}",
)
