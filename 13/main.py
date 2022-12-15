from functools import cmp_to_key
import itertools
from typing import Any

dat: list[list[list[Any]
               | int]] = [[eval(j) for j in i.strip().split("\n")]
                          for i in open("input.txt").read().split("\n\n")]


def compare(a: list[Any] | int, b: list[Any] | int) -> bool | None:
    match (a, b):
        case int(a), int(b):
            if a == b:
                return None
            return a < b
        case list(a), list(b):
            for l, r in zip(a, b):
                v = compare(l, r)
                if v is not None:
                    return v
            if len(a) == len(b):
                return None
            return len(a) < len(b)
        case list(a), int(b):
            return compare(a, [b])
        case int(a), list(b):
            return compare([a], b)
        case _, _:
            pass
    raise TypeError(f"Wtf is ({a=}, {b=})")


print(
    "Part 1:",
    sum([
        i + 1 if v else 0
        for i, v in enumerate(map(lambda x: compare(x[0], x[1]), dat))
    ]))

dat_flat: list[list[Any] | int] = list(itertools.chain.from_iterable(dat))
dat_flat.append([[2]])
dat_flat.append([[6]])
# print(dat_flat)
dat_flat.sort(
    key=cmp_to_key(lambda x, y: -1 if compare(x, y) else 1))  # type: ignore
print("Part 2:", (dat_flat.index([[2]]) + 1) * (dat_flat.index([[6]]) + 1))
