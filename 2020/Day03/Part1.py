import time
start_time = time.time()

rows = 0
blanks = 0
trees = 0

with open('./input.txt', 'r') as infile:
    data = infile.read().splitlines()

print('Data in...') #! DEBUGGING

positions = [0]

for _ in range(len(data) + 1):
    positions.append(positions[-1] + 3)

print('Calculated positions...') #! DEBUGGING
print('Running scenario...') #! DEBUGGING

row = 0

for line in data:
    rows += 1
    #print(f'Running line {row}...') #! DEBUGGING
    try:
        position = positions[row]

        if position > (len(line) + 1):
            for _ in range(int(position / len(line))):
                line += line
        #print(f'Line length: {len(line)}') #! DEBUGGING
        item = line[position]

        if item == '.':
            blanks += 1
        elif item == '#':
            trees += 1

        #print(row, item)
        row += 1

    except MemoryError as e:
        print(f'{e}\nRow {row}\nRows: {rows} | Blanks: {blanks} | Trees: {trees}')
        execution_time = (time.time() - start_time)
        if execution_time <= 60:
            print(f'Execution time: {execution_time} seconds')
        else:
            print(f'Execution time: {int(execution_time / 60)}m {int(execution_time % 60)}s')

print(f'Rows: {rows} | Blanks: {blanks} | Trees: {trees}')

execution_time = (time.time() - start_time)
if execution_time <= 60:
    print(f'Execution time: {execution_time} seconds')
else:
    print(f'Execution time: {int(execution_time / 60)}m {int(execution_time % 60)}s')