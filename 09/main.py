dat = [i.strip() for i in open("input.txt")]


def move(snake: list[tuple[int, int]], c: int):
    x, y = snake[c]
    xn, yn = snake[c + 1]

    xnn, ynn = xn, yn
    # TODO: make pretty
    if xn == x + 2:
        if abs(yn - y) != 2:
            ynn = y
        xnn = x + 1
    elif xn == x - 2:
        if abs(yn - y) != 2:
            ynn = y
        xnn = x - 1

    if yn == y + 2:
        if abs(xn - x) != 2:
            xnn = x
        ynn = y + 1
    elif yn == y - 2:
        if abs(xn - x) != 2:
            xnn = x
        ynn = y - 1

    snake[c + 1] = (xnn, ynn)

    if (xn, yn) != (xnn, ynn) and c + 1 != len(snake) - 1:
        move(snake, c + 1)


def process(length: int) -> set[tuple[int, int]]:
    snake: list[tuple[int, int]] = [(0, 0)] * length
    visited: set[tuple[int, int]] = set()
    visited.add(snake[-1])
    for line in dat:
        d, n = line.split(" ")
        for _ in range(int(n)):
            x, y = snake[0]
            match d:
                case "R":
                    x += 1
                case "L":
                    x -= 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case s:
                    print("Unexpected direction:", s)
            snake[0] = (x, y)
            move(snake, 0)
            visited.add(snake[-1])
    return visited


print("Part 1:", len(process(2)))
print("Part 2:", len(process(10)))
