#!/usr/bin/env python3
"""Day 3. Mull It Over."""

import re

from aocd import get_data

puzzle_input = get_data(day=3, year=2024)

print("# ---- Part 1 ----")

sum_mul: int = 0
MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
for line in puzzle_input.splitlines():
    matches = MUL_RE.findall(line)
    for match in matches:
        mul_result = int(match[0]) * int(match[1])
        sum_mul += mul_result

print(f"Sum of all valid mul instructions: {sum_mul}")

print("# ---- Part 2 ----")


def prod(val_tuple: tuple) -> int:
    res = 1
    for val in val_tuple:
        res *= int(val)
    return res


sum_mul: int = 0
MUL_RE = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
DO_RE = re.compile(r"do\(\)")
DONT_RE = re.compile(r"don't?\(\)")
mul_enabled: bool = True
for line in puzzle_input.splitlines():
    mul_matches = MUL_RE.finditer(line)
    do_matches = DO_RE.finditer(line)
    do_inst: list[int] = [0, *[idx.start() for idx in do_matches]]
    dont_matches = DONT_RE.finditer(line)
    dont_inst: list[int] = [idx.start() for idx in dont_matches]
    for mul_inst in mul_matches:
        if do_inst[0] < mul_inst.start() < dont_inst[0]:
            sum_mul += prod(mul_inst.groups())
        else:
            if do_inst[1] > mul_inst.start():
                _ = do_inst.pop(0)
            if dont_inst[0] < do_inst[0]:
                _ = dont_inst.pop(0)


print(f"Sum of all valid mul instructions: {sum_mul}")
