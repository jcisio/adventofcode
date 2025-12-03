"""
Advent Of Code
--- Day 3: Lobby ---
https://adventofcode.com/2025/day/3
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
        self.input = input

    def find_max(self, bank, n=12):
        batteries = [int(i) for i in bank]
        m = 0
        start = 0
        for nn in range(n):
            p, v = start, 0
            for i in range(p, len(batteries) - n + nn + 1):
                if v < batteries[i]:
                    v = batteries[i]
                    start = i + 1
            m = m * 10 + v
        return m

    def solve(self):
        return sum(self.find_max(i, 2) for i in self.input)

    def solve2(self):
        return sum(self.find_max(i, 12) for i in self.input)

in1 = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
assert(Solver(in1).solve(1) == 357)
assert(Solver(in1).solve(2) == 3121910778619)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
