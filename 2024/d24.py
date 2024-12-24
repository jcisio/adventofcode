"""
Advent Of Code
--- Day 24: Crossed Wires ---
https://adventofcode.com/2024/day/24
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
        d = input.index('')
        self.gates = {l[0:3]: int(l[5]) for l in input[:d]}
        ops = [l.split() for l in input[d+1:]]
        self.ops = {op[4]: (op[1], op[0], op[2]) for op in ops}

    def solve(self):
        while True:
            ops = list(self.ops.keys()).copy()
            flag = False
            for op in ops:
                if self.ops[op][1] not in self.gates or self.ops[op][2] not in self.gates:
                    continue
                flag = True
                if self.ops[op][0] == 'AND':
                    self.gates[op] = self.gates[self.ops[op][1]] & self.gates[self.ops[op][2]]
                elif self.ops[op][0] == 'OR':
                    self.gates[op] = self.gates[self.ops[op][1]] | self.gates[self.ops[op][2]]
                elif self.ops[op][0] == 'XOR':
                    self.gates[op] = self.gates[self.ops[op][1]] ^ self.gates[self.ops[op][2]]
                del(self.ops[op])
                # print(op, self.gates[op])
            if not flag:
                break
        zz = [k for k in self.gates if k[0] == 'z']
        return sum([self.gates[z] << int(z[1:]) for z in zz])

    def solve2(self):
        return 0

in1 = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02
"""
assert(Solver(in1).solve(1) == 4)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
