"""
Advent Of Code
--- Day 18: RAM Run ---
https://adventofcode.com/2024/day/18
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


parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = [tuple(map(int, line.split(','))) for line in input]
        self.N = 71 if len(input) > 100 else 7
        self.top = 1024 if len(input) > 100 else 12

    def print(self):
        for y in range(self.N):
            for x in range(self.N):
                print(' ' if (x, y) in self.input[0:self.top] else '#', end='')
            print()

    def find(self, top):
        grid = set(self.input[:top])
        q = [(0, 0, 0)]
        seen = set()
        # self.print()
        while q:
            dist, x, y = q.pop(0)
            if (x,y) == (self.N-1,self.N-1):
                return dist
            for dx,dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx,ny = x+dx, y+dy
                if 0 <= nx < self.N and 0 <= ny < self.N and (nx,ny) not in grid and (nx,ny) not in seen:
                    q.append((dist+1, nx, ny))
                    seen.add((nx,ny))
        return 0

    def solve(self):
        return self.find(self.top)

    def solve2(self):
        top = self.top + 1
        while self.find(top) > 0:
            top += 1
        print(self.input[top-1])
        return top

in1 = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""
assert(Solver(in1).solve(1) == 22)
assert(Solver(in1).solve(2) == 21)

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
