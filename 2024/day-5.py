#!/usr/bin/env python3
"""Day 4. Print Queue.

Credits to nitekat1124 as I had absolutely no idea how to solve this.
"""

from collections import defaultdict

from aocd import get_data

puzzle_input = get_data(day=5, year=2024)


def extract_data(data: list[str]) -> tuple[defaultdict[set], list[list[int]]]:
    """Parse input data into dependency rules and a list of update sequences.

    Args:
        data (list[str]): A list of strings where the first section defines the rules
            in the format "a|b" and the second section defines the update sequence in
            the format "x,y,z".

    Returns:
        tuple[defaultdict[set], list[list[int]]]:
            - A defaultdict representing dependency rules.
            - A list of update sequences.

    """
    separator = data.index("")

    rules = defaultdict(set)
    for i in data[:separator]:
        a, b = map(int, i.split("|"))
        rules[a].add(b)

    updates = [list(map(int, i.split(","))) for i in data[separator + 1 :]]

    return rules, updates


def is_valid(rules: defaultdict[set], update: list[int]) -> bool:
    """Validate whether the provided update sequence satisfies the dependency rules.

    Args:
        rules (defaultdict[set]): A mapping of items to their allowed dependencies.
        update (list[int]): A list of updates to validate.

    Returns:
        bool: True if the update sequence is valid, False otherwise.

    """
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True


def fix_update(rules: defaultdict[set], update: list[int]) -> list[int]:
    """Filter and sort a list of updates based on the given rules.

    Args:
        rules (defaultdict[set]): A mapping of items to their allowed dependencies.
        update (list[int]): A list of updates to process.

    Returns:
        list[int]: A sorted list of updates prioritized by the number of dependencies
            they have, in descending order.

    """
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = rules[i] & set(update)

    return sorted(filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True)


rules, updates = extract_data(puzzle_input.splitlines())

print("# ---- Part 1 ----")

sum_middle_pages: int = 0
for update in updates:
    if is_valid(rules, update):
        sum_middle_pages += update[len(update) // 2]

print(f"Sum of all middle pages from valid updates: {sum_middle_pages}")

print("# ---- Part 2 ----")

sum_fixed_middle_pages: int = 0
for update in updates:
    if not is_valid(rules, update):
        fixed_update = fix_update(rules, update)
        sum_fixed_middle_pages += fixed_update[len(fixed_update) // 2]

print(f"Sum of all middle pages from fixed updates: {sum_fixed_middle_pages}")
