"""
Advent Of Code
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.R = [int(input[i].split(': ')[1]) for i in range(3)]
        self.prog = list(map(int, input[4].split(': ')[1].split(',')))
        self.p = 0

    def combo(self, op):
        if 4 <= op <= 6:
            return self.R[op-4]
        else:
            return op

    def solve(self):
        output = []
        while self.p < len(self.prog):
            p = self.p
            self.p += 2
            if self.prog[p] == 0:
                self.R[0] = self.R[0] // (2**self.combo(self.prog[p+1]))
            elif self.prog[p] == 1:
                self.R[1] = self.R[1] ^ self.prog[p+1]
            elif self.prog[p] == 2:
                self.R[1] = self.combo(self.prog[p+1]) % 8
            elif self.prog[p] == 3:
                if self.R[0] != 0:
                    self.p = self.prog[p+1]
            elif self.prog[p] == 4:
                self.R[1] = self.R[1] ^ self.R[2]
            elif self.prog[p] == 5:
                output.append(self.combo(self.prog[p+1]) % 8)
            elif self.prog[p] == 6:
                self.R[1] = self.R[0] // (2**self.combo(self.prog[p+1]))
            elif self.prog[p] == 7:
                self.R[2] = self.R[0] // (2**self.combo(self.prog[p+1]))
        print(','.join(map(str,output)))
        return 0

    def solve2(self):
        return 0

### No change after this ###

class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + ('.in' if example else '.test'), 'r')
solver = Solver(f.read().strip().split('\n'))
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
