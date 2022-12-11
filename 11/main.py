class Monkey:
    items: list[int]
    op_add = 0
    op_mul = 1
    op_self = False
    test = 1
    test_t: int
    test_f: int
    inspections = 0

    next_items: list[int]
    next_items_cur: list[int]

    def __init__(self,
                 items: list[int],
                 test: int,
                 test_t: int,
                 test_f: int,
                 op_add: int = 0,
                 op_mul: int = 1,
                 op_self: bool = False) -> None:
        self.items = items
        self.op_add = op_add
        self.op_mul = op_mul
        self.op_self = op_self
        self.test = test
        self.test_t = test_t
        self.test_f = test_f

        self.next_items = []

    def process(self):
        # if len(self.items) == 0:
        #     self.items = self.next_items
        #     self.next_items = []
        for idx, worry in enumerate(self.items):
            self.inspections += 1
            worry = worry * (worry
                             if self.op_self else self.op_mul) + self.op_add
            worry //= 3
            global monkeys
            if worry % self.test == 0:
                monkeys[self.test_t].items.append(worry)
            else:
                monkeys[self.test_f].items.append(worry)
        self.items = []


dat = []
global monkeys
monkeys: list[Monkey] = []
with open("input.txt") as f:
    tmp = f.read()
    dat = [m.split("\n") for m in tmp.split("\n\n")]
    for monkey in dat:
        st: list[int] = list(
            map(int, map(lambda x: x.strip(","), monkey[1].split(" ")[4:])))
        op, op_val = monkey[2].split(" ")[-2:]
        op_add = 0
        op_mul = 1
        op_self = False
        if op_val == "old":
            op_self = True
        elif op == "+":
            op_add = int(op_val)
        else:
            op_mul = int(op_val)

        test = int(monkey[3].split(" ")[-1])
        test_t = int(monkey[4].split(" ")[-1])
        test_f = int(monkey[5].split(" ")[-1])
        monkeys.append(
            Monkey(items=st,
                   test=test,
                   test_t=test_t,
                   test_f=test_f,
                   op_add=op_add,
                   op_mul=op_mul,
                   op_self=op_self))

for n in range(20):
    for m in monkeys:
        m.process()

insp = [m.inspections for m in monkeys]
insp.sort()
print("Part 1:", insp[-1] * insp[-2])
print("Part 2:")
