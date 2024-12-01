"""
Advent Of Code
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self):
        lleft = sorted(self.input['left'])
        lright = sorted(self.input['right'])
        return sum([abs(x-y) for x, y in zip(lleft, lright)])

    def solve2(self):
        return 0


class Solver:
    def __init__(self, input) -> None:
        l = [list(map(int, line.split())) for line in input]
        self.input = {
            'left': [x[0] for x in l],
            'right': [x[1] for x in l],
        }

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
#print("Puzzle 2: ", solver.solve(2))
