"""
Advent Of Code
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6
"""
import time


example, parts = True, [1, 2]

class Problem:
    def __init__(self, input):
        self.input = input
        self.nr = len(input)
        self.nc = len(input[0])
        for r in range(self.nr):
            for c in range(self.nc):
                if self.input[r][c] == '^':
                    self.p = (r, c)
        self.dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.d = 0

    def solve(self):
        return self.visited()

    # stuck -> 0
    def visited(self):
        visited = set([self.p])
        states = set([(self.p, self.d)])
        while True:
            next = (self.p[0] + self.dirs[self.d][0], self.p[1] + self.dirs[self.d][1])
            if 0 <= next[0] < self.nr and 0 <= next[1] < self.nc:
                if self.input[next[0]][next[1]] == '#':
                    self.d = (self.d + 1) % 4
                else:
                    self.p = next
                    visited.add(next)
                if (self.p, self.d) in states:
                    return 0
                states.add((self.p, self.d))
                #print(self.d, next, self.input[next[0]][next[1]])
            else:
                return len(visited)

    def solve2(self):
        s = 0
        for r in range(self.nr):
            for c in range(self.nc):
                if self.input[r][c] == '.':
                    self.input[r] = self.input[r][:c] + '#' + self.input[r][c+1:]
                    p, d = self.p, self.d
                    if self.visited() == 0:
                        s += 1
                    self.input[r] = self.input[r][:c] + '.' + self.input[r][c+1:]
                    self.p, self.d = p, d
        return s


class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in' if example else '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
for part in parts:
    start = time.time()
    result = solver.solve(part)
    length = time.time() - start
    print(f"Puzzle {part}: \033[1;31m{result}\033[0m in {length*1000:.0f} ms")
