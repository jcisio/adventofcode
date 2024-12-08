"""
Advent Of Code
--- Day 8: Resonant Collinearity ---
https://adventofcode.com/2024/day/8
"""
import time
from collections import defaultdict

example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = input
        self.nr = len(input)
        self.nc = len(input[0])
        self.antennas = defaultdict(list)
        for i in range(self.nr):
            for j in range(self.nc):
                if input[i][j] != '.':
                    self.antennas[input[i][j]].append((i,j))

    def solve(self):
        antinodes = set()
        for a in self.antennas.values():
            for i in range(len(a)):
                for j in range(i+1, len(a)):
                    if 0 <= a[i][0]*2-a[j][0] < self.nr and 0 <= a[i][1]*2-a[j][1] < self.nc:
                        antinodes.add((a[i][0]*2-a[j][0], a[i][1]*2-a[j][1]))
                    if 0 <= a[j][0]*2-a[i][0] < self.nr and 0 <= a[j][1]*2-a[i][1] < self.nc:
                        antinodes.add((a[j][0]*2-a[i][0], a[j][1]*2-a[i][1]))
        return len(antinodes)

    def solve2(self):
        return 0

### No change after this ###

class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + ('.in' if example else '.test'), 'r')
solver = Solver(f.read().strip().split('\n'))
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
