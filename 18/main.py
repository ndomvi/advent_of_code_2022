import sys

sys.setrecursionlimit(12000)

dat = [i.strip() for i in open("input.txt")]
cubes = set(tuple(map(int, line.split(','))) for line in dat)

faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
surface = 0
for x, y, z in cubes:
    for dx, dy, dz in faces:
        if (x + dx, y + dy, z + dz) not in cubes:
            surface += 1
print("Part 1:", surface)

visited: set[tuple[int, int, int]] = set()


def dfs(cube: tuple[int, int, int]) -> int:
    if any(i < -1 or i > 20 for i in cube):
        return 0
    visited.add(cube)
    x, y, z = cube
    f = 0
    for dx, dy, dz in faces:
        n_cube = (x + dx, y + dy, z + dz)
        if n_cube in cubes:
            f += 1
        else:
            if n_cube not in visited:
                f += dfs(n_cube)
    return f


s = 0
for i in range(-1, 21):
    for j in range(-1, 21):
        for k in range(-1, 21):
            # Only start on edges
            # There are no coordinates <0 or >19
            if i == -1 or i == 20 or j == -1 or j == 20 or k == -1 or k == 20:
                if (i, j, k) not in visited:
                    s += dfs((i, j, k))

print("Part 2:", s)
