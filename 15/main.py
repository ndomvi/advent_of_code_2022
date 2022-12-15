dat = [i.strip() for i in open("input.txt")]

sensors: list[tuple[tuple[int, int], tuple[int, int], int]] = []
for l in dat:
    p = l.split(" ")
    s = int(p[2].split("=")[1][:-1]), int(p[3].split("=")[1][:-1])
    b = int(p[-2].split("=")[1][:-1]), int(p[-1].split("=")[1])
    sensors.append((s, b, abs(s[0] - b[0]) + abs(s[1] - b[1])))

target_y = 2000000

empty_x: set[int] = set()
for s, b, dist in sensors:
    d = abs(s[1] - target_y)
    if d <= dist:
        for x in range(s[0] - dist + d, s[0] + dist - d + 1):
            empty_x.add(x)

for s, b, _ in sensors:
    if b[1] == target_y:
        if b[0] in empty_x:
            empty_x.remove(b[0])

print("Part 1:", len(empty_x))

# I am done with trying to implement this shit using "normal" python
# z3 is VERY useful for this type of tasks.
# it still took me like 20 minutes to make it work
# TODO: write an algorithmic solution (without z3)

import z3

x = z3.Int("x")
y = z3.Int("y")

s = z3.Solver()
s.add(x > 0, y > 0, x <= 4000000, y <= 4000000)

for sen, b, dist in sensors:
    s.add(z3.Abs(x - sen[0]) + z3.Abs(y - sen[1]) > dist)

s.check()

m = s.model()
print(m, m[x].as_long() * 4000000 + m[y].as_long())
