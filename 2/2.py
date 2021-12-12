def part1() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    h = 0
    d = 0

    for i in lines:
        command = i.split()
        if command[0] == "forward":
            h += int(command[1])
        elif command[0] == "down":
            d += int(command[1])
        elif command[0] == "up":
            d -= int(command[1])

    return h * d
        
print("part1: ", part1())

def part2() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    aim = 0
    h = 0
    d = 0

    for i in lines:
        command = i.split()
        if command[0] == "forward":
            h += int(command[1])
            d += int(command[1]) * aim
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    return h * d

print("part2: ", part2())
