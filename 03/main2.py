from functools import reduce
import string

dat = [i.strip() for i in open("input.txt")]

part1 = reduce(
    lambda s, x: s + string.ascii_letters.index(
        set(x[:len(x) // 2]).intersection(set(x[len(x) // 2:])).pop()) + 1,
    dat, 0)
print("Part 1:", part1)

res: list[str] = []
for g in range(0, len(dat), 3):
    comm: set[str] = set()
    for e in dat[g:g + 3]:
        s = set(e)
        if len(comm) == 0:
            comm = s
        else:
            comm = comm.intersection(s)

    res += comm.pop()

part2 = 0
for c in res:
    part2 += string.ascii_letters.index(c) + 1
print("Part 2:", part2)
