d = open("input.txt").read()
e = d.split("\n\n")
m = (0, 0)
t = []
for n, i in enumerate(e):
    s = 0
    for l in i.strip().split("\n"):
        s += int(l)
    t.append(s)
    if s > m[1]:
        m = (n+1, s)

t.sort()
print("Part 1:", m[1])
print("Part 2:", sum(t[-3:]))
