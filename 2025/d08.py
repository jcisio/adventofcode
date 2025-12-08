"""
Advent Of Code
--- Day 8: Playground ---
https://adventofcode.com/2025/day/8
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

from collections import Counter
from itertools import combinations
import time


class Problem:
    def __init__(self, input):
        self.boxes = [tuple(map(int, line.split(','))) for line in input]
        d = {}
        for ((x1,y1,z1), (x2,y2,z2)) in combinations(self.boxes, 2):
            d[(x1,y1,z1), (x2,y2,z2)] = abs(x1-x2)**2 + abs(y1-y2)**2 + abs(z1-z2)**2
        self.distances = sorted(d, key=d.get)

    def connect(self, circuits, ab):
        m1, m2 = min(circuits[ab[0]], circuits[ab[1]]), max(circuits[ab[0]], circuits[ab[1]])
        for c in circuits:
            if circuits[c] == m2:
                circuits[c] = m1

    def solve(self):
        circuits = {b:i for i, b in enumerate(self.boxes)}
        for i in range(10 if len(circuits) < 100 else 1000):
            self.connect(circuits, self.distances[i])
        c = Counter(circuits.values())
        top3 = c.most_common(3)
        return top3[0][1] * top3[1][1] * top3[2][1]

    def solve2(self):
        return 0

in1 = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
assert(Solver(in1).solve(1) == 40)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
