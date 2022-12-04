dat = [i.strip() for i in open("input.txt")]

score = 0
for line in dat:
    a, b = line[0], line[1]
    match b:
        case 'X':
            score += 1
            match a:
                case 'A':
                    score += 3
                case 'B':
                    score += 0
                case 'C':
                    score += 6
        case 'Y':
            score += 2
            match a:
                case 'A':
                    score += 6
                case 'B':
                    score += 3
                case 'C':
                    score += 0
        case 'Z':
            score += 3
            match a:
                case 'A':
                    score += 0
                case 'B':
                    score += 6
                case 'C':
                    score += 3

print("Part 1:", score)

score = 0
for line in dat:
    a, b = line.split(' ')
    match b:
        case 'X':
            score += 0
            match a:
                case 'A':
                    score += 3
                case 'B':
                    score += 1
                case 'C':
                    score += 2
        case 'Y':
            score += 3
            match a:
                case 'A':
                    score += 1
                case 'B':
                    score += 2
                case 'C':
                    score += 3
        case 'Z':
            score += 6
            match a:
                case 'A':
                    score += 2
                case 'B':
                    score += 3
                case 'C':
                    score += 1

print("Part 2:", score)
