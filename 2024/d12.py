"""
Advent Of Code
--- Day 12: Garden Groups ---
https://adventofcode.com/2024/day/12
"""
import time


example = True
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.plants = {}
        for r in range(len(input)):
            for c in range(len(input[r])):
                self.plants[(r, c)] = input[r][c]
        self.nr = len(input)
        self.nc = len(input[0])

    def fill(self, r, c, region):
        if (r, c) in region:
            return
        region.add((r, c))
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= r + d[0] < self.nr and 0 <= c + d[1] < self.nc:
                if self.plants[(r, c)] == self.plants[(r+d[0], c+d[1])]:
                    self.fill(r+d[0], c+d[1], region)

    def cost(self, r, c, visited, discount):
        if (r, c) in visited:
            return 0
        region = set()
        self.fill(r, c, region)
        visited.update(region)

        fences = set()
        for r, c in region:
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (r+d[0], c+d[1]) in region:
                    continue
                fences.add((r, c, d))

        if not discount:
            cost = len(fences)
        else:
            paid = set()
            cost = 0
            for fence in fences:
                if fence in paid:
                    continue
                paid.add(fence)
                cost += 1
                while True:
                    updated = False
                    for o in fences:
                        if o not in paid:
                            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                # Only two directions are possible, the other two are never in the fences
                                # so we can ignore them and simply check all directions.
                                if (o[0]+d[0], o[1]+d[1], o[2]) in paid:
                                    paid.add(o)
                                    updated = True
                    if not updated:
                        break

        return len(region) * cost

    def solve(self):
        visited = set()
        return sum(self.cost(r, c, visited, False) for r, c in self.plants)

    def solve2(self):
        visited = set()
        return sum(self.cost(r, c, visited, True) for r, c in self.plants)

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
