"""
Advent Of Code
--- Day 16: Reindeer Maze ---
https://adventofcode.com/2024/day/16
"""
import time


example = True
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.walls = set()
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c == 'S':
                    self.start = (x, y)
                elif c == 'E':
                    self.end = (x, y)
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # CCW
        self.dir = 1 # East

    def solve(self):
        to_visit = [(self.start, self.dir)]
        costs = {to_visit[0]: 0}
        #print(self.start, self.dir)
        for cur, dir in to_visit:
            for d in [0, -1, 1]:
                nd = (dir + d) % 4
                next = cur[0]+self.dirs[nd][0], cur[1]+self.dirs[nd][1]
                if next not in self.walls:
                    new_cost = costs[cur, dir] + 1 + (0 if d == 0 else 1000)
                    if (next, nd) not in costs or new_cost < costs[next, nd]:
                        costs[next, nd] = new_cost
                        to_visit.append((next, nd))
                        # print(next, nd)
        return min(costs[self.end, d] for d in range(4) if (self.end, d) in costs)

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
