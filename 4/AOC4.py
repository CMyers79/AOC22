with open('input.txt') as file:
    s = file.readlines()
    x = 0
    y = 0
for l in s:
    t = [r for r in l.strip().split(',')]
    a = [int(n) for n in t[0].split('-') + t[1].split('-')]
    if a[0] == min(a) and a[1] == max(a) or a[2] == min(a) and a[3] == max(a):
        x += 1
    if a[0] <= a[2] <= a[1] or a[0] <= a[3] <= a[1] or a[2] <= a[0] <= a[3] or a[2] <= a[1] <= a[3]:
        y += 1
print(x, y)

