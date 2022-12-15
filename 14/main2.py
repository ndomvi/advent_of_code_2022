dat = [i.strip() for i in open("input.txt")]

walls: set[tuple[int, int]] = set()


def srange(start: int, stop: int, step: int = 1):
    if start > stop:
        start, stop = stop, start
    return range(start, stop + 1, step)


max_y = -1
for line in dat:
    l = line.split(" -> ")
    for w in range(len(l) - 1):
        wall_s, wall_e = list(map(int, l[w].split(","))), list(
            map(int, l[w + 1].split(",")))
        for y in srange(wall_s[1], wall_e[1]):
            for x in srange(wall_s[0], wall_e[0]):
                max_y = max(max_y, y)
                walls.add((x, y))

spawn = (500, 0)

sand = walls.copy()
overflow = False
while not overflow:
    x, y = spawn
    y += 1
    while True:
        if y > max_y + 1:
            overflow = True
            break
        if (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in sand:
            y += 1
            x -= 1
        elif (x + 1, y + 1) not in sand:
            y += 1
            x += 1
        else:
            # stuck
            sand.add((x, y))
            break

print("Part 1:", len(sand - walls))

sand = walls.copy()
while True:
    x, y = spawn
    if spawn in sand:
        break
    while True:
        if y + 1 >= max_y + 2:
            sand.add((x, y))
            break
        if (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in sand:
            y += 1
            x -= 1
        elif (x + 1, y + 1) not in sand:
            y += 1
            x += 1
        else:
            # stuck
            sand.add((x, y))
            break

print("Part 2:", len(sand - walls))
