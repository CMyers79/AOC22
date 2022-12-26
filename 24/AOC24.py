with open('input.txt') as file:
    s = file.readlines()

start = (0, 1)
end = (36, 100)

v = [[[] for _ in range(37)]]
b = []

for i, l in enumerate(s):
    for j, c in enumerate(l.strip()):
        v[0][i].append(c)
        if c != '.':
            b.append([c, i, j])

for i in range(700):
    v.append([['#'] for _ in range(37)])

    for x in b:
        if x[0] == '^':
            x[1] -= 1
            if x[1] < 1:
                x[1] = 35
        elif x[0] == 'v':
            x[1] += 1
            if x[1] > 35:
                x[1] = 1
        elif x[0] == '<':
            x[2] -= 1
            if x[2] < 1:
                x[2] = 100
        elif x[0] == '>':
            x[2] += 1
            if x[2] > 100:
                x[2] = 1
        v[i + 1][x[1]].append(x[0])

print(v)
