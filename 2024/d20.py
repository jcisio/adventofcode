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
from heapq import heappop, heappush


parts = [1]

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
            d, pos = heappop(q)
            if d > dist[pos]:
                continue
            else:
                dist[pos] = d
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if new_pos in self.route and d < dist[new_pos]:
                    heappush(q, (d+1, new_pos))
        self.dist = dist

    def solve(self):
        cheats = {}
        for r in self.route:
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (r[0] + dir[0], r[1] + dir[1]) not in self.route and (r[0] + 2*dir[0], r[1] + 2*dir[1]) in self.route:
                    if self.dist[r[0] + 2*dir[0], r[1] + 2*dir[1]] - self.dist[r] > 2:
                        cheats[r, dir] = self.dist[r[0] + 2*dir[0], r[1] + 2*dir[1]] - self.dist[r] - 2
        save = defaultdict(int)
        for c in cheats:
            save[cheats[c]] += 1
        for s in sorted(save):
            print(save[s], s)
        return sum(save[s] for s in save if s >= 100)

    def solve2(self):
        return 0

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
assert(Solver(in1).solve(1) == 0)
# assert(Solver(in1).solve(2) == 0)

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
