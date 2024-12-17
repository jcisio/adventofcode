"""
Advent Of Code
--- Day 17: Chronospatial Computer ---
https://adventofcode.com/2024/day/17
"""
import time


example = False
parts = [1,2]

class Problem:
    def __init__(self, input):
        self.R = [int(input[i].split(': ')[1]) for i in range(3)]
        self.prog = list(map(int, input[4].split(': ')[1].split(',')))

    def combo(self, op, R):
        if 4 <= op <= 6:
            return R[op-4]
        else:
            return op

    def run(self, R, prog):
        output = []
        p = 0
        while p < len(prog):
            np = p + 2
            if prog[p] == 0:
                R[0] = R[0] // (2**self.combo(prog[p+1], R))
            elif prog[p] == 1:
                R[1] = self.R[1] ^ prog[p+1]
            elif prog[p] == 2:
                R[1] = self.combo(prog[p+1], R) % 8
            elif prog[p] == 3:
                if R[0] != 0:
                    np = prog[p+1]
            elif prog[p] == 4:
                R[1] = R[1] ^ R[2]
            elif prog[p] == 5:
                output.append(self.combo(prog[p+1], R) % 8)
            elif prog[p] == 6:
                R[1] = R[0] // (2**self.combo(prog[p+1], R))
            elif prog[p] == 7:
                R[2] = R[0] // (2**self.combo(prog[p+1], R))
            p = np
        return ','.join(map(str,output))

    def solve(self):
        print(self.run(self.R, self.prog))
        return 0

    def solve2(self):
        prog = ','.join(map(str,self.prog))
        R = [1, 0, 0]
        while True:
            if prog == self.run(R.copy(), self.prog):
                break
            R[0] += 1
            if R[0]%1000 == 0: print(R[0])
        return R[0]

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
