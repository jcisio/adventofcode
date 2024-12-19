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


parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.patterns = input[0].split(', ')
        self.designs = input[2:]
        self.tested = {p: True for p in self.patterns}

    def is_possible(self, design):
        if design == '':
            return True
        if design in self.tested:
            return self.tested[design]
        self.tested[design] = any(self.is_possible(design[len(p):]) for p in self.patterns if design[0:len(p)]==p)
        return self.tested[design]

    def solve(self):
        return sum(1 if self.is_possible(d) else 0 for d in self.designs)

    def solve2(self):
        return 0

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
assert(Solver(in1).solve(2) == 0)

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
