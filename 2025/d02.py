"""
Advent Of Code
--- Day 2: Gift Shop ---
https://adventofcode.com/2025/day/2
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
        self.input = ''.join(input)

    def is_invalid(id):
        sid = str(id)
        return sid[:len(sid)//2] == sid[len(sid)//2:]

    def is_invalid2(id):
        sid = str(id)
        for i in range(1, len(sid)//2 + 1):
            if sid[:i]*(len(sid)//i) == sid:
                return True
        return sid[:len(sid)//2] == sid[len(sid)//2:]

    def solve(self, checker=is_invalid):
        s = 0
        for ids in self.input.split(','):
            id_from, id_to = map(int, ids.split('-'))
            for id in range(id_from, id_to + 1):
                if checker(id):
                    s += id
        return s

    def solve2(self):
        return self.solve(checker=Problem.is_invalid2)

in1 = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""
# assert(Solver(in1).solve(1) == 1227775554)
assert(Solver(in1).solve(2) == 4174379265)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
