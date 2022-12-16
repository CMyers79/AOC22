with open('input.txt') as file:
    s = file.readlines()
    m = []
    o = []
    t = []
    n = []
    for l in s[1:len(s):7]:
        m.append([int(''.join(filter(str.isdigit, i))) for i in l.strip().split()[2:]])
        n.append(0)
    for l in s[2: len(s):7]:
        o.append([i for i in l.strip().split()[4:]])
    for l in s[3: len(s):7]:
        t.append([int(l.strip().split()[3])])
    for i, l in enumerate(s[4: len(s):7]):
        t[i].append(int(l.strip().split()[5]))
    for i, l in enumerate(s[5: len(s):7]):
        t[i].append(int(l.strip().split()[5]))

    for r in range(10000):
        for i in range(len(m)):
            for j, a in enumerate(m[i]):
                if o[i][0] == '+':
                    a += int(o[i][1])
                else:
                    if o[i][1] == 'old':
                            a *= a
                    else:
                        a *= int(o[i][1])

                if a % t[i][0] == 0:
                    m[t[i][1]].append(a)
                else:
                    m[t[i][2]].append(a)

                n[i] += 1
            m[i] = []

    print(n)






