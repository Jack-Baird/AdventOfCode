import re

expression = r'([0-9]{1,2})-([0-9]{1,2}) ([a-zA-Z]): ([a-zA-Z]*)'

valid_pwords = []
invalid_pwords = []

with open('./input.txt', 'r') as infile:
    pwlist = infile.read().splitlines()

print(f'{len(pwlist)} passwords loaded - examining now...')

numPwords = 0

for password in pwlist:
    matchObject = re.match(expression, password)

    numPwords += 1

    if matchObject:
        pos1 = int(matchObject.group(1))
        pos2 = int(matchObject.group(2))
        letter = matchObject.group(3)
        entry = matchObject.group(4)

        # print(f'Min: {minValue} | Max: {maxValue} | Letter: {letter} | Password: {entry}')
        print(f'Entry number: {numPwords} ({entry}) | {len(entry)} digits; looking for {letter} in positions {pos1} or {pos2}')

        if pos1 <= (len(entry) + 1) and pos2 <= (len(entry) + 1):
            if (entry[pos1 - 1] == letter or entry[pos2 - 1] == letter) and not (entry[pos1 - 1] == letter and entry[pos2 - 1] == letter):
                valid_pwords.append(entry)
            else:
                invalid_pwords.append(entry)

print(f'Number of VALID passwords: {len(valid_pwords)}')
print(f'Number of INVALID passwords: {len(invalid_pwords)}')