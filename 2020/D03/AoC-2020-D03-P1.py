# AoC 2020, Day 03, Part 1
# https://adventofcode.com/2020/day/3

#[x]: Read in input from text file
#[x]: Iterate over lines, moving RIGHT 3 each time you move down 1
#[x]: Repeat input frame as required if idx > len(frame)
#[x]: Determine how many trees (#) would be encountered on the way down the slope

with open('2020/D03/D03-Input.txt', 'r') as infile:
    frame = infile.read().splitlines()

trees = 0

for i in range(len(frame)):

    row = frame[i]
    idx = (i * 3) % len(row)

    # print(len(row), idx, 'ERROR' if idx > len(row) else 'OK')

    if row[idx] == '#':

        trees += 1

print(f'Riding on this slope, you would encouter {trees} trees!')