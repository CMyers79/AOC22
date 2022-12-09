with open('input.txt') as file:
    s = file.readlines()
    d = []
    n = []
    r = [[0,0] for _ in range(10)]
    v = {(0,0) : 1}

for m in s:
    l = m.strip().split()
    d.append(l[0])
    n.append(l[1])

for i in range(len(d)):

    if d[i] == 'U':
        for _ in range(int(n[i])):
            r[0][0] += 1
            for j in range(9):
                if r[j + 1][0] < r[j][0] - 1:
                    r[j + 1][0] += 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                if r[j + 1][1] > r[j][1] + 1:
                    r[j + 1][1] -= 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                if r[j + 1][1] < r[j][1] - 1:
                    r[j + 1][1] += 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                v[(r[9][0], r[9][1])] = 1

    elif d[i] == 'D':
        for _ in range(int(n[i])):
            r[0][0] -= 1
            for j in range(9):
                if r[j + 1][0] > r[j][0] + 1:
                    r[j + 1][0] -= 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                if r[j + 1][1] > r[j][1] + 1:
                    r[j + 1][1] -= 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                if r[j + 1][1] < r[j][1] - 1:
                    r[j + 1][1] += 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                v[(r[9][0], r[9][1])] = 1

    elif d[i] == 'L':
        for _ in range(int(n[i])):
            r[0][1] -= 1
            for j in range(9):
                if r[j + 1][1] > r[j][1] + 1:
                    r[j + 1][1] -= 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                if r[j + 1][0] < r[j][0] - 1:
                    r[j + 1][0] += 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                if r[j + 1][0] > r[j][0] + 1:
                    r[j + 1][0] -= 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                v[(r[9][0], r[9][1])] = 1

    elif d[i] == 'R':
        for _ in range(int(n[i])):
            r[0][1] += 1
            for j in range(9):
                if r[j + 1][1] < r[j][1] - 1:
                    r[j + 1][1] += 1
                    if abs(r[j + 1][0] - r[j][0]) < 1.5:
                        r[j + 1][0] = r[j][0]
                    else:
                        r[j + 1][0] = round((r[j + 1][0] + r[j][0]) / 2)

                if r[j + 1][0] < r[j][0] - 1:
                    r[j + 1][0] += 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                if r[j + 1][0] > r[j][0] + 1:
                    r[j + 1][0] -= 1
                    if abs(r[j + 1][1] - r[j][1]) < 1.5:
                        r[j + 1][1] = r[j][1]
                    else:
                        r[j + 1][1] = round((r[j + 1][1] + r[j][1]) / 2)

                v[(r[9][0], r[9][1])] = 1

print(len(v))

