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
        self.updates = []
        self.precedence = defaultdict(list)
        ordering = True
        for line in input:
            if line == "":
                ordering = False
                continue
            if ordering:
                o = tuple(map(int, line.split('|')))
                self.precedence[o[0]].append(o[1])
            else:
                self.updates.append(list(map(int, line.split(','))))

    def sort(self, update):
        correct = True
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if update[j] in self.precedence and update[i] in self.precedence[update[j]]:
                    correct = False
                    update[i], update[j] = update[j], update[i]
        return (correct, update)

    def solve(self):
        s = [0, 0]
        for u in self.updates:
            correct, u = self.sort(u)
            s[0 if correct else 1] += u[len(u)//2]
        return s

class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.test', 'r')
solver = Solver(f.read().strip().split('\n'))
s = solver.solve()
print("Puzzle 1: ", s[0])
print("Puzzle 2: ", s[1])
