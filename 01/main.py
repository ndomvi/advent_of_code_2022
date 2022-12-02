import heapq

d = open("input.txt").read()
elves = d.split("\n\n")
h = []
for e in elves:
    s = 0
    for l in e.strip().split("\n"):
        s += int(l)
    heapq.heappush(h, -s)

m = [-heapq.heappop(h) for _ in range(3)]
print("Part 1:", m[0])
print("Part 2:", sum(m))
