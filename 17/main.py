pat = [i.strip() for i in open("input.txt")][0]

# stack: list[list[str]] = []  #[["." for _ in range(7)] for _ in range(3)]


def create_stone(t: int, y: int) -> set[tuple[int, int]]:
    t = t % 5
    # BOTTOM-UP
    if t == 0:
        # ####
        return {(2, y), (3, y), (4, y), (5, y)}
    elif t == 1:
        # .#.
        # ###
        # .#.
        return {(3, y), (2, y + 1), (3, y + 1), (4, y + 1), (3, y + 2)}
    elif t == 2:
        # ..#
        # ..#
        # ###
        return {(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)}
    elif t == 3:
        # #
        # #
        # #
        # #
        return {(2, y), (2, y + 1), (2, y + 2), (2, y + 3)}
    elif t == 4:
        # ##
        # ##
        return {(2, y), (3, y), (2, y + 1), (3, y + 1)}
    raise ValueError


seen: set[tuple[int, int]] = set()
lines = []


def simulate(n: int) -> int:
    stones: set[tuple[int, int]] = set()

    t = 0
    max_y = 0
    last_line = (0, 0)
    for s in range(n):
        if s % 10000 == 0:
            print(s)
            print(lines)
        stone = create_stone(s, max_y + 4)
        stopped = False
        while not stopped:
            # Wind
            new_stone: set[tuple[int, int]] = set()
            if pat[t] == "<":
                for x, y in stone:
                    i = (x - 1, y)
                    if i[0] < 0 or i in stones:
                        break
                    new_stone.add(i)
                else:
                    stone = new_stone
            else:
                for x, y in stone:
                    i = (x + 1, y)
                    if i[0] > 6 or i in stones:
                        break
                    new_stone.add(i)
                else:
                    stone = new_stone

            # Fall down
            new_stone = set()
            for x, y in stone:
                i = (x, y - 1)
                if i in stones or i[1] == 0:
                    stones |= stone
                    max_y = max(max_y, *[y for _, y in stone])
                    stopped = True
                    for dy in set(y for _, y in stone):
                        for ix in range(7):
                            if (ix, dy) not in stones:
                                break
                        else:
                            if (s % 5, t) in seen:
                                if s % 5 == 1 and t == 31:
                                    lines.append((dy, t, s % 5, s))
                                    print("FULL LOOP")
                                # print(f"REPEAT @ {dy}, ({s%5},{t}) {len(seen)=}")
                                # input()
                            else:
                                print(f"NEW LINE @ {dy}, ({s%5},{t}) ")
                                seen.add((s % 5, t))
                                if s % 5 == 0 and t == 1132:
                                    print(s, dy)
                    break
                new_stone.add(i)
            else:
                stone = new_stone

            t = (t + 1) % len(pat)

    return max_y


# 3117
print("Part 1:", simulate(2022))
# a = "y before infinite loop starts" + (((1000000000000 - "stones before loop starts") // "stones per loop") * "y per loop")
a = 2707 + (((1000000000000 - 1746) // 1735) * 2695)
# I have no clue why this is correct
b = ((1000000000000 - 1746) % 1735) - 5
# 1553314121019
print(a + simulate(b))
print(1553314121019 - (a + simulate(b)))
# print(a + simulate(b))
# print("Part 2:", simulate(1000000000000))
