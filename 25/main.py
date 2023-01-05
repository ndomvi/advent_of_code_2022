dat = [i.strip() for i in open("input.txt")]


def stfu_to_dec(stfu: str) -> int:
    res = 0
    for i, c in enumerate(reversed(stfu)):
        val = 0
        match c:
            case "=":
                val = -2
            case "-":
                val = -1
            case num:
                val = int(num)
        res += val * (5**i)
    return res


def dec_to_stfu(num: int) -> str:
    # Generic conversion algorithm
    res = ""
    while num > 0:
        div, mod = divmod(num, 5)
        # We do not have a digit to represent a number greater than 2, so it should "overflow"
        res += "012=-"[mod]
        num = div
        # Everything makes sense, except this thing
        if mod > 2:
            # something similar to overflow, in case digit became negative
            num += 1

    return res[::-1]


s = 0
for line in dat:
    s += stfu_to_dec(line)

print("Sum is", s)
print("Part 1:", dec_to_stfu(s))
