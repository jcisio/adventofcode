"""
Advent Of Code
--- Day 11: Plutonian Pebbles ---
https://adventofcode.com/2024/day/11
"""
import time
from collections import defaultdict


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = {i:1 for i in map(int, input[0].split())}

    def blink(self, stones):
        new = defaultdict(int)
        for s in stones:
            if s == 0:
                new[1] += stones[s]
            else:
                ss = str(s)
                l = len(ss)
                if l % 2 == 0:
                    new[int(ss[0:l//2])] += stones[s]
                    new[int(ss[l//2:])] += stones[s]
                else:
                    new[s * 2024] += stones[s]
        return new


    def solve(self):
        for _ in range(25):
            self.input = self.blink(self.input)
        return sum(self.input.values())

    def solve2(self):
        for _ in range(75):
            self.input = self.blink(self.input)
        return sum(self.input.values())

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
