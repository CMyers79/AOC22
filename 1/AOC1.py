with open('input.txt') as file:
    strings = file.readlines()
    most = []
    current = 0
    for string in strings:
        if string != '\n':
            current += int(string)
        else:
            most.append(current)
            if len(most) == 4:
                most.remove(min(most))
            current = 0
    print(sum(most))
