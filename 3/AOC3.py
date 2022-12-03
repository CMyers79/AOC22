with open('input.txt') as file:
    s = file.readlines()
    t = 0
for g in range(0, len(s), 3):
    cur = [c for c in s[g] if c in s[g + 1] and c in s[g + 2]][0]
    if ord(cur) > 96:
        t += ord(cur) - 96
    else:
        t += ord(cur) - 38
print(t)
