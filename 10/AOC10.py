with open('input.txt') as file:
    s = file.readlines()
    c = []
    cyc = 0
    str = 1
    tot = 0
    crt = [[' ' for _ in range(40)] for _ in range(6)]

for l in s:
    if len(l.strip().split()) == 1:
        c.append(l.strip().split()[0])
    else:
        c.append(l.strip().split())
for a in c:
    if a == "noop":
        cyc += 1
        if cyc in (20, 60, 100, 140, 180, 220):
            tot += cyc * str
        for j in range(0, 201, 40):
            if cyc in range(j + 1, j + 41):
                if int(str) in range(max(1, cyc - j // 40 - 1), min(41, cyc - j // 40 + 2)):
                    crt[j // 40][cyc - j // 40 - 1] = 'X'
    else:
        cyc += 1
        if cyc in (20, 60, 100, 140, 180, 220):
            tot += cyc * str
        for j in range(0, 201, 40):
            if cyc in range(j + 1, j + 41):
                if int(str) in range(max(1, cyc - j // 40 - 1), min(41, cyc - j // 40 + 2)):
                    crt[j // 40][cyc - j // 40 - 1] = 'X'
        cyc += 1
        if cyc in (20, 60, 100, 140, 180, 220):
            tot += cyc * str
        for j in range(0, 201, 40):
            if cyc in range(j + 1, j + 41):
                if int(str) in range(max(1, cyc - j // 40 - 1), min(41, cyc - j // 40 + 2)):
                    crt[j // 40][cyc - j // 40 - 1] = 'X'
        str += int(a[1])
    print(str)

print(tot)
for row in crt:
    print(row)
