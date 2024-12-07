"""
Advent Of Code
--- Day 7: Bridge Repair ---
https://adventofcode.com/2024/day/7
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = []
        for row in input:
            r = row.split(': ')
            self.input.append((int(r[0]), list(map(int, r[1].split()))))

    def is_ok(self, test, numbers, part=1):
        if test < numbers[0]:
            return False
        if len(numbers) == 1:
            return test == numbers[0]
        if self.is_ok(test, [numbers[0] + numbers[1]] + numbers[2:], part) or self.is_ok(test, [numbers[0] * numbers[1]] + numbers[2:], part):
            return True
        if part == 2 and self.is_ok(test, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], part):
            return True
        return False

    def solve(self):
        return sum(line[0] for line in self.input if self.is_ok(line[0], line[1], 1))

    def solve2(self):
        return sum(line[0] for line in self.input if self.is_ok(line[0], line[1], 2))

### No change after this ###

class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + ('.in' if example else '.test'), 'r')
solver = Solver(f.read().strip().split('\n'))
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
