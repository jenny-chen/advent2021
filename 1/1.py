def part1() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    count = 0

    lst = []
    for i in lines:
        lst.append(int(i))

    last = lst[0]
    for i in lst:
        if i > last:
            count += 1
        
        last = i

    return count
        
print("part1: ", part1())

def part2() -> int:

    with open('input.txt') as data:
        lines = [x.strip() for x in data.readlines()]

    count = 0

    lst = []
    for i in lines:
        lst.append(int(i))

    last = lst[0] + lst[1] + lst[2]
    for i in range(1, len(lst)-2):
        curr = lst[i] + lst[i+1] + lst[i+2]
        if curr > last:
            count += 1
        
        last = curr

    return count

print("part2: ", part2())
