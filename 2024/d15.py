"""
Advent Of Code
--- Day 15: Warehouse Woes ---
https://adventofcode.com/2024/day/15
"""
import time


example = False
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.walls = set()
        self.boxes = set()
        self.robot = (0,0)
        self.input = input

    def move(self, m):
        d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[m]
        n = (self.robot[0] + d[0], self.robot[1] + d[1])
        if n in self.walls:
            return
        if n not in self.boxes:
            self.robot = n
            return
        n2 = (n[0] + d[0], n[1] + d[1])
        while n2 in self.boxes:
            n2 = (n2[0] + d[0], n2[1] + d[1])
        if n2 not in self.walls:
            self.boxes.remove(n)
            self.boxes.add(n2)
            self.robot = n

    def move2(self, m, debug=False):
        d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}[m]
        n = (self.robot[0] + d[0], self.robot[1] + d[1])
        if n in self.walls:
            return
        if d[1] == 0:
            if n not in self.boxes and (n[0]-1,n[1]) not in self.boxes:
                self.robot = n
                return
            if (n[0]-1,n[1]) in self.boxes:
                n = (n[0]-1,n[1])
            n2 = (n[0] + d[0]*2, n[1] + d[1])
            while n2 in self.boxes:
                n2 = (n2[0] + d[0]*2, n2[1])
            if debug:
                print(self.robot, n, n2)
                self.print()
            if (d[0] == 1 and n2 not in self.walls) or (d[0]==-1 and (n2[0]+1,n2[1]) not in self.walls):
                self.robot = (self.robot[0] + d[0], self.robot[1] + d[1])
                while n in self.boxes:
                    self.boxes.remove(n)
                    self.boxes.add((n[0]+d[0], n[1]))
                    n = (n[0]+d[0]*2, n[1])
        else: # d[0] == 0
            blockers = set()
            new_blockers = set()
            if n in self.boxes:
                new_blockers.add(n)
            if (n[0]-1,n[1]) in self.boxes:
                new_blockers.add((n[0]-1,n[1]))
            if debug:
                print(new_blockers)
            while new_blockers:
                next_blockers = set()
                for b in new_blockers:
                    if (b[0], b[1]+d[1]) in self.walls or (b[0]+1, b[1]+d[1]) in self.walls:
                        return
                    for o in [-1, 0, 1]:
                        if (b[0]+o, b[1]+d[1]) in self.boxes:
                            next_blockers.add((b[0]+o, b[1]+d[1]))
                blockers |= new_blockers
                new_blockers = next_blockers
            self.boxes -= blockers
            for b in blockers:
                self.boxes.add((b[0], b[1]+d[1]))
            self.robot = n

    def print(self):
        for y in range(self.Y):
            for x in range(self.X):
                if (x, y) in self.walls:
                    print('#', end='')
                elif (x, y) in self.boxes:
                    print('[', end='')
                elif (x, y) == self.robot:
                    print('\033[1;15m@\033[0m', end='')
                elif (x-1, y) in self.boxes:
                    print(']', end='')
                else:
                    print('.', end='')
            print()

    def solve(self):
        for y, line in enumerate(self.input):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls.add((x, y))
                elif c == 'O':
                    self.boxes.add((x, y))
                elif c == '@':
                    self.robot = (x, y)
            if line == '':
                break

        self.moves = ''.join(self.input[y+1:])
        self.X = max(x for x, _ in self.walls) + 1
        self.Y = max(y for _, y in self.walls) + 1

        for m in self.moves:
            self.move(m)
        return sum(x + y*100 for x, y in self.boxes)

    def solve2(self):
        for y, line in enumerate(self.input):
            for x, c in enumerate(line):
                if c == '#':
                    self.walls |= {(x*2, y), (x*2+1,y)}
                elif c == 'O':
                    self.boxes.add((x*2, y))
                elif c == '@':
                    self.robot = (x*2, y)
            if line == '':
                break

        self.moves = ''.join(self.input[y+1:])
        self.X = max(x for x, _ in self.walls) + 1
        self.Y = max(y for _, y in self.walls) + 1

        # self.print()
        for i, m in enumerate(self.moves):
            self.move2(m, i==-1)
            # if 373 <= i <= 375:
            #     print(f"Step {i}: \033[1;31m{m}\033[0m")
            #     self.print()
            #     time.sleep(0.5)
        # self.print()
        return sum(x + y*100 for x, y in self.boxes)

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
