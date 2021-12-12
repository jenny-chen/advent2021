import copy

def part1() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    count = [0] * len(lines[0])

    for line in lines:
        for i in range(len(line)):
            if line[i] == "1":
                count[i] += 1
            else:
                count[i] -= 1

    n = ""
    m = ""
    for i in count:
        if i > 0:
            n += "1"
            m += "0"
        else:
            n += "0"
            m += "1"

    n = int(n, 2)
    m = int(m, 2)

    return n * m
        
print("part1: ", part1())

def part2() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    potential = copy.deepcopy(lines)
    index = 0

    while len(potential) > 1:
        count = 0
        for line in potential:
            if line[index] == "1":
                count += 1
            else:
                count -= 1

        i = 0
        if count >= 0:
            while i < len(potential):
                if potential[i][index] != "1":
                    potential.pop(i)
                else:
                    i += 1

        else:
            while i < len(potential):
                if potential[i][index] != "0":
                    potential.pop(i)
                else:
                    i += 1

        index += 1

    n = int(potential[0], 2)

    potential = lines
    index = 0

    while len(potential) > 1:
        count = 0
        for line in potential:
            if line[index] == "1":
                count += 1
            else:
                count -= 1

        i = 0
        if count < 0:
            while i < len(potential):
                if potential[i][index] != "1":
                    potential.pop(i)
                else:
                    i += 1

        else:
            while i < len(potential):
                if potential[i][index] != "0":
                    potential.pop(i)
                else:
                    i += 1

        index += 1

    m = int(potential[0], 2)

    return n * m

print("part2: ", part2())

