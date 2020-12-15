# AoC 2020, Day 01, Part 2

with open('./input.txt', 'r') as infile:
    indata = infile.read().splitlines()

num1 = 0

sumnums = []
solutions = 0

for line1 in indata:
    line1 = int(line1)
    num1 += 1
    num2 = 0
    for line2 in indata:
        line2 = int(line2)
        num2 += 1
        num3 = 0
        for line3 in indata:
            line3 = int(line3)
            num3 += 1
            if line1 + line2 + line3 == 2020:
                print(f'Success: {line1} + {line2} + {line3} = {line1 + line2 + line3}')
                solutions += 1
                sumnums.append(line1)
                sumnums.append(line2)
                sumnums.append(line3)
                print(f'Solution #{solutions} is {sumnums[0] * sumnums[1] * sumnums[2]}')
                sumnums = []
                break
    print(f'Checked entry {num1} against {num2 * num3} other entries')

print(f'Found {solutions} possible solutions')