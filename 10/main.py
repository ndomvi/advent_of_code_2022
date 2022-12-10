dat = [i.strip() for i in open("input.txt")]

x = 1
counter = -19
vals: list[int] = [0] * 6
crt = [["." for _ in range(40)] for _ in range(6)]
for i in dat:
    instr = i.split(" ")
    if instr[0] == "addx":
        counter += 2
        if (counter - 1) % 40 == 0:
            vals[(counter - 1) // 40] = x * (counter - 1 + 20)

        if (x - 1) <= ((counter - 1 + 20) % 40) - 1 <= (x + 1):
            crt[(counter - 1 + 20) // 40][(counter - 1 + 20) % 40 - 1] = "#"

        x += int(instr[1])

    else:
        counter += 1

    if counter % 40 == 0:
        vals[counter // 40] = x * (counter + 20)

    if (x - 1) <= ((counter + 20) % 40) - 1 <= (x + 1):
        crt[(counter + 20) // 40][(counter + 20) % 40 - 1] = "#"

print("Part 1:", sum(vals))
print("Part 2:")
print('\n'.join([''.join(l) for l in crt]))
