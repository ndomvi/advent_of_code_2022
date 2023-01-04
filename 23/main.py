from itertools import permutations

dat = [i.strip() for i in open("input.txt")]

elves: set[tuple[int, int]] = set()
for y in range(len(dat)):
    for x in range(len(dat[y])):
        if dat[y][x] == "#":
            elves.add((x, y))

neighbours = set(permutations([-1, -1, 0, 1, 1], 2))
dirs = [((0, -1), ((-1, -1), (0, -1), (1, -1))),
        ((0, 1), ((-1, 1), (0, 1), (1, 1))),
        ((-1, 0), ((-1, 1), (-1, 0), (-1, -1))),
        ((1, 0), ((1, -1), (1, 0), (1, 1)))]

for _ in range(10):
    candidate_elves: dict[tuple[int, int], tuple[int, int]] = {}
    for x, y in elves:
        # Check for any neighbour elf
        if not any((x + dx, y + dy) in elves for dx, dy in neighbours):
            candidate_elves[(x, y)] = (x, y)
            continue

        for dir, dir_neighbours in dirs:
            if not any((x + dx, y + dy) in elves for dx, dy in dir_neighbours):
                if (taken := candidate_elves.get(
                    (x + dir[0], y + dir[1]))) is not None:
                    candidate_elves[taken] = taken
                    candidate_elves[(x, y)] = (x, y)
                    del candidate_elves[(x + dir[0], y + dir[1])]
                else:
                    candidate_elves[(x + dir[0], y + dir[1])] = (x, y)
                break
        else:
            candidate_elves[(x, y)] = (x, y)

    elves = set(candidate_elves.keys())
    dirs.append(dirs.pop(0))

elves_list = list(elves)
min_x, min_y = elves_list[0]
max_x, max_y = elves_list[0]
for x, y in elves_list:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# len_x = 0
# if max_x >= 0 and min_x < 0:
#     len_x = max_x - min_x
# else:
#     len_x = max_x + min_x

# len_y = 0
# if max_y >= 0 and min_y < 0:
#     len_y = max_y + min_y
# else:
#     len_y = max_y - min_y

# area = len_x * len_y
area = (1 + max_x - min_x) * (1 + max_y - min_y)

print("Part 1:", area - len(elves_list))

moved = True
moves = 10
# TODO: extract to a function/code duplication
while moved:
    candidate_elves: dict[tuple[int, int], tuple[int, int]] = {}
    for x, y in elves:
        # Check for any neighbour elf
        if not any((x + dx, y + dy) in elves for dx, dy in neighbours):
            candidate_elves[(x, y)] = (x, y)
            continue

        for dir, dir_neighbours in dirs:
            if not any((x + dx, y + dy) in elves for dx, dy in dir_neighbours):
                if (taken := candidate_elves.get(
                    (x + dir[0], y + dir[1]))) is not None:
                    candidate_elves[taken] = taken
                    candidate_elves[(x, y)] = (x, y)
                    del candidate_elves[(x + dir[0], y + dir[1])]
                else:
                    candidate_elves[(x + dir[0], y + dir[1])] = (x, y)
                break
        else:
            candidate_elves[(x, y)] = (x, y)

    elves_next = set(candidate_elves.keys())
    if elves == elves_next:
        moved = False
    elves = elves_next
    moves += 1
    dirs.append(dirs.pop(0))

print("Part 2:", moves)
