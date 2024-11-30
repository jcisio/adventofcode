import math

f = open('d03.in', 'r')

def findTrees(trees, dx, dy):
    c, i, j, l = 0, 0, 0, len(trees[0])
    while i < len(trees):
        if trees[i][j] == '#':
            c += 1
        i += dy
        j = (j + dx) % l
    print(c)
    return c

trees = list(f.read().strip().split('\n'))
print("Puzzle 1: ", findTrees(trees, 3, 1))
print("Puzzle 2: ", math.prod(findTrees(trees, dx, dy) for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]))