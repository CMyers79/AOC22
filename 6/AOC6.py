with open('input.txt') as file:
    s = file.readlines()

for i in range(3, len(s[0])):
    if s[0][i] not in s[0][i-3:i] and s[0][i-1] not in s[0][i-3:i-1] and s[0][i-2] != s[0][i-3]:
        print(i+1)
        break

for i in range(13, len(s[0])):
    f = True
    for j in range(14):
        if s[0][i-j] in s[0][i-13:i-j]:
            f = False
            break
    if f:
        print(i+1)
