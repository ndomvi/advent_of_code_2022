dat = [i.strip() for i in open("input.txt")]

c = 0
c2 = 0
for line in dat:
    a, b = line.split(",")
    (a_l, a_h) = list(map(int, a.split("-")))
    (b_l, b_h) = list(map(int, b.split("-")))

    if (a_l <= b_l and a_h >= b_h) or (a_l >= b_l and a_h <= b_h):
        c += 1

    if (a_l >= b_l and a_l <= b_h) or (b_l >= a_l and b_l <= a_h):
        c2 += 1

print("Part 1:", c)
print("Part 2:", c2)
