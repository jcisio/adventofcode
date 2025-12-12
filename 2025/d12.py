"""
Advent Of Code
--- Day 12: Christmas Tree Farm ---
https://adventofcode.com/2025/day/12
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

        self.shapes = [input[i*5+1:i*5+4] for i in range(6)]
        self.regions = [list(map(int, line.replace('x', ' ').replace(':', '').split())) for line in input[30:]]

    def can_fit(self, region):
        shapes = [sum(1 for c in ''.join(shape) if c=='#') for shape in self.shapes]
        return region[0]*region[1] > sum(region[i+2]*shapes[i] for i in range(6)) + 5

    def solve(self):
        return len([True for region in self.regions if self.can_fit(region)])

    def solve2(self):
        return 0

in1 = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
assert(Solver(in1).solve(1) == 2)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
