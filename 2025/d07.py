"""
Advent Of Code
--- Day 7: Laboratories ---
https://adventofcode.com/2025/day/7
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

    def solve(self):
        c = 0
        ts = set([self.input[0].find('S')])

        for s in self.input[1:]:
            ts_next = set()
            for t in ts:
                if s[t] == '^':
                    ts_next.add(t - 1)
                    ts_next.add(t + 1)
                    c += 1
                else:
                    ts_next.add(t)
            ts = ts_next
        return c

    def solve2(self):
        return 0

in1 = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
assert(Solver(in1).solve(1) == 21)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
