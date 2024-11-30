f = open('d02.in', 'r')


def findResult(lines):
    position = 0
    depth = 0
    for line in lines:
        (direction, amount) = line.split()
        amount = int(amount)
        if direction == 'down':
            depth += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'forward':
            position += amount
    return position * depth


def findResult2(lines):
    position = 0
    depth = 0
    aim = 0
    for line in lines:
        (direction, amount) = line.split()
        amount = int(amount)
        if direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'forward':
            position += amount
            depth += aim * amount
    return position * depth


lines = f.read().strip().split('\n')
print("Puzzle 1: ", findResult(lines))
print("Puzzle 2: ", findResult2(lines))
