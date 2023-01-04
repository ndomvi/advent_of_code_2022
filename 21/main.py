import time

dat = [i.strip() for i in open("input.txt")]
resolved: dict[str, float] = {}
unresolved: dict[str, list[str]] = {}
for line in dat:
    name, *params = line.split(" ")
    name = name[:-1]
    if len(params) == 1:
        resolved[name] = int(params[0])
    else:
        unresolved[name] = params


def resolve(name: str) -> float:
    if name in resolved:
        return resolved[name]

    lhs_unres, op, rhs_unres = unresolved[name]
    lhs = resolve(lhs_unres)
    rhs = resolve(rhs_unres)
    res = 0.0
    match op:
        case "+":
            res = lhs + rhs
        case "-":
            res = lhs - rhs
        case "*":
            res = lhs * rhs
        case "/":
            res = lhs / rhs
        case _:
            print("unknown op:", op)

    resolved[name] = res

    return res


resolved_orig = resolved.copy()
print("Part 1:", round(resolve("root")))


def tree_prune(name: str, root: str) -> bool:
    if root == name:
        return True
    if root in resolved:
        return False

    lhs, _, rhs = unresolved[root]
    l = tree_prune(name, lhs)
    r = tree_prune(name, rhs)

    if not l:
        resolve(lhs)
    if not r:
        resolve(rhs)

    return l or r


resolved = resolved_orig
tree_prune("humn", "root")
start = time.perf_counter()
lhs = unresolved["root"][0]
rhs = unresolved["root"][2]
n = 0
step = 1
while True:
    resolved = resolved_orig.copy()
    resolved["humn"] = n
    if resolve(lhs) == resolve(rhs):
        print("Part 2:", round(n))
        break

    if n % 1000 == 0:
        print(f"1000 in {time.perf_counter()-start}")
        delta = resolve(lhs) - resolve(rhs)
        print("∆:", delta)
        if abs(delta) > 10000:
            step = delta // 10000
        else:
            step = 1
        start = time.perf_counter()
    n += step
