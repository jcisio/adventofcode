"""
Advent Of Code
--- Day 9: Movie Theater ---
https://adventofcode.com/2025/day/9
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

from itertools import combinations
import time


class Problem:
    def __init__(self, input):
        self.input = [tuple(map(int, line.split(','))) for line in input]

    def solve(self):
        return max((abs(x1-x2)+1)*(abs(y1-y2)+1) for (x1,y1), (x2,y2) in combinations(self.input, 2))

    def solve2(self):
        return 0

in1 = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
assert(Solver(in1).solve(1) == 50)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
