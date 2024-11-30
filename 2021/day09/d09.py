f = open('d09.in', 'r')


def findLowPoints(map):
    low_points = []
    for y in range(len(map)-2):
        for x in range(len(map[y])-2):
            if map[y+1][x+1] < min(map[y+1][x], map[y][x+1], map[y+1][x+2], map[y+2][x+1]):
                low_points.append((y+1, x+1))
    return low_points


def solvePart1(map):
    low_points = findLowPoints(map)
    return sum([int(map[low_point[0]][low_point[1]]) for low_point in low_points]) + len(low_points)


def findSizeBasin(map, low_point):
    basin = set()
    queue = [low_point]
    while queue:
        point = queue.pop(0)
        basin.add(point)
        for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            point_next = (point[0] + delta[0], point[1] + delta[1])
            if map[point_next[0]][point_next[1]] < '9' and point_next not in basin:
                queue.append(point_next)
    return len(basin)


def solvePart2(map):
    low_points = findLowPoints(map)
    sizes = sorted([findSizeBasin(map, low_point) for low_point in low_points], reverse=True)
    return sizes[0]*sizes[1]*sizes[2]


map = f.read().strip().split('\n')
# Add border for easy indexing.
map = ['A'*(len(map[0])+2)] + ['A'+line+'A' for line in map] + ['A'*(len(map[0])+2)]
print("Puzzle 1: ", solvePart1(map))
print("Puzzle 2: ", solvePart2(map))
