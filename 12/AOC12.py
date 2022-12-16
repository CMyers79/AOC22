with open('input.txt') as file:
    s = file.readlines()

a = []
for l in s:
    a.append([c for c in l.strip()])

d = [[float('inf') for _ in range(len(a[0]))] for _ in range(len(a))]
v = []
end = (20, a[20].index('E'))
start = (20, 1)
cur = end
prev = []
a[end[0]][end[1]] = 'z'
a[start[0]][start[1]] = 'a'
d[end[0]][end[1]] = 0

while cur != start:

    for (r, c) in [(cur[0] + 1, cur[1] + 1), (cur[0] + 1, cur[1] - 1), (cur[0] + 1, cur[1] + 1), (cur[0] - 1, cur[1] - 1)]:
        if ord(a[r][c]) >= ord(a[cur[0]][cur[1]]) - 1 and (r, c) not in v:
            d[r][c] = min(d[r][c], d[cur[0]][cur[1]] + 1)
    v.append(cur)
    
    if len(adj) > 0:
        prev.append(cur)
        cur = (adj[0][0], adj[0][1])
    else:
        cur = prev.pop()
    print(v)

print(d[cur[0]][cur[1]])
