import re

with open('input.txt') as file:
    s = file.readlines()

stacks = [[] for _ in range(10)]

for i in range(7, -1, -1):
    for j in range(1, len(s[0]), 4):
        if s[i][j] != ' ':
            stacks[int(s[8][j]) - 1].append(s[i][j])

for l in s[10:]:
    nums = [int(n) for n in re.findall('[0-9]+', l)]

    for _ in range(nums[0]):
        stacks[9].append(stacks[nums[1] - 1].pop())

    for _ in range(nums[0]):
        stacks[nums[2] - 1].append(stacks[9].pop())

for i in range(9):
    print(stacks[i][-1])
