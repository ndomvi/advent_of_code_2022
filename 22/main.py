dat = open("input.txt").read()
board_raw, moves_raw = dat.split("\n\n")

# Pad the board with spaces to simplify code
board = [" " + i + " " for i in board_raw.split("\n")]
board.insert(0, " " * len(board[0]))
board.insert(len(board), " " * len(board[-1]))
board_max_row = max(len(row) for row in board)
for line in range(len(board)):
    board[line] = board[line].ljust(board_max_row, " ")


moves: list[int | str] = []
int_buf = ""
c = 0
while c != len(moves_raw):
    if moves_raw[c].isdigit():
        int_buf += moves_raw[c]
    else:
        moves.append(int(int_buf))
        int_buf = ""

        moves.append(moves_raw[c])

    c += 1
if int_buf != "":
    moves.append(int(int_buf))

dir_values: dict[tuple[int, int], int] = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}


def p1() -> None:
    x, y = (board[1].find("."), 1)
    d_x, d_y = (1, 0)
    for m in moves:
        match m:
            case int(num):
                for _ in range(num):
                    n_x, n_y = x + d_x, y + d_y
                    if board[n_y][n_x] == "#":
                        break
                    elif board[n_y][n_x] == " ":
                        while board[y - d_y][x - d_x] != " ":
                            x += -d_x
                            y += -d_y
                    else:
                        x, y = n_x, n_y
            case "R":
                d_x, d_y = (-d_y, d_x)
            case "L":
                d_x, d_y = (d_y, -d_x)
            case _:
                raise ValueError("Unexpected value:", m)

    print("Part 1:", (1000 * y + 4 * x + dir_values[d_x, d_y]))


def p2() -> None:
    x, y = (board[1].find("."), 1)
    d_x, d_y = (1, 0)
    for m in moves:
        # print(f"({x-1}, {y-1}) ({d_x}, {d_y}) {m}")
        match m:
            case int(num):
                for _ in range(num):
                    n_x, n_y = x + d_x, y + d_y
                    nd_x, nd_y = d_x, d_y
                    if board[n_y][n_x] == " ":
                        # TODO: make a universal solution for this?
                        # Would probably involve cube folding, which doesnt sound fun
                        # TODO: some corners will not work if walked into.
                        # Need to add a specific case for that, which considers the direction
                        if n_y == 0:
                            if n_x < 101:
                                n_y = 100 + n_x
                                n_x = 1
                                nd_x, nd_y = 1, 0
                            else:
                                n_y = 200
                                n_x = n_x - 100
                                nd_x, nd_y = 0, -1
                        elif n_y < 51:
                            if n_x == 50:
                                n_x = 1
                                n_y = 151 - n_y
                                nd_x, nd_y = 1, 0
                            elif n_x == 151:
                                n_y = 151 - n_y
                                n_x = 100
                                nd_x, nd_y = -1, 0
                        elif n_y == 51 and n_x > 100:
                            n_y = n_x - 50
                            n_x = 100
                            nd_x, nd_y = -1, 0
                        elif n_y < 100:
                            if n_x == 50:
                                n_x = n_y - 50
                                n_y = 101
                                nd_x, nd_y = 0, 1
                            elif n_x == 101:
                                n_x = 100 + (n_y - 50)
                                n_y = 50
                                nd_x, nd_y = 0, -1
                        elif n_y == 100 and n_x < 51:
                            n_y = n_x + 50
                            n_x = 51
                            nd_x, nd_y = 1, 0
                        elif n_y < 151:
                            if n_x == 0:
                                n_x = 51
                                n_y = 151 - n_y
                                nd_x, nd_y = 1, 0
                            elif n_x == 101:
                                n_x = 150
                                n_y = 151 - n_y
                                nd_x, nd_y = -1, 0
                        elif n_y == 151 and n_x > 50:
                            n_y = 100 + n_x
                            n_x = 50
                            nd_x, nd_y = -1, 0
                        elif n_y < 201:
                            if n_x == 0:
                                n_x = n_y - 100
                                n_y = 1
                                nd_x, nd_y = 0, 1
                            elif n_x == 51:
                                n_x = n_y - 100
                                n_y = 150
                                nd_x, nd_y = 0, -1
                        elif n_y == 201:
                            n_y = 1
                            n_x = n_x + 100
                            nd_x, nd_y = 0, 1
                    if board[n_y][n_x] == "#":
                        break
                    else:
                        x, y = n_x, n_y
                        d_x, d_y = nd_x, nd_y

            case "R":
                d_x, d_y = (-d_y, d_x)
            case "L":
                d_x, d_y = (d_y, -d_x)
            case _:
                raise ValueError("Unexpected value:", m)

    print("Part 2:", (1000 * y + 4 * x + dir_values[d_x, d_y]))


p1()
p2()
