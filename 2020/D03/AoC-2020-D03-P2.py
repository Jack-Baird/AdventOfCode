# AoC 2020, Day 03, Part 2
# https://adventofcode.com/2020/day/3

#[x]: Do the same as Part 1, but also for 3 other slopes
#[x]: For the fifth and final slope, work out how to change the RIGHT:DOWN ratio to 1:2

from math import prod

with open('2020/D03/D03-Input.txt', 'r') as infile:
    frame = infile.read().splitlines()

# List of slope gradients (RIGHT, DOWN)
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

tree_counts = []

for slope in slopes:

    trees = 0

    for i in range(0, len(frame), slope[1]):

        row = frame[i]
        idx = (i * slope[0]) % len(row)

        # print(len(row), idx, 'ERROR' if idx > len(row) else 'OK')

        if row[idx] == '#':

            trees += 1

    tree_counts.append(trees)

print(f'Combined, all slopes have {prod(tree_counts)} trees along their given paths!')