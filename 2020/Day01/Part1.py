

with open('./input.txt', 'r') as infile:
    indata = infile.read().splitlines()

num1 = 0

sumnums = []

for line1 in indata:
    line1 = int(line1)
    num1 += 1
    num2 = 0
    for line2 in indata:
        line2 = int(line2)
        num2 += 1
        if line1 + line2 == 2020:
            print(f'Success: {line1} + {line2} = {line1 + line2}')
            sumnums.append(line1)
            sumnums.append(line2)
            break
    print(f'Checked entry {num1} against {num2} other entries')

print(f'The solution is {sumnums[0] * sumnums[1]}')