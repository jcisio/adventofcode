"""
Advent Of Code
--- Day 4: Printing Department ---
https://adventofcode.com/2025/day/4
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
        self.x = len(input[0])
        self.y = len(input)
        self.adj = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def count_adjacent(self, x, y):
        return sum(1 for dx, dy in self.adj if self.is_accessible(x+dx, y+dy))

    def is_accessible(self, x, y):
        return 0 <= x < len(self.input[0]) and 0 <= y < len(self.input) and self.input[y][x] == '@'

    def solve(self):
        return sum(1 for x in range(self.x) for y in range(self.y) if self.input[y][x] =='@' and self.count_adjacent(x, y)<4)

    def solve2(self):
        return 0

in1 = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
assert(Solver(in1).solve(1) == 13)
# assert(Solver(in1).solve(2) == 0)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
