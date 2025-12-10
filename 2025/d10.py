"""
Advent Of Code
--- Day 10: Factory ---
https://adventofcode.com/2025/day/10
"""
class Solver:
    def __init__(self, input):
        if input == '.test':
            f = open(__file__[:-3] + input, 'r')
            self.input = f.read().strip().split('\n')
        else:
            self.input = input.strip().split('\n')

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()

### No change before this ###

from itertools import combinations
import time
from scipy.optimize import milp, LinearConstraint
import numpy as np


class Problem:

    class Machine:
        def __init__(self, states, buttons, joltage):
            self.states = states
            self.buttons = buttons
            self.joltage = joltage
        def parse(line):
            items = line.split()
            states = tuple(i == '#' for i in items[0][1:-1])
            buttons = sorted([set(map(int, item[1:-1].split(','))) for item in items[1:-1]], key=len, reverse=True)
            joltage = tuple(map(int, items[-1][1:-1].split(',')))
            return Problem.Machine(states, buttons, joltage)
        def min(self):
            for i in range(len(self.buttons)):
                for buttons in combinations(self.buttons, i+1):
                    states = [False]*len(self.states)
                    for button in buttons:
                        for j in button:
                            states[j] = not states[j]
                    if tuple(states) == self.states:
                        return i+1
            return len(self.joltage)
        def compute_joltage(self, buttons):
            joltage = [0]*len(self.joltage)
            for i, b in enumerate(buttons):
                for j in self.buttons[i]:
                    joltage[j] += b
            return joltage
        def min2(self):
            n = len(self.joltage)
            m = len(self.buttons)

            # Objective: minimize sum of all button presses (all coefficients = 1)
            c = np.ones(m)

            # Build constraint matrix A where A[j][i] = 1 if button i affects position j
            A = np.zeros((n, m))
            for i in range(m):
                for j in self.buttons[i]:
                    A[j][i] = 1

            # Equality constraints: A @ x == joltage
            constraints = LinearConstraint(A, lb=self.joltage, ub=self.joltage)

            # Optimize with all variables as integers
            return int(milp(c=c, constraints=constraints, integrality=np.ones(m)).fun)

    def __init__(self, input):
        self.input = [Problem.Machine.parse(line) for line in input]

    def solve(self):
        return sum(machine.min() for machine in self.input)

    def solve2(self):
        return sum(machine.min2() for machine in self.input)

in1 = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
assert(Solver(in1).solve(1) == 7)
assert(Solver(in1).solve(2) == 33)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
