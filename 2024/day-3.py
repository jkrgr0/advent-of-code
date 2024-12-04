#!/usr/bin/env python3
"""Day 3. Mull It Over."""

import re
from functools import reduce
from operator import mul

from aocd import get_data

puzzle_input = get_data(day=3, year=2024)


def prod(val_tuple: tuple[int]) -> int:
    """Calculate the product of all integers in a tuple.

    Args:
        val_tuple (tuple[int]): A tuple containing integer values.

    Returns:
        int: The product of all integers in the tuple.

    """
    int_tuple = tuple(int(val) for val in val_tuple)
    return reduce(mul, int_tuple, 1)


print("# ---- Part 1 ----")

sum_mul: int = 0
MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
for line in puzzle_input.splitlines():
    sum_mul += sum([prod(instr) for instr in MUL_RE.findall(line)])

print(f"Sum of all valid mul instructions: {sum_mul}")

print("# ---- Part 2 ----")

sum_mul: int = 0
INSTR_RE = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
mul_enabled: bool = True
for line in puzzle_input.splitlines():
    for instr in INSTR_RE.findall(line):
        if instr[0] == "do()":
            mul_enabled = True
        elif instr[0] == "don't()":
            mul_enabled = False
        elif mul_enabled and instr[0].startswith("mul"):
            sum_mul += prod(instr[1:])

print(f"Sum of all valid mul instructions: {sum_mul}")
