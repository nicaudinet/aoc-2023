from itertools import chain

import numpy as np

with open("inputs/day03.txt", "r") as file:
    lines = file.read().splitlines()

test = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def is_digit(char):
    return char in "0123456789"


def is_symbol(char):
    return char not in "0123456789."


def is_near_symbol(neighbors):
    return np.any(np.vectorize(is_symbol)(neighbors))


def line_numbers(line):
    nums = []
    start = None
    for j, char in enumerate(line):
        if is_digit(char) and start is None:
            start = j
        if not is_digit(char) and start is not None:
            nums.append((start, j - 1))
            start = None
    if start is not None:
        nums.append((start, len(line) - 1))
    return nums


def part_numbers(lines):
    grid = np.array([list(line) for line in lines])
    width, height = len(lines[0]), len(lines)
    part_numbers = []
    for i, line in enumerate(lines):
        for start, end in line_numbers(line):
            left = max(start - 1, 0)
            top = max(i - 1, 0)
            right = min(end + 2, width)
            bottom = min(i + 2, height)
            neighbors = grid[top:bottom, left:right]
            if is_near_symbol(neighbors):
                part_numbers.append(int(line[start : end + 1]))
    return part_numbers


print(sum(part_numbers(lines)))


test = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def gear_ratios(lines):
    grid = np.array([list(line) for line in lines])
    width, height = len(lines[0]), len(lines)
    part_numbers = []
    gears = {}
    for i, line in enumerate(lines):
        for start, end in line_numbers(line):
            left = max(start - 1, 0)
            top = max(i - 1, 0)
            right = min(end + 2, width)
            bottom = min(i + 2, height)
            neighbors = grid[top:bottom, left:right]
            stars = np.where(neighbors == "*")
            num = int(line[start : end + 1])
            for x, y in zip(*stars):
                coord = (top + x, left + y)
                if coord not in gears:
                    gears[coord] = [num]
                else:
                    gears[coord].append(num)
    return sum([gear[0] * gear[1] for gear in gears.values() if len(gear) == 2])


print(gear_ratios(lines))
