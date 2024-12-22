"""
Advent Of Code
--- Day 22: Monkey Market ---
https://adventofcode.com/2024/day/22
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
from collections import defaultdict


class Problem:
    def __init__(self, input):
        self.input = list(map(int, input))

    def next(self, n, d = 1):
        for _ in range(d):
            n = ((n << 6) ^ n) & ((1 << 24) - 1)
            n = ((n >> 5) ^ n) & ((1 << 24) - 1)
            n = ((n << 11) ^ n) & ((1 << 24) - 1)
        return n

    def prices(self, n):
        prices = [n % 10]
        changes = []
        p = n
        for _ in range(2000):
            n = self.next(p)
            prices.append(n % 10)
            changes.append(n % 10 - p % 10)
            p = n
        return prices, changes

    def solve(self):
        return sum(self.next(n,2000) for n in self.input)

    def find_seq(self, n):
        prices, changes = self.prices(n)
        return {tuple(changes[i:i+4]): prices[i+4] for i in range(len(changes)-4, -1, -1)}

    def solve2(self):
        seq = defaultdict(int)
        for n in self.input:
            for k, v in self.find_seq(n).items():
                seq[k] += v
        return seq[max(seq, key=seq.get)]
in1 = """
1
10
100
2024
"""
in2 = """
1
2
3
2024
"""
assert(Solver(in1).solve(1) == 37327623)
assert(Solver(in2).solve(2) == 23)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
