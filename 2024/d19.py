"""
Advent Of Code
--- Day 19: Linen Layout ---
https://adventofcode.com/2024/day/19
"""
class Solver:
    def __init__(self, input):
        if input == '.test':
            f = open(__file__[:-3] + input, 'r')
            self.input = f.read().strip().split('\n')
        else:
            self.input = input.strip().split('\n')

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()

### No change before this ###

import time
from collections import defaultdict
from functools import cache


parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.patterns = input[0].split(', ')
        self.designs = input[2:]

    @cache
    def count(self, design):
        if design == '':
            return 1
        return sum(self.count(design[len(p):]) for p in self.patterns if design[0:len(p)]==p)

    def solve(self):
        return sum(1 if self.count(d) > 0 else 0 for d in self.designs)

    def solve2(self):
        return sum(self.count(d) for d in self.designs)

in1 = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""
assert(Solver(in1).solve(1) == 6)
assert(Solver(in1).solve(2) == 16)

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
