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

    def find_max(self, bank):
        batteries = [int(i) for i in bank]
        p, v = 0, 0
        for i in range(len(batteries) - 1):
            if v < batteries[i]:
                p = i
                v = batteries[i]
        q, v = p + 1, 0
        for j in range(p + 1, len(batteries)):
            if v < batteries[j]:
                q = j
                v = batteries[j]
        return batteries[p]*10 + batteries[q]

    def solve(self):
        return sum(self.find_max(i) for i in self.input)

    def solve2(self):
        return 0

in1 = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
assert(Solver(in1).solve(1) == 357)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
