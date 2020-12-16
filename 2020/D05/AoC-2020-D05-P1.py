# AoC 2020, Day 05, Part 1
# https://adventofcode.com/2020/day/5

#[x]: Read in input data
#[x]: Create a boarding pass instance
#[x]: Parse boarding pass to determine row and column
#[x]: Calculate seat ID and add to list
#[x]: Find the highest seat ID in the list

test_data = [
    'BFFFBBFRRR', # row 70, col 7, seat ID 567
    'FFFBBBFRRR', # row 14, col 7, seat ID 119
    'BBFFBBFRLL'  # row 102, col 4, seat ID 820
]

INPUT = '2020/D05/D05-Input.txt'

# Read in input data
def read_data(filename):
    with open(filename, 'r') as infile:
        return infile.read().splitlines()

# Create a boarding pass instance
class BoardingPass:
    def __init__(self, pass_num):
        self.pass_num = pass_num
        self.row_id = pass_num[:7]
        self.col_id = pass_num[7:]
        self.row = 0
        self.col = 0
        self.seat = 0

    # Parse the bp to determine row
    def identify_row(self):
        row_min = 0
        row_max = 127
        for char in self.row_id:
            row_range = row_max - row_min
            if char == 'F':
                row_max = int(row_min + (row_range / 2))

            if char == 'B':
                row_min = int((row_max - (row_range /2)) + 1)

        self.row = row_min
        return self.row

    # Parse the bp to determine col
    def identify_col(self):
        col_min = 0
        col_max = 7
        for char in self.col_id:
            col_range = col_max - col_min
            if char == 'L':
                col_max = int(col_min + (col_range / 2))

            if char == 'R':
                col_min = int((col_max - (col_range /2)) + 1)

        self.col = col_min
        return self.col

    # Calculate seat ID
    def identify_seat(self):
        self.seat = (self.row * 8) + self.col
        return self.seat

    def position(self):
        self.identify_row()
        self.identify_col()
        self.identify_seat()
        return (self.row, self.col, self.seat)

seat_ids = []

for bp in read_data(INPUT):
    boarding_pass = BoardingPass(bp)
    #print(f'{"-" * 23}\nPass Number: {boarding_pass.pass_num}\n{"-" * 23}\nR: {boarding_pass.position()[0]} | C: {boarding_pass.position()[1]} | S: {boarding_pass.position()[2]}\n')
    seat_ids.append(boarding_pass.position()[2] if boarding_pass.seat == 0 else boarding_pass.seat) # Conditional to handle previous print statement not being run

# Find the highest seat Id in the list - Part 1
print(f'Highest Seat ID: {max(seat_ids)}') #! 959

# Find the empty seat - Part 2
for seat in seat_ids:
    if seat + 1 not in seat_ids and seat + 2 in seat_ids:
        print(f'Found a possible seat: \x1b[32;1m{seat + 1}\x1b[0m') #! 527