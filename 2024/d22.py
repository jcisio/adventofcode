"""
Advent Of Code
--- Day 22: Monkey Market ---
https://adventofcode.com/2024/day/22
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


class Problem:
    def __init__(self, input):
        self.input = list(map(int, input))

    def next(self, n, d = 1):
        for _ in range(d):
            n = ((n << 6) ^ n) & ((1 << 24) - 1)
            n = ((n >> 5) ^ n) & ((1 << 24) - 1)
            n = ((n << 11) ^ n) & ((1 << 24) - 1)
        return n

    def solve(self):
        return sum(self.next(n,2000) for n in self.input)

    def solve2(self):
        return 0

in1 = """
1
10
100
2024
"""
assert(Solver(in1).solve(1) == 37327623)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
