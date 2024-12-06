"""
Advent Of Code
--- Day 6: Guard Gallivant ---
https://adventofcode.com/2024/day/6
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
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
        visited = set([self.p])
        while True:
            next = (self.p[0] + self.dirs[self.d][0], self.p[1] + self.dirs[self.d][1])
            if 0 <= next[0] < self.nr and 0 <= next[1] < self.nc:
                if self.input[next[0]][next[1]] == '#':
                    self.d = (self.d + 1) % 4
                else:
                    self.p = next
                    visited.add(next)
                #print(self.d, next, self.input[next[0]][next[1]])
            else:
                break
        return len(visited)
    
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
            else:
                return len(visited)

    def solve2(self):
        s = 0
        for r in range(self.nr):
            for c in range(self.nc):
                if self.input[r][c] == '.':
                    self.input[r] = self.input[r][:c] + '#' + self.input[r][c+1:]
                    p = self.p
                    d = self.d
                    if self.visited() == 0:
                        s += 1
                    self.input[r] = self.input[r][:c] + '.' + self.input[r][c+1:]
                    self.p = p
                    self.d = d
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
#print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
