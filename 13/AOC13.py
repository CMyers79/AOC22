
def compare(l, r, more=False):

    if isinstance(l, list) and isinstance(r, list):
        if len(l) > 1 and len(r) > 1:
            return compare(l[0], r[0]) * compare(l[1:], r[1:])
        elif len(r) > 0 and len(l) > 0:
            return compare(l[0], r[0], len(r) == 1 and len(l) > 1 and not isinstance(r[0], list))
        else:
            return 1

    elif isinstance(l, list) and not isinstance(r, list):
        r = [r]
        return compare(l, r)

    elif not isinstance(l, list) and isinstance(r, list):
        l = [l]
        return compare(l, r)

    else:
        if l <= r and not more:
            return 1
        elif l < r:
            return 1
        else:
            return 0


with open('input.txt') as file:
    s = file.readlines()
    tot = 0

    for i in range(0, len(s), 3):
        l = [s[i].strip()]
        r = [s[i + 1].strip()]
        for half in l, r:
            cur = half
            prev = [cur]
            for j in range(1, len(half[0])):
                c = half[0][j]
                if c == '[':
                    cur.append([])
                    prev.append(cur)
                    cur = cur[-1]
                elif c.isdigit():
                    if c == '1' and half[0][j+1] == '0':
                        cur.append(10)
                    elif c == '0' and half[0][j - 1] == '1':
                        continue
                    else:
                        cur.append(int(c))

                elif c == ']':
                    cur = prev.pop()

        l = l[1:]
        r = r[1:]

        if compare(l, r):
            print(i // 3 + 1)
            tot += i // 3 + 1

    print(tot)
