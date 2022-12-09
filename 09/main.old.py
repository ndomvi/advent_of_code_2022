dat = [i.strip() for i in open("input.txt")]

head = (0, 0)
tail = (0, 0)
visited: set[tuple[int, int]] = set()
for line in dat:
    d, n = line.split(" ")
    for _ in range(int(n)):
        x, y = head
        match d[0]:
            case "R":
                x += 1
                if tail[0] == x - 2:
                    tail = (x - 1, y)
            case "L":
                x -= 1
                if tail[0] == x + 2:
                    tail = (x + 1, y)
            case "U":
                y += 1
                if tail[1] == y - 2:
                    tail = (x, y - 1)
            case "D":
                y -= 1
                if tail[1] == y + 2:
                    tail = (x, y + 1)
            case s:
                print("error", s)

        head = (x, y)
        # print(head, tail)
        visited.add(tail)

print("Part 1:", len(visited))
print("Part 2:")
