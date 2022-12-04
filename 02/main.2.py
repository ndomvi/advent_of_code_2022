dat = [i.strip() for i in open("input.txt")]

a = {'A': 0, 'B': 1, 'C': 2}
b = {'X': 0, 'Y': 1, 'Z': 2}

score = 0
for line in dat:
    s = line.split(' ')
    x = a[s[0]]
    y = b[s[1]]
    score += y + 1

    res = (x - y) % 3
    if res == 2:
        score += 6
    elif res == 0:
        score += 3
    else:
        score += 0

print("Part 1:", score)
