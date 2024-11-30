import time


f = open('d05.in', 'r')
debug = False


def printMap(map, vent = []):
    global debug
    if not debug:
        return
    print("\033[2K", vent)
    for m in map:
        print(*m)
    time.sleep(1)
    print("\033[" + str(len(map)+2) + "F")

def findDangerousAreas(vents, included_diagonal = False):
    Nmax = max([max(vent) for vent in vents]) + 1
    map = [[0]*Nmax for i in range(Nmax)]
    for vent in vents:
        if vent[0] == vent[2]:
            for i in range(min(vent[1::2]), max(vent[1::2]) + 1):
                map[i][vent[0]] += 1
        elif vent[1] == vent[3]:
            for i in range(min(vent[0::2]), max(vent[0::2]) + 1):
                map[vent[1]][i] += 1
        elif included_diagonal:
            dx = 1 if vent[0] < vent[2] else -1
            dy = 1 if vent[1] < vent[3] else -1
            printMap(map, vent)
            for i in range(abs(vent[0] - vent[2]) + 1):
                map[vent[1]+dy*i][vent[0]+dx*i] += 1
                printMap(map, vent)
    printMap(map)
    return sum([sum([1 for x in line if x >= 2]) for line in map])

vents = [list(map(int, line.replace(' -> ', ',').split(','))) for line in f.read().strip().split('\n')]
print("Puzzle 1: ", findDangerousAreas(vents))
print("Puzzle 2: ", findDangerousAreas(vents, True))
