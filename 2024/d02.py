"""
Advent Of Code
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""
from __future__ import annotations
from collections import defaultdict
import parse


class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def is_safe(self, report) -> int:
        for i in range(1, len(report)):
            if (report[i] - report[i-1])*(report[1] - report[0]) <= 0 or abs(report[i] - report[i-1]) > 3:
                return 0
        return 1

    def is_safe2(self, report) -> int:
        if self.is_safe(report): return 1
        for i in range(0, len(report)):
            if self.is_safe(report[:i] + report[i+1:]):
                return 1
        return 0

    def solve(self):
        return sum([self.is_safe(report) for report in self.input])

    def solve2(self):
        return sum([self.is_safe2(report) for report in self.input])


class Solver:
    def __init__(self, input) -> None:
        self.input = [list(map(int, line.split())) for line in input]

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
