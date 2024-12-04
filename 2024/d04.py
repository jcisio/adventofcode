"""
Advent Of Code
--- Day 4: Ceres Search ---
https://adventofcode.com/2024/day/4
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input
        self.rows = len(input)
        self.cols = len(input[0])

    def solve(self):
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.input[r][c] != 'X':
                    continue
                for d in dir:
                    if r + 3*d[0] >= self.rows or c + 3*d[1] >= self.cols or r + 3*d[0] < 0 or c + 3*d[1] < 0:
                        continue
                    if self.input[r+d[0]][c+d[1]] == 'M' and self.input[r+2*d[0]][c+2*d[1]] == 'A' and self.input[r+3*d[0]][c+3*d[1]] == 'S':
                        count += 1
                        print(r,c,d)
        return count

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
