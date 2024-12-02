#!/usr/bin/env python3
"""Day 1: Historian Hysteria."""

from aocd import get_data

puzzle_input = get_data(day=1, year=2024)

left_table: list[int] = []
right_table: list[int] = []

for line in puzzle_input.splitlines():
    left_item, right_item = line.split("   ")
    left_table.append(int(left_item))
    right_table.append(int(right_item))

left_table.sort(reverse=True)
right_table.sort(reverse=True)

total_distance: int = 0

for i in range(len(left_table)):
    distance = left_table[i] - right_table[i]
    if distance < 0:
        distance = right_table[i] - left_table[i]

    total_distance += distance

print(f"Total distance is: {total_distance}")

# ---- Part 2 ----

similarity_score: int = 0

for i in range(len(left_table)):
    occurence_right = right_table.count(left_table[i])
    similarity_score += left_table[i] * occurence_right

print(f"Similarity score is: {similarity_score}")
