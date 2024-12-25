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
from itertools import permutations, combinations


class Problem:
    def __init__(self, input):
        d = input.index('')
        self.gates = {l[0:3]: int(l[5]) for l in input[:d]}
        ops = [l.split() for l in input[d+1:]]
        self.ops = {op[4]: (op[1], min(op[0], op[2]), max(op[0], op[2]), op[4]) for op in ops}

    def sum(self, gates, o):
        zz = [k for k in gates if k[0] == o]
        return sum([gates[z] << int(z[1:]) for z in zz])

    def do_ops(self, opss):
        gates = {k: self.gates[k] for k in self.gates if k[0] in 'xy'}
        while True:
            ops = list(opss.keys()).copy()
            flag = False
            for op in ops:
                if opss[op][1] not in gates or opss[op][2] not in gates:
                    continue
                flag = True
                if opss[op][0] == 'AND':
                    gates[op] = gates[opss[op][1]] & gates[opss[op][2]]
                elif opss[op][0] == 'OR':
                    gates[op] = gates[opss[op][1]] | gates[opss[op][2]]
                elif opss[op][0] == 'XOR':
                    gates[op] = gates[opss[op][1]] ^ gates[opss[op][2]]
                del(opss[op])
            if not flag:
                break
        return self.sum(gates, 'z')

    def solve(self):
        return self.do_ops({k: self.ops[k] for k in self.ops})

    # Find the first wrong bit
    def find(self, opss1):
        gates = {k: self.gates[k] for k in self.gates if k[0] in 'xy'}
        opss = {k: v for k,v in opss1.items()}
        dep = {k: set() for k in gates}
        x = self.sum(gates, 'x')
        y = self.sum(gates, 'y')
        while True:
            ops = list(opss.keys())
            flag = False
            for op in ops:
                if opss[op][1] not in gates or opss[op][2] not in gates:
                    continue
                flag = True
                if opss[op][0] == 'AND':
                    gates[op] = gates[opss[op][1]] & gates[opss[op][2]]
                elif opss[op][0] == 'OR':
                    gates[op] = gates[opss[op][1]] | gates[opss[op][2]]
                elif opss[op][0] == 'XOR':
                    gates[op] = gates[opss[op][1]] ^ gates[opss[op][2]]
                dep[op] = dep[opss[op][1]].union(dep[opss[op][2]])
                if opss[op][1] in self.ops: dep[op].add(opss[op][1])
                if opss[op][2] in self.ops: dep[op].add(opss[op][2])
                del(opss[op])
            if not flag:
                break
        z = self.sum(gates, 'z')
        zz = x + y
        for i in range(45):
            if (zz & 1) != (z & 1):
                return i, dep
            zz >>= 1
            z >>= 1
        return -1, None

    def solve2(self):
        # A    XOR B    -> VAL0     <= FAGate0
        # A    AND B    -> VAL1     <= FAGate1
        # VAL0 AND CIN  -> VAL2     <= FAGate2
        # VAL0 XOR CIN  -> SUM      <= FAGate3
        # VAL1 OR  VAL2 -> COUT     <= FAGate4
        ops = self.ops
        vv = ops.values()

        xyxor_out = {k for k in ops if ops[k][0] == 'XOR' and ops[k][1][0] in 'xy' and ops[k][2][0] in 'xy'}
        xyand_out = {k for k in ops if ops[k][0] == 'AND' and ops[k][1][0] in 'xy' and ops[k][2][0] in 'xy' and ops[k][1][1:]!='00'}
        and_out = {k[3] for k in vv if k[0] == 'AND' and k[1][1:] != '00'}
        or_in = {k[1] for k in vv if k[0] == 'OR'} | {k[2] for k in vv if k[0] == 'OR'}
        and_in = {k[1] for k in vv if k[0] == 'AND'} | {k[2] for k in vv if k[0] == 'AND'}
        xor_in = {k[1] for k in vv if k[0] == 'XOR'} | {k[2] for k in vv if k[0] == 'XOR'}
        or_out = {k[3] for k in vv if k[0] == 'OR'}
        xor_out = {k[3] for k in vv if k[0] == 'XOR'}

        # gate 0
        wrong0 = [k for k in xyxor_out if k not in and_in and k not in xor_in and k[1:] != '00']

        # gate 1
        wrong1 = [k for k in xyand_out if k not in or_in]

        # gate 2
        wrong2 = [k for k in and_out.difference(xyand_out) if k not in or_in]

        # gate 3
        wrong3 = [k for k in xor_out.difference(xyxor_out) if k[0] != 'z']

        # gate 4
        wrong4 = [k for k in or_out if k not in and_in and k not in xor_in and k != 'z45']

        wrong = wrong0 + wrong1 + wrong2 + wrong3 + wrong4
        return ','.join(sorted(set(wrong)))

in1 = """
x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00
"""
# assert(Solver(in1).solve(1) == 9)
# assert(Solver(in1).solve(2) == 'z00,z01,z02,z05')
assert(Solver(".test").solve(2) == 'gjc,gvm,qjj,qsb,wmp,z17,z26,z39')
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
