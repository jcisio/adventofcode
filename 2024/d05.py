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
        self.updates_list = []
        self.precedence = defaultdict(list)
        ordering = True
        for line in input:
            if line == "":
                ordering = False
                continue
            if ordering:
                o = list(map(int, line.split('|')))
                self.ordering.append(o)
                self.precedence[o[0]].append(o[1])
            else:
                x = line.split(',')
                self.updates.append({int(x[i]):i for i in range(len(x))})
                self.updates_list.append(list(map(int, x)))

    def is_correct(self, update):
        return all([update[o[0]] < update[o[1]] for o in self.ordering if o[0] in update and o[1] in update])

    def solve(self):
        s = 0
        for i, u in enumerate(self.updates):
            if self.is_correct(u):
                for k in u.keys():
                    if u[k] == len(u)//2:
                        s += k
        return s
    
    def sort(self, update):
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if update[j] in self.precedence and update[i] in self.precedence[update[j]]:
                    update[i], update[j] = update[j], update[i]
        return update

    def solve2(self):
        s = 0
        for i,u in enumerate(self.updates_list):
            if self.is_correct(self.updates[i]):
                continue
            u = self.sort(u)
            s += u[len(u)//2]
        return s

class Solver:
    def __init__(self, input) -> None:
        self.input = input

    def solve(self, part=1):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + '.in', 'r')
solver = Solver(f.read().strip().split('\n'))
print("Puzzle 1: ", solver.solve())
print("Puzzle 2: ", solver.solve(2))
