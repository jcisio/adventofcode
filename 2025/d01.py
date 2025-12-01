"""
Advent Of Code
--- Day 1: Secret Entrance ---
https://adventofcode.com/2025/day/1
"""
class Solver:
    def __init__(self, input):
        if input == '.test':
            print(__file__[:-3] + input)
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

    def solve(self, pass_zero = False):
        p = 50
        zero = 0
        for i in self.input:
            o_p = p
            p = p + int(i[1:]) * (1 if i[0] == 'R' else -1)
            if p%100 == 0:
                zero += 1
            if pass_zero:
                if p > 100:
                    zero += (p - 1)//100
                elif p < 0:
                    zero += (-p - 1) // 100 + 1
                    if o_p == 0:
                        zero -= 1
            p %= 100
        return zero

    def solve2(self):
        return self.solve(True)

in1 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
assert(Solver(in1).solve(1) == 3)
assert(Solver(in1).solve(2) == 6)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
