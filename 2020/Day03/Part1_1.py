RIGHT = 3 + 1
DOWN = 1

rows = 0
blanks = 0
trees = 0

with open('./input.txt', 'r') as infile:
    data = infile.read().splitlines()

line_no = 0

for line in data:
    line_no += 1

    index = (line_no % len(line)) + 3

    if line[index] == '#':
        trees += 1
    elif line[index] == '.':
        blanks += 1

print(blanks, trees, blanks + trees)