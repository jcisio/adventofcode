"""
Advent Of Code
--- Day 25: Code Chronicle ---
https://adventofcode.com/2024/day/25
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
        self.locks = []
        self.keys = []
        for i in range(len(input)//8+1):
            if input[i*8][0] == '#':
                self.locks.append([sum(1 for r in range(5) if input[i*8+r+1][j] == '#') for j in range(5)])
            else:
                self.keys.append([sum(1 for r in range(5) if input[i*8+r+1][j] == '#') for j in range(5)])

    def fits(self, lock, key):
        return all(lock[i] + key[i] <= 5 for i in range(5))

    def solve(self):
        return sum(sum(1 for k in self.keys if self.fits(l, k)) for l in self.locks)

    def solve2(self):
        return 0

in1 = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""
assert(Solver(in1).solve(1) == 3)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
