"""
Advent Of Code
--- Day 13: Claw Contraption ---
https://adventofcode.com/2024/day/13
"""
import time
import parse


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        machines = []
        for i in range(len(input)//4+1):
            machines.append({
                "a": parse.parse("Button A: X+{:d}, Y+{:d}", input[i*4]).fixed,
                "b": parse.parse("Button B: X+{:d}, Y+{:d}", input[i*4+1]).fixed,
                "prize": parse.parse("Prize: X={:d}, Y={:d}", input[i*4+2]).fixed,
            })
        self.machines = machines

    def min_token(self, m):
        c = m["a"][0]*m["b"][1] - m["a"][1]*m["b"][0]
        if c == 0:
            print(m)
            return 0
        else:
            x = (m["prize"][0]*m["b"][1] - m["prize"][1]*m["b"][0]) / c
            y = (m["a"][0]*m["prize"][1] - m["a"][1]*m["prize"][0]) / c
            if x < 0 or y < 0 or not x.is_integer() or not y.is_integer():
                return 0
            else:
                return x*3 + y

    def solve(self):
        return sum([self.min_token(m) for m in self.machines])

    def solve2(self):
        return 0

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
