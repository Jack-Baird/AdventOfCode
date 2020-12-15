    """Script to create blank python files for each of the AoC challenges, complete with link to the puzzle page.
    """
import os

ROOT = r'C:\Users\Baird\OneDrive\Documents\GitHub\AdventOfCode2020\2020'

dirs = []

for i in range(5, 26):

    day = str(i).zfill(2)

    dir_name = f'D{day}'
    dir_path = os.path.join(ROOT, dir_name)

    if os.path.isdir(dir_path):

        for x in range(1,3):

            file_path = os.path.join(dir_path, f'AoC-2020-{dir_name}-P{x}.py')

            with open(file_path, 'w') as f:

                f.write(f'# AoC 2020, Day {day}, Part {x}\n# https://adventofcode.com/2020/day/{i}')