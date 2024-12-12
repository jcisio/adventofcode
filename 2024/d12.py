"""
Advent Of Code
--- Day 12: Garden Groups ---
https://adventofcode.com/2024/day/12
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.plants = {}
        for r in range(len(input)):
            for c in range(len(input[r])):
                self.plants[(r, c)] = input[r][c]
        self.nr = len(input)
        self.nc = len(input[0])

    def fill(self, r, c, region, bound):
        if (r, c) in region:
            return
        region.add((r, c))
        b = 0
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + d[0] < self.nr and 0 <= c + d[1] < self.nc:
                if self.plants[(r, c)] == self.plants[(r+d[0], c+d[1])]:
                    b += 1
                    self.fill(r+d[0], c+d[1], region, bound)
        bound[(r, c)] = b

    def cost(self, r, c, visited):
        if (r, c) in visited:
            return 0
        region = set()
        bound = {}
        self.fill(r, c, region, bound)
        visited.update(region)
        return len(region) * (len(region)*4 - sum(bound.values()))

    def solve(self):
        visited = set()
        return sum(self.cost(r, c, visited) for r, c in self.plants)

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
