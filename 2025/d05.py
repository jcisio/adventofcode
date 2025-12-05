"""
Advent Of Code
--- Day 5: Cafeteria ---
https://adventofcode.com/2025/day/5
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
        self.fresh = []
        self.available = []
        for l in input:
            if l == '':
                continue
            i = l.split('-')
            if len(i) == 1:
                self.available.append(int(i[0]))
            else:
                self.fresh.append((int(i[0]), int(i[1])))

    def is_fresh(self, i):
        return any(f[0] <= i <= f[1] for f in self.fresh)

    def solve(self):
        return sum(1 for i in self.available if self.is_fresh(i))

    def solve2(self):
        return 0

in1 = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
assert(Solver(in1).solve(1) == 3)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
