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
        pos = []
        disk = list(map(int, list(input[0])))
        for b in range(len(disk)):
            pos.append(len(blocks))
            blocks += [b//2 if b%2==0 else '.'] * disk[b]
        self.disk = disk
        self.blocks = blocks
        self.files = len(disk) // 2 # last file
        self.pos = pos

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
    
    def sum(self):
        return sum([(0 if self.blocks[i]=='.' else self.blocks[i])*i for i in range(len(self.blocks))])

    def find_spaces(self, size):
        i = -1
        while i < len(self.blocks)-1:
            i += 1
            if self.blocks[i] != '.':
                continue
            d = 0
            while i+d < len(self.blocks) and self.blocks[i+d] == '.':
                if d == size-1:
                    return i
                d += 1
        return -1

    def solve2(self):
        #self.print()
        for f in range(self.files, -1, -1):
            file_pos = self.pos[f*2]
            size = self.disk[f*2]
            pos = self.find_spaces(size)
            if pos > -1 and pos < file_pos:
                self.blocks[pos:pos+size], self.blocks[file_pos:file_pos+size] = self.blocks[file_pos:file_pos+size], self.blocks[pos:pos+size]
                #self.print()
                #print(' ', f)
        return self.sum()

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
