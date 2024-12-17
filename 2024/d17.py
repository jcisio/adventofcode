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

    def combo(self, op, R):
        if 4 <= op <= 6:
            return R[op-4]
        else:
            return op

    def run(self, A, match=[]):
        output = []
        R = [A, 0, 0]
        prog = self.prog
        p = 0
        while p < len(prog):
            np = p + 2
            c = self.combo(prog[p+1], R)
            if prog[p] == 0:
                R[0] = R[0] // (2**c)
            elif prog[p] == 1:
                R[1] = R[1] ^ prog[p+1]
            elif prog[p] == 2:
                R[1] = c % 8
            elif prog[p] == 3:
                if R[0] != 0:
                    np = prog[p+1]
            elif prog[p] == 4:
                R[1] = R[1] ^ R[2]
            elif prog[p] == 5:
                output.append(c % 8)
                # Early quit to save time.
                if len(output) <= len(match) and output[-1] != match[len(output)-1]:
                    return []
            elif prog[p] == 6:
                R[1] = R[0] // (2**c)
            elif prog[p] == 7:
                R[2] = R[0] // (2**c)
            p = np
        return output

    def solve(self):
        print(','.join(map(str,self.run(self.R[0]))))
        return 0

    def solve2(self):
        L = len(self.prog)
        tests = [(0, L-1)]
        while tests:
            a, i = tests.pop(0)
            for j in range(8):
                if self.run(a*8+j, self.prog[i:]):
                    if i == 0:
                        return a*8+j
                    tests.append((a*8+j, i-1))
                    # print(tests)

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
