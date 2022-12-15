dat = [i.strip() for i in open("input.txt")]

sensors: list[tuple[tuple[int, int], tuple[int, int]]] = []
for l in dat:
    p = l.split(" ")
    sensor = int(p[2].split("=")[1][:-1]), int(p[3].split("=")[1][:-1])
    beacon = int(p[-2].split("=")[1][:-1]), int(p[-1].split("=")[1])
    sensors.append((sensor, beacon))

nobeacon: set[tuple[int, int]] = set()


def dist_to_set(s: tuple[int, int], dist: int, coords: set[tuple[int, int]]):
    for dx in range(dist + 1):
        for dy in range(dist, -1, -1):
            if abs(dx) + abs(dy) <= dist:
                coords.add((s[0] + dx, s[1] + dy))
    for dx in range(dist + 1):
        for dy in range(-dist, 1):
            if abs(dx) + abs(dy) <= dist:
                coords.add((s[0] + dx, s[1] + dy))

    for dx in range(0, -dist - 1, -1):
        for dy in range(dist, -1, -1):
            if abs(dx) + abs(dy) <= dist:
                coords.add((s[0] + dx, s[1] + dy))
    for dx in range(0, -dist - 1, -1):
        for dy in range(-dist, 1):
            if abs(dx) + abs(dy) <= dist:
                coords.add((s[0] + dx, s[1] + dy))

for s, b in sensors:
    print(s)
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    dist_to_set(s, dist, nobeacon)

for _, b in sensors:
    if b in nobeacon:
        nobeacon.remove(b)

# print(nobeacon)
c = 0
t = []
for nb in nobeacon:
    if nb[1] == 2000000:
        # print(nb)
        # t.append(nb[0])
        c += 1
# print(sorted(t))
print("Part 1:", c)
print("Part 2:")
