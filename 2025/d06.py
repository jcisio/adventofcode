"""
Advent Of Code
--- Day 6: Trash Compactor ---
https://adventofcode.com/2025/day/6
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

import time


class Problem:
    def __init__(self, input):
        self.operators = input[-1].split()
        self.input = input

    def compute(self):
        s = 0
        for j in range(len(self.operands[0])):
            result = self.operands[0][j]
            for i in range(1, len(self.operands)):
                if self.operators[j] == '*':
                    result *= self.operands[i][j]
                else:
                    result += self.operands[i][j]
            s += result
        return s

    def solve(self):
        self.operands = []
        for line in self.input[:-1]:
            self.operands.append(list(map(int, line.split())))
        return self.compute()

    def solve2(self):
        maxlength = max(len(x) for x in self.input[:-1])
        self.input = [x.ljust(maxlength) for x in self.input]
        ops = self.input[-1] + ' '
        width = []
        for c in ops:
            if c == ' ':
                width[-1] += 1
            else:
                width.append(0)

        s = 0
        p = 0
        # Do each problem
        for i in range(len(width)):
            operands = [0] * width[i]
            for j in range(width[i]-1, -1, -1):
                for k in range(len(self.input)-1):
                    if self.input[k][j+p] != ' ':
                        operands[j] = operands[j] * 10 + int(self.input[k][j+p])
            p += width[i] + 1
            result = operands[0]
            for j in range(1, len(operands)):
                if self.operators[i] == '*':
                    result *= operands[j]
                else:
                    result += operands[j]
            s += result
        return s

in1 = """
123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +
"""
assert(Solver(in1).solve(1) == 4277556)
assert(Solver(in1).solve(2) == 3263827)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
