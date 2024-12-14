"""
Advent Of Code
--- Day 14: Restroom Redoubt ---
https://adventofcode.com/2024/day/14
"""
import time
import parse


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.robots = [list(parse.parse("p={:d},{:d} v={:d},{:d}", l).fixed) for l in input]
        self.X = 101
        self.Y = 103

    def move(self):
        for r in self.robots:
            r[0] = (r[0] + r[2]) % self.X
            r[1] = (r[1] + r[3]) % self.Y

    def solve(self):
        #self.X, self.Y = 11, 7
        for _ in range(100):
            self.move()
        s1 = sum(1 for r in self.robots if r[0] < self.X//2 and r[1] < self.Y//2)
        s2 = sum(1 for r in self.robots if r[0] > self.X//2 and r[1] < self.Y//2)
        s3 = sum(1 for r in self.robots if r[0] < self.X//2 and r[1] > self.Y//2)
        s4 = sum(1 for r in self.robots if r[0] > self.X//2 and r[1] > self.Y//2)
        print(s1, s2, s3, s4)
        return s1*s2*s3*s4

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
