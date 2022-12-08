with open('input.txt') as file:
    s = file.readlines()
t = []
v = 0
w = 0
for r in s:
    t.append([int(c) for c in r.strip()])

for j, r in enumerate(t):
    for i, tree in enumerate(r):
        l = ri = u = do = 0

        if i == 0 or i == len(t[0]) - 1 or j == 0 or j == len(t) - 1:
            v += 1
        elif tree > max(r[:i]) or tree > max(r[i + 1:]) or tree > max([t[k][i] for k in range(j)]) or tree > max([t[k][i] for k in range(j + 1, len(t))]):
            v += 1

        if not (i == 0 or i == len(t[0]) - 1 or j == 0 or j == len(t) - 1):
            for a in range(i - 1, -1, -1):
                l += 1
                if t[j][a] >= tree:
                    break

            for b in range(i + 1, len(t[0])):
                ri += 1
                if t[j][b] >= tree:
                    break

            for c in range(j - 1, -1, -1):
                u += 1
                if t[c][i] >= tree:
                    break

            for d in range(j + 1, len(t)):
                do += 1
                if t[d][i] >= tree:
                    break
        w = max(w, l * ri * u * do)
print(v,w)
