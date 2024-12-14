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

    def quadrants(self):
        s1 = sum(1 for r in self.robots if r[0] < self.X//2 and r[1] < self.Y//2)
        s2 = sum(1 for r in self.robots if r[0] > self.X//2 and r[1] < self.Y//2)
        s3 = sum(1 for r in self.robots if r[0] < self.X//2 and r[1] > self.Y//2)
        s4 = sum(1 for r in self.robots if r[0] > self.X//2 and r[1] > self.Y//2)
        return s1, s2, s3, s4 # top left, top right, bottom left, bottom right

    def solve(self):
        #self.X, self.Y = 11, 7
        for _ in range(100):
            self.move()
        s1, s2, s3, s4 = self.quadrants()
        #print(s1, s2, s3, s4)
        return s1*s2*s3*s4
    
    def print(self):
        for y in range(self.Y):
            for x in range(self.X):
                if any(r[0] == x and r[1] == y for r in self.robots):
                    print("#", end="")
                else:
                    print(".", end="")
            print()

    def is_tree(self):
        robots = set([(r[0], r[1]) for r in self.robots])
        for axe in range(-20, 20):
            middle = self.X//2 - axe
            ok = sum(1 for r in robots if any((middle*2-r[0]+i, r[1]) in robots for i in range(-3, 4)))
            if ok >= 0.7*len(robots): return True
        return False

    def solve2(self):
        for i in range(10000):
            self.move()
            if self.is_tree():
                print(i)
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
