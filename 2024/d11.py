"""
Advent Of Code
--- Day 11: Plutonian Pebbles ---
https://adventofcode.com/2024/day/11
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = list(map(int, input[0].split()))

    def blink(self, stones):
        new = []
        for s in stones:
            if s == 0:
                new.append(1)
            else:
                ss = str(s)
                l = len(ss)
                if l % 2 == 0:
                    new += [int(ss[0:l//2]), int(ss[l//2:])]
                else:
                    new.append(s * 2024)
        return new

    def solve(self):
        for i in range(25):
            self.input = self.blink(self.input)
        return len(self.input)

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
