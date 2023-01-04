dat: list[tuple[int,
                bool]] = [(int(i.strip()), False) for i in open("input.txt")]


# Numbers need to be wrapped in this class to be able to find a specific instance of a number
class Num:
    def __init__(self, val: int) -> None:
        self.val = val


orig = [Num(i * 811589153) for i, _ in dat]

# Fast, but does not work for part 2 :(
curr = 0
while curr != len(dat):
    val, moved = dat[curr]
    if moved:
        curr += 1
        continue

    dat.pop(curr)
    idx = (curr + val) % len(dat)
    dat.insert(idx, (val, True))
    curr = max(curr - 2, 0)

res = [i for i, _ in dat]
offset = res.index(0)
print("Part 1:",
      (res[(1000 + offset) % len(res)] + res[(2000 + offset) % len(res)] +
       res[(3000 + offset) % len(res)]))

nums = orig.copy()

zero = None
for i in nums:
    if i.val == 0:
        zero = i
        break
assert zero is not None

for _ in range(10):
    for i in orig:
        idx = nums.index(i)
        nums.pop(idx)
        n_idx = (idx + i.val) % len(nums)
        nums.insert(n_idx, i)

res = [i.val for i in nums]
offset = nums.index(zero)
print("Part 2:",
      (res[(1000 + offset) % len(res)] + res[(2000 + offset) % len(res)] +
       res[(3000 + offset) % len(res)]))
