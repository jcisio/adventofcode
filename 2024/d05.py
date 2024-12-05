"""
Advent Of Code
--- Day 5: Print Queue ---
https://adventofcode.com/2024/day/5
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.ordering = []
        self.updates = []
        ordering = True
        for line in input:
            if line == "":
                ordering = False
                continue
            if ordering:
                self.ordering.append(list(map(int, line.split('|'))))
            else:
                x = line.split(',')
                self.updates.append({int(x[i]):i for i in range(len(x))})

    def is_correct(self, update):
        return all([update[o[0]] < update[o[1]] for o in self.ordering if o[0] in update and o[1] in update])

    def solve(self):
        s = 0
        for u in self.updates:
            if self.is_correct(u):
                for k in u.keys():
                    if u[k] == len(u)//2:
                        s += k
        return s

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
