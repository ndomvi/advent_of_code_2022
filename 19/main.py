from functools import lru_cache

dat = [i.strip() for i in open("input.txt")]

Blueprint = tuple[int, int, tuple[int, ...], tuple[int, ...]]
blueprints: list[Blueprint] = []
for line in dat:
    nums = tuple(map(int, filter(lambda x: x.isnumeric(), line.split(" "))))
    blueprints.append((nums[0], nums[1], tuple(nums[2:4]), tuple(nums[4:])))

global global_best
global_best = 0


@lru_cache(maxsize=None)
def explore(blueprint: Blueprint, robots: tuple[int, ...],
            resources: tuple[int, ...], time_left: int) -> int:
    global global_best
    if time_left == 0:
        global_best = max(global_best, resources[3])
        return resources[3]
    # Check whether it is possible to get more gems if we only create gem robots
    if (resources[3] + (robots[3] * time_left) +
        ((time_left * (time_left - 1)) // 2)) < global_best:
        return 0

    # There is no point in producing more resources than can be consumed in a single move
    # Thus, these subtrees can be pruned
    if robots[0] > max(blueprint[0], blueprint[1], blueprint[2][0],
                       blueprint[3][0]):
        return 0

    if robots[1] > blueprint[2][1]:
        return 0

    if robots[2] > blueprint[3][1]:
        return 0

    # Explore the tree
    o_ro = list(robots)
    o_re = list(resources)
    o_re = [
        o_ro[0] + o_re[0], o_ro[1] + o_re[1], o_ro[2] + o_re[2],
        o_ro[3] + o_re[3]
    ]

    m_geodes = 0
    # Ore robot
    if resources[0] >= blueprint[0]:
        ro = o_ro.copy()
        re = o_re.copy()
        ro[0] += 1
        re[0] -= blueprint[0]
        m_geodes = max(m_geodes,
                       explore(blueprint, tuple(ro), tuple(re), time_left - 1))
    # Clay robot
    if resources[0] >= blueprint[1]:
        ro = o_ro.copy()
        re = o_re.copy()
        ro[1] += 1
        re[0] -= blueprint[1]
        m_geodes = max(m_geodes,
                       explore(blueprint, tuple(ro), tuple(re), time_left - 1))

    # Obsidian robot
    if resources[0] >= blueprint[2][0] and resources[1] >= blueprint[2][1]:
        ro = o_ro.copy()
        re = o_re.copy()
        ro[2] += 1
        re[0] -= blueprint[2][0]
        re[1] -= blueprint[2][1]
        m_geodes = max(m_geodes,
                       explore(blueprint, tuple(ro), tuple(re), time_left - 1))

    # Geode robot
    if resources[0] >= blueprint[3][0] and resources[2] >= blueprint[3][1]:
        ro = o_ro.copy()
        re = o_re.copy()
        ro[3] += 1
        re[0] -= blueprint[3][0]
        re[2] -= blueprint[3][1]
        m_geodes = max(m_geodes,
                       explore(blueprint, tuple(ro), tuple(re), time_left - 1))

    # Save resources
    m_geodes = max(m_geodes,
                   explore(blueprint, tuple(o_ro), tuple(o_re), time_left - 1))

    return m_geodes


p1 = 0
for i, b in enumerate(blueprints):
    explore.cache_clear()
    global_best = 0
    res = explore(b, (1, 0, 0, 0), (0, 0, 0, 0), 24)
    print(i + 1, b, res, res * (i + 1))
    p1 += res * (i + 1)

print("Part 1:", p1)

p2 = 1
for i, b in enumerate(blueprints[:3]):
    explore.cache_clear()
    global_best = 0
    res = explore(b, (1, 0, 0, 0), (0, 0, 0, 0), 32)
    print(i + 1, b, res)
    p2 *= res

print("Part 2:", p2)
