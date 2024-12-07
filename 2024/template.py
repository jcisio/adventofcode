import time


example = True
parts = [1, 2]

class Problem:
    def __init__(self, input):
        self.input = input

    def solve(self):
        return 0

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
    length = time.time() - start
    print(f"Part {part}: \033[1;31m{result:<8d}\033[0m ({length*1000:.0f} ms)")
