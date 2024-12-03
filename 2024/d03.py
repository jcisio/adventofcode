"""
Advent Of Code
--- Day 3: Mull It Over ---
https://adventofcode.com/2024/day/3
"""
from __future__ import annotations
import re

class Problem:
    def __init__(self, input) -> None:
        self.input = input

    def do_mul(self, t):
        a, b = map(int, t[4:-1].split(','))
        return a*b

    def solve(self):
        x = re.findall("mul\(\d{1,3},\d{1,3}\)", ''.join(self.input))
        return sum([self.do_mul(t) for t in x])

    def solve2(self):
        s = 0
        do = True
        for op in re.findall("(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", ''.join(self.input)):
            if op == "do()":
                do = True
            elif op == "don't()":
                do = False
            elif do:
                s += self.do_mul(op)
        return s


class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
