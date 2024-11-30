f = open('d23.in', 'r')


def makeAMove(next_cup, current):
    a = next_cup[current]
    b = next_cup[a]
    c = next_cup[b]
    dest_cup = current
    while True:
        dest_cup = dest_cup - 1 if dest_cup > 1 else dest_cup - 1 + len(next_cup)
        if dest_cup not in [a,b,c]: break
    next_cup[current] = next_cup[c]
    next_dest_cup = next_cup[dest_cup]
    next_cup[dest_cup] = a
    next_cup[c] = next_dest_cup
    return next_cup, next_cup[current]


def formatCups(next_cup):
    output = []
    cup = 1
    for i in range(len(next_cup)-1):
        cup = next_cup[cup]
        output.append(cup)
    return ''.join(map(str, output))


def findPuzzle1(circle):
    next_cup = dict()
    for i in range(-1, len(circle)-1):
        next_cup[circle[i]] = circle[i+1]
    current = circle[0]
    for i in range(10):
        next_cup, current = makeAMove(next_cup, current)
    return formatCups(next_cup)


def findPuzzle2(circle):
    next_cup = dict()
    circle += range(10, 1000001)
    for i in range(-1, len(circle)-1):
        next_cup[circle[i]] = circle[i+1]
    current = circle[0]
    for i in range(10000000):
        next_cup, current = makeAMove(next_cup, current)
    print(next_cup[1])
    return next_cup[1] * next_cup[next_cup[1]]


circle = list(map(int, f.read().strip()))
print("Puzzle 1: ", findPuzzle1(circle))
print("Puzzle 2: ", findPuzzle2(circle))
