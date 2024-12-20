"""
Advent Of Code
--- Day 20: Race Condition ---
https://adventofcode.com/2024/day/20
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
        self.route = set()
        for r, line in enumerate(input):
            for c, ch in enumerate(line):
                if ch != '#':
                    self.route.add((r, c))
                if ch == 'S':
                    self.start = (r, c)
                elif ch == 'E':
                    self.end = (r, c)


        q = [(0, self.start)]
        dist = defaultdict(lambda: 1e9)
        while q:
            d, pos = q.pop(0)
            dist[pos] = d
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos in self.route and d < dist[new_pos]:
                    q.append((d+1, new_pos))
        self.dist = dist

    def count_cheats(self, m):
        cheats = {}
        for r in self.route:
            for d1 in range(m+1):
                for d2 in range(m+1-d1):
                    for d in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                        r2 = (r[0] + d[0]*d1, r[1] + d[1]*d2)
                        if r != r2 and r2 in self.route:
                            if self.dist[r2] - self.dist[r] > d1+d2:
                                cheats[r, r2] = self.dist[r2] - self.dist[r] - d1 - d2
        save = defaultdict(int)
        for c in cheats:
            save[cheats[c]] += 1
        return save

    def solve(self):
        save = self.count_cheats(2)
        return sum(save[s] for s in save if s >= 100)

    def solve2(self):
        save = self.count_cheats(20)
        return sum(save[s] for s in save if s >= 100)

in1 = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""
# assert(Solver(in1).solve(1) == 0)
# assert(Solver(in1).solve(2) == 0)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
