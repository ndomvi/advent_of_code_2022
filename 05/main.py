from copy import deepcopy

stacks: list[list[str]] = []
start = []
moves = []

with open("input.txt") as f:
    data = f.read()
    start, moves = map(lambda x: x.split("\n"), data.split("\n\n"))

n = len(start[-1].strip().split())
stacks = [[] for _ in range(n)]
for l in start[:-1][::-1]:
    for i in range(n):
        idx = (4 * i) + 1
        if l[idx] != " ":
            stacks[i].append(l[idx])

stacks2 = deepcopy(stacks)
for mov in moves:
    m = mov.split()
    c, s, d = map(int, [m[1], m[3], m[5]])
    for _ in range(c):
        stacks[d - 1].append(stacks[s - 1].pop())

for mov in moves:
    m = mov.split()
    c, s, d = map(int, [m[1], m[3], m[5]])
    stacks2[d - 1].extend(stacks2[s - 1][-c:])
    stacks2[s - 1] = stacks2[s - 1][:-c]

print("Part 1:", ''.join([s[-1] for s in stacks]))
r2 = []
for st2 in stacks2:
    if len(st2) != 0:
        r2.append(st2[-1])
print("Part 2:", ''.join(r2))
