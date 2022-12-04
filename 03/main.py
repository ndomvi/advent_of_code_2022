import string

dat = [i.strip() for i in open("input.txt")]
res: list[str] = []
for line in dat:
    a, b = line[:len(line) // 2], line[len(line) // 2:]
    sa = set(a)
    sb = set(b)
    res += sa.intersection(sb).pop()

result = 0
for c in res:
    result += string.ascii_letters.index(c) + 1
print("Part 1:", result)

res = []
for g in range(0, len(dat), 3):
    comm: set[str] = set()
    for e in dat[g:g + 3]:
        s = set(e)
        if len(comm) == 0:
            comm = s
        else:
            comm = comm.intersection(s)

    assert len(comm) == 1
    res += comm.pop()

result = 0
for c in res:
    result += string.ascii_letters.index(c) + 1
print("Part 2:", result)
