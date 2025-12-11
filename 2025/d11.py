"""
Advent Of Code
--- Day 11: Reactor ---
https://adventofcode.com/2025/day/11
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
        devices = {}
        for line in input:
            name, rest = line.split(': ')
            devices[name] = rest.split(' ')
        self.input = devices

    def solve(self):
        paths = {'out': 1}
        remaining = set(self.input.keys()) - {'out'}
        while remaining:
            for device in remaining.copy():
                outputs = self.input[device]
                if all(o in paths for o in outputs):
                    paths[device] = sum(paths[o] for o in outputs)
                    remaining.remove(device)
        return paths['you']

    def solve2(self):
        return 0

in1 = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
assert(Solver(in1).solve(1) == 5)
# assert(Solver(in1).solve(2) == 0)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
