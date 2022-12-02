with open('input.txt') as file:
    s = file.readlines()

score = 0

m = [l.split() for l in s]
for n in m:
    if n[1] == 'X':
        if n[0] == 'A':
            score += 3
        elif n[0] == 'B':
            score += 1
        else:
            score += 2

    elif n[1] == 'Y':
        if n[0] == 'A':
            score += 4
        elif n[0] == 'B':
            score += 5
        else:
            score += 6
    else:
        if n[0] == 'A':
            score += 8
        elif n[0] == 'B':
            score += 9
        else:
            score +=7


print(score)

