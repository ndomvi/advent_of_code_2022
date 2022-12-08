dat = [i.strip() for i in open("input.txt")]
grid = [[int(i) for i in l] for l in dat]
counter = 0
max_score = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        c = grid[y][x]
        v = False
        score = 1

        d = 0
        for ax in range(x - 1, -1, -1):
            d += 1
            if grid[y][ax] >= c:
                break
        else:
            v = True
        score *= d
        d = 0
        for ax in range(x + 1, len(grid)):
            d += 1

            if grid[y][ax] >= c:
                break
        else:
            v = True
        score *= d

        d = 0
        for ay in range(y - 1, -1, -1):
            d += 1

            if grid[ay][x] >= c:
                break
        else:
            v = True
        score *= d

        d = 0
        for ay in range(y + 1, len(grid)):
            d += 1

            if grid[ay][x] >= c:
                break
        else:
            v = True
        score *= d

        max_score = max(max_score, score)
        if v:
            counter += 1

print("Part 1:", counter)
print("Part 2:", max_score)
