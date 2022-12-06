dat = [i.strip() for i in open("input.txt")][0]

# This seems really inefficient but I am actually not sure if there's a
# better (in terms of performance and/or simplicity) way to do this
for i in range(len(dat) - 4):
    if len(set(dat[i:i + 4])) == 4:
        print("Part 1:", i + 4)
        break

for i in range(len(dat) - 14):
    if len(set(dat[i:i + 14])) == 14:
        print("Part 2:", i + 14)
        break
