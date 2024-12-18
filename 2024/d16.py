"""
Advent Of Code
--- Day 16: Reindeer Maze ---
https://adventofcode.com/2024/day/16
"""

class Solver:
    def __init__(self, input):
        if input == '.test':
            f = open(__file__[:-3] + input, 'r')
            self.input = f.read().strip().split('\n')
        else:
            self.input = input.split('\n')

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()

### No change before this ###

import time
from collections import defaultdict
from heapq import heappop, heappush


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.walls = set()
        for y, line in enumerate(input):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c == 'S':
                    self.start = (x, y)
                elif c == 'E':
                    self.end = (x, y)
        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # CCW
        self.dir = 1 # East

    def print(self, p):
        dirs = "v>^<"
        return f"{dirs[p[1]]}{p[0]}"

    def pprint(self, visited):
        X, Y = max(x for x,y in self.walls)+1, max(y for x,y in self.walls)+1
        for y in range(Y):
            for x in range(X):
                if (x,y) in self.walls:
                    print(' ', end='')
                elif (x,y) == self.start:
                    print('S', end='')
                elif (x,y) == self.end:
                    print('E', end='')
                elif (x,y) in visited:
                    print('O', end='')
                else:
                    print(' ', end='')
            print()

    def debug(self, p, best, costs):
        result = []
        for b in best:
            if b[0] == p:
                for x in best[b]:
                    result.append((x, b))

        for x,b in result:
            print(f"{self.print(x)} --> {self.print(b)} cost={costs[b]}")

    def solve(self):
        to_visit = [(self.start, self.dir)]
        costs = {to_visit[0]: 0}
        #print(self.start, self.dir)
        for cur, dir in to_visit:
            for d in [0, -1, 1]:
                nd = (dir + d) % 4
                next = cur[0]+self.dirs[nd][0], cur[1]+self.dirs[nd][1]
                if next not in self.walls:
                    new_cost = costs[cur, dir] + 1 + (0 if d == 0 else 1000)
                    if (next, nd) not in costs or new_cost < costs[next, nd]:
                        costs[next, nd] = new_cost
                        to_visit.append((next, nd))
                        # print(next, nd)
        return min(costs[self.end, d] for d in range(4) if (self.end, d) in costs)

    def solve2(self):
        # distance, position, direction, path
        q = [(0, self.start, 1, [self.start])]
        visited = set()
        best = defaultdict(lambda: 1e9)
        min_score = 1e9
        while q:
            dist, pos, dir, path = heappop(q)
            # print(dist,  pos, dir)
            if dist > best[pos, dir]:
                continue
            else:
                best[pos, dir] = dist
            if pos == self.end and dist <= min_score:
                visited.update(path)
                min_score = dist
                # print(f"New best: {dist}")
            for d in [0, -1, 1]:
                nd = (dir + d) % 4
                next = pos[0]+self.dirs[nd][0], pos[1]+self.dirs[nd][1]
                if next not in self.walls:
                    heappush(q, (dist+1+(0 if d == 0 else 1000), next, nd, path+[next]))
        # for pos, dir in best:
        #     if pos == self.end:
        #         print(f"{pos}, {dir}, cost={best[pos, dir]}")
        # self.pprint(visited)
        return len(visited)

in1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
in2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

assert(Solver(in1).solve(1) == 7036)
assert(Solver(in2).solve(1) == 11048)
# print(Solver(in1).solve(2))
# print(Solver(in2).solve(2))
assert(Solver(in1).solve(2) == 45)
# assert(Solver(in2).solve(2) == 64)

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
