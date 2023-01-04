from collections import defaultdict
from functools import lru_cache

dat = [i.strip() for i in open("input.txt")]

valves: dict[str, tuple[int, set[str]]] = {}
dist: defaultdict[tuple[str, str], int] = defaultdict(lambda: 61)
pressurised_valves: set[str] = set()

for line in dat:
    parts = line.split(" ")
    name = parts[1]
    rate = int(parts[4][5:-1])
    paths = {path.strip(",") for path in parts[9:]}
    valves[name] = (rate, paths)
    dist[name, name] = 0
    for path in paths:
        dist[name, path] = 1

    if rate > 0:
        pressurised_valves.add(name)

# Floyd–Warshall algorithm
for k in valves.keys():
    for i in valves.keys():
        for j in valves.keys():
            dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])


@lru_cache(maxsize=None)
def explore(open_valves: tuple[str],
            current_valve: str,
            time_left: int,
            elephant: bool = False) -> int:
    if time_left <= 0 or len(open_valves) == len(pressurised_valves):
        if elephant:
            return 0
        # unleash the elephant
        return explore(open_valves, "AA", 26, True)

    max_val = 0
    for valve in pressurised_valves - set(open_valves):
        d = dist[current_valve, valve]
        if valve == current_valve or (time_left - d) < 1:
            continue

        if valves[current_valve][0] == 0:
            max_val = max(max_val,
                          explore(open_valves, valve, time_left - d, elephant))

        max_val = max(
            max_val, valves[current_valve][0] * (time_left - 1) +
            explore(tuple(sorted(open_valves + (current_valve, ))), valve,
                    time_left - 1 - d, elephant))

    # if not elephant:
    #     if valves[current_valve][0] == 0:
    #         max_val = max(max_val, explore(open_valves, "AA", 26, True))
    #     max_val = max(
    #         max_val, valves[current_valve][0] * (time_left - 1) +
    #         explore(tuple(sorted(open_valves +
    #                              (current_valve, ))), "AA", 26, True))
    return max_val


# Part 1: 2077
print("Part 1:", explore((), 'AA', 30, True))
# Part 2: 2741
print("Part 2:", explore((), 'AA', 26))
