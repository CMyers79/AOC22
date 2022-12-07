with open('input.txt') as file:
    s = file.readlines()

m = [l.strip().split() for l in s]

d = []
cur = d
prev = []
i = 1

while i < len(m):
    if m[i][0] == "$" and m[i][1] == "ls":
        i += 1
        while i < len(m) and m[i][0] not in ["$", "ls"]:

            if m[i][0] != "dir":
                cur.append(int(m[i][0]))
            else:
                cur.append(m[i][1])
                cur.append([])

            i += 1

    elif m[i][0] == "$" and m[i][1] == "cd":
        if m[i][2] != "..":
            prev.append(cur)
            print(cur)
            cur = cur[cur.index(m[i][2]) + 1]
        else:
            cur = prev.pop()

        i += 1

def size(di):
    tot = 0
    for i in range(len(di)):
        if isinstance(di[i], int):
            tot += di[i]
        elif isinstance(di[i], list):
            tot += size(di[i])
    return tot

def total(di):
    return sum([size(d) for d in di if isinstance(d, list) and size(d) <= 100000]) + sum([total(d) for d in di if isinstance(d, list)])

def size_list(di):

    outer = [size(dr) for dr in di if isinstance(dr, list) and size(dr) >= 1609574]
    inner = [size_list(dr) for dr in di if isinstance(dr, list)]
    for l in inner:
        outer.append(l)
    return outer

print(total(d))
print(size_list(d))
