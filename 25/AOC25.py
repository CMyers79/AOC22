with open('input.txt') as file:
    s = file.readlines()
tot = 0
m = 0
for line in s:
    t = 0
    b = 0
    l = line.strip()
    m = max(len(l), m)
    for i in range(len(l) - 1, -1, -1):
        if l[i] == '-':
            t += -1 * 5 ** b
        elif l[i] == '=':
            t += -2 * 5 ** b
        else:
            t += int(l[i]) * 5 ** b
        b += 1
    tot += t  # base 10

print(tot)

ts = ''
for p in range(m + 2, -1, -1):
    if tot >= 5 ** p:
        ts = ts + str(tot // 5 ** p)
        tot %= 5 ** p
    else:
        ts = ts + '0'

print(ts)  # base 5, leading 0s

c = 0
f = ''
for d in range(len(ts) - 1, -1, -1):
    if int(ts[d]) + c == 3:
        c = 1
        f = '=' + f
    elif int(ts[d]) + c == 4:
        c = 1
        f = '-' + f
    elif int(ts[d]) + c == 5:
        c = 1
        f = '0' + f
    else:
        f = str(int(ts[d]) + c) + f
        c = 0

print(f)  # SNAFU
