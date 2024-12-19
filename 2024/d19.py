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


parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.patterns = input[0].split(', ')
        self.designs = input[2:]
        self.tested = {p: True for p in self.patterns}
        self.count = defaultdict(int)

    def is_possible(self, design):
        if design == '':
            return True
        if design in self.tested:
            return self.tested[design]
        self.tested[design] = sum(self.is_possible(design[len(p):]) for p in self.patterns if design[0:len(p)]==p)
        return self.tested[design]

    def possibility(self, design):
        if design == '':
            return 1
        if design in self.count:
            return self.count[design]

        ok = [p for p in self.patterns if design[0:len(p)]==p]
        if len(ok) == 0:
            self.count[design] = 0
        elif len(ok) == 1:
            self.count[ok[0]] = 1
            self.count[design] = self.possibility(design[len(ok[0]):])
        else:
            # print(ok)
            self.count[design] = sum(self.possibility(design[len(p):]) for p in ok if len(p) < len(design)) + sum(1 if len(p) == len(design) else 0 for p in ok)
        # print(design, self.count[design], self.count)
        return self.count[design]

    def solve(self):
        return sum(1 if self.is_possible(d) else 0 for d in self.designs)

    def solve2(self):
        return sum(self.possibility(d) for d in self.designs)

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
