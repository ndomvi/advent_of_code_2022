dat = [i.strip() for i in open("input.txt")]

pwd = "/"
dirs: dict[str, tuple[int, set[str]]] = {}
processed_dirs: dict[str, int] = {}
for line in dat:
    if line.startswith("$"):
        cmd = line.split(" ")
        if cmd[1] == "cd":
            n_dir = cmd[2]
            if n_dir == "/":
                pwd = "/"
            elif n_dir == "..":
                pwd = '/'.join(pwd.split("/")[:-1])
                if pwd == "":
                    pwd = "/"
            else:
                if pwd != "/":
                    pwd = f"{pwd}/{n_dir}"
                else:
                    pwd = f"/{n_dir}"
    else:
        # ls-ing
        if pwd not in dirs:
            dirs[pwd] = (0, set())
        ftype, fname = line.split(" ")
        if ftype == "dir":
            dirs[pwd][1].add(f"{pwd}/{fname}" if pwd != "/" else f"/{fname}")
        else:
            dirs[pwd] = (dirs[pwd][0] + int(ftype), dirs[pwd][1])

# Reduce the dirs "tree" into a set consisting of (path, size)
# This whole thing needs to be refactored. It does work but it wish it didn't.
# It does too many checks on processed dirs, which can be eliminated.
while len(dirs) != 0:
    for d, v in dirs.items():
        # No unprocessed dirs left; size is known
        if len(v[1]) == 0:
            processed_dirs[d] = v[0]
    for pd, pv in processed_dirs.items():
        # Remove the processed dir from all dirs if necessary
        if pd in dirs:
            del dirs[pd]
        # Recalculate sizes based on the newly processed directory
        for d, v in dirs.items():
            if pd in v[1]:
                v[1].remove(pd)
                dirs[d] = (v[0] + pv, v[1])

s = 0
for size in processed_dirs.values():
    if size <= 100000:
        s += size

print("Part 1:", s)

dir_sizes = [v for v in processed_dirs.values()]
total_size = dir_sizes[-1]
dir_sizes.sort()
for size in dir_sizes:
    if ((70000000 - total_size) + size) > 30000000:
        print("Part 2:", size)
        break
