"""
Advent Of Code
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        map = {}
        self.nr = len(input)
        self.nc = len(input[0])
        for r in range(self.nr):
            for c in range(self.nc):
                map[(r, c)] = int(input[r][c])
        self.map = map

    def count_next(self, r, c):
        if self.map[(r, c)] == 9:
            return set([(r, c)])
        ends = set()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (r+dr, c+dc) in self.map and self.map[(r+dr, c+dc)] == self.map[(r, c)]+1:
                ends.update(self.count_next(r+dr, c+dc))
        return ends

    def count_next2(self, r, c):
        if self.map[(r, c)] == 9:
            return 1
        count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (r+dr, c+dc) in self.map and self.map[(r+dr, c+dc)] == self.map[(r, c)]+1:
                count += self.count_next2(r+dr, c+dc)
        return count

    def solve(self):
        return sum([len(self.count_next(r, c)) for r in range(self.nr) for c in range(self.nc) if self.map[(r, c)] == 0])

    def solve2(self):
        return sum([self.count_next2(r, c) for r in range(self.nr) for c in range(self.nc) if self.map[(r, c)] == 0])

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
