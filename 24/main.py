from collections import deque


dat = [i.strip() for i in open("input.txt")]
dat.insert(0, "#" * len(dat[0]))
dat.append("#" * len(dat[-1]))

Coord = tuple[int, int]
walls: set[Coord] = set()
blizzards: list[tuple[Coord, tuple[int, int]]] = []
for row, row_v in enumerate(dat):
    for cell, cell_v in enumerate(row_v):
        match cell_v:
            case "#":
                walls.add((cell, row))
            case "^":
                blizzards.append(((cell, row), (0, -1)))
            case "v":
                blizzards.append(((cell, row), (0, 1)))
            case "<":
                blizzards.append(((cell, row), (-1, 0)))
            case ">":
                blizzards.append(((cell, row), (1, 0)))
            case ".":
                pass
            case _:
                raise ValueError("Unknown input map character:", cell_v)

blizzards_time: list[set[Coord]] = [set(b[0] for b in blizzards)]
c = 1
while True:
    s: set[Coord] = set()
    for idx, b in enumerate(blizzards):
        n_x, n_y = b[0]
        n_x += b[1][0]
        n_y += b[1][1]
        if n_x == 0:
            n_x = len(dat[0]) - 2
        elif n_x == len(dat[0]) - 1:
            n_x = 1
        elif n_y == 1:
            n_y = len(dat) - 3
        elif n_y == len(dat) - 2:
            n_y = 2

        blizzards[idx] = ((n_x, n_y), b[1])
        s.add((n_x, n_y))

    if s == blizzards_time[0]:
        break

    blizzards_time.append(s)
    c += 1


def bfs(start: Coord, goal: Coord, walls: set[Coord],
        blizzards_time: list[set[Coord]],
        start_time: int = 0) -> int:
    visited: set[tuple[int, Coord]] = set()
    frontier: deque[tuple[int, Coord]] = deque()
    frontier.append((start_time, start))
    while True:
        if len(frontier) > 10000:
            print(frontier)
            input()
        time, cur = frontier.popleft()

        if cur == goal:
            return time

        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)):
            nx, ny = (cur[0] + dx, cur[1] + dy)
            # This move has already been made
            if (time % len(blizzards_time), (nx, ny)) in visited:
                continue
            else:
                visited.add((time % len(blizzards_time), (nx, ny)))

            if (nx, ny) in walls:
                continue
            # Next move will be in a blizzard
            if (nx, ny) in blizzards_time[(time + 1) % len(blizzards_time)]:
                continue

            frontier.append((time + 1, (nx, ny)))


start = (dat[1].index("."), 1)
goal = (dat[-2].index("."), len(dat) - 2)

p1 = bfs(start, goal, walls, blizzards_time)
print("Part 1:", p1)
p2 = bfs(goal, start, walls, blizzards_time, start_time=p1)
p2 = bfs(start, goal, walls, blizzards_time, start_time=p2)
print("Part 2:", p2)
