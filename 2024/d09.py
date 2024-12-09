"""
Advent Of Code
--- Day 9: Disk Fragmenter ---
https://adventofcode.com/2024/day/9
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        blocks = []
        disk = list(map(int, list(input[0])))
        for b in range(len(disk)):
            blocks += [b//2 if b%2==0 else '.'] * disk[b]
        self.blocks = blocks

    def print(self):
        for b in self.blocks: print(b, end='')

    def solve(self):
        l, r = 0, len(self.blocks)-1
        while True:
            while self.blocks[l] != '.':
                l += 1
            while self.blocks[r] == '.':
                r -= 1
            if l >= r: break
            self.blocks[l], self.blocks[r] = self.blocks[r], self.blocks[l]
            #self.print()
            #print(' ', l, r)
        #self.print()
        return sum([self.blocks[i]*i for i in range(r+1)])

    def solve2(self):
        return 0

### No change after this ###

class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self, part):
        problem = Problem(self.input)
        return problem.solve() if part==1 else problem.solve2()


f = open(__file__[:-3] + ('.in' if example else '.test'), 'r')
solver = Solver(f.read().strip().split('\n'))
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
