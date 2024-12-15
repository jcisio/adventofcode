"""
Advent Of Code
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.walls = set()
        self.boxes = set()
        self.robot = (0,0)
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c == 'O':
                    self.boxes.add((x, y))
                elif c == '@':
                    self.robot = (x, y)
            if line == '':
                break
        
        self.moves = ''.join(input[y+1:])
        self.X = max(x for x, _ in self.walls) + 1
        self.Y = max(y for _, y in self.walls) + 1

    def move(self, m):
        d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[m]
        n = (self.robot[0] + d[0], self.robot[1] + d[1])
        if n in self.walls:
            return
        if n not in self.boxes:
            self.robot = n
            return
        n2 = (n[0] + d[0], n[1] + d[1])
        while n2 in self.boxes:
            n2 = (n2[0] + d[0], n2[1] + d[1])
        if n2 not in self.walls:
            self.boxes.remove(n)
            self.boxes.add(n2)
            self.robot = n
        
    def solve(self):
        for m in self.moves:
            self.move(m)
        return sum(x + y*100 for x, y in self.boxes)

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
