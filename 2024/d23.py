"""
Advent Of Code
--- Day 23: LAN Party ---
https://adventofcode.com/2024/day/23
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
        self.connections = set()
        self.computers = set()
        for l in input:
            a, b = l.split('-')
            self.connections.update([(a, b), (b, a)])
            self.computers.update([a, b])

    def solve(self):
        s = 0
        for (a, b) in self.connections:
            for c in self.computers:
                if (b, c) in self.connections and (c, a) in self.connections:
                    if a[0] == 't' or b[0] == 't' or c[0] == 't':
                        s += 1
        return s//6


    def solve2(self):
        groups = [set(c) for c in self.connections if c[0] < c[1]]
        while True:
            flag = False
            for g in groups:
                for c in self.computers:
                    if c not in g and all([(c, x) in self.connections for x in g]):
                        g.add(c)
                        flag = True
            if not flag:
                break
        m = max([len(g) for g in groups])
        group = [g for g in groups if len(g) == m][0]
        return ','.join(sorted(group))

in1 = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""
assert(Solver(in1).solve(1) == 7)
assert(Solver(in1).solve(2) == "co,de,ka,ta")
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
