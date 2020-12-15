# AoC 2020, Day 02, Part 1

import re

expression = r'([0-9]{1,2})-([0-9]{1,2}) ([a-zA-Z]): ([a-zA-Z]*)'

valid_pwords = []
invalid_pwords = []

with open('./input.txt', 'r') as infile:
    pwlist = infile.read().splitlines()

print(f'{len(pwlist)} passwords loaded - examining now...')

for password in pwlist:
    matchObject = re.match(expression, password)

    if matchObject:
        minValue = int(matchObject.group(1))
        maxValue = int(matchObject.group(2))
        letter = matchObject.group(3)
        entry = matchObject.group(4)

        # print(f'Min: {minValue} | Max: {maxValue} | Letter: {letter} | Password: {entry}')

        numLetter = entry.count(letter)

        if minValue <= numLetter <= maxValue:
            valid_pwords.append(entry)

        else:
            invalid_pwords.append(entry)

print(f'Number of VALID passwords: {len(valid_pwords)}')
print(f'Number of INVALID passwords: {len(invalid_pwords)}')