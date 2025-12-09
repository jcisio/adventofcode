"""
Advent Of Code
--- Day 9: Movie Theater ---
https://adventofcode.com/2025/day/9
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

from itertools import combinations
import time


class Problem:
    def __init__(self, input):
        self.input = [tuple(map(int, line.split(','))) for line in input]

    def get_size(self, i, j, check=False):
        (x1, y1), (x2, y2) = self.input[i], self.input[j]
        if check:
            for x3,y3 in self.input:
                if (x3-x1)*(x3-x2) < 0 and (y3-y1)*(y3-y2) < 0:
                    return 0
        return (abs(x1-x2)+1)*(abs(y1-y2)+1)

    def solve(self):
        return max(self.get_size(i, j) for i,j in combinations(range(len(self.input)), 2))

    def draw(self):
        import matplotlib.pyplot as plt
        from matplotlib.patches import Polygon

        # Create figure and axis
        fig, ax = plt.subplots(figsize=(10, 10))

        # Draw the polygon
        polygon = Polygon(self.input, fill=False, edgecolor='blue', linewidth=2)
        ax.add_patch(polygon)

        # Draw lines connecting consecutive points
        for i in range(len(self.input)):
            x1, y1 = self.input[i]
            x2, y2 = self.input[(i + 1) % len(self.input)]
            ax.plot([x1, x2], [y1, y2], 'b-', linewidth=1.5)

        ax.grid(True, alpha=0.3)

        # Set axis limits with some padding
        padding = 1
        xs = [x for x, y in self.input]
        ys = [y for x, y in self.input]
        ax.set_xlim(min(xs) - padding, max(xs) + padding)
        ax.set_ylim(min(ys) - padding, max(ys) + padding)

        # Save to PDF
        plt.savefig('polygon.pdf', format='pdf', bbox_inches='tight')
        plt.close()

    def find_max(self, i, j):
        return max(self.get_size(x,y,True) for x,y in combinations(range(i,j+1), 2))

    def solve2(self):
        # self.draw()
        # if len(self.input) < 100: # test case
        #     return self.find_max(0, len(self.input)-1)

        m = max([i for i in range(len(self.input)-1)], key=lambda j:abs(self.input[j][0]-self.input[j+1][0])) + 1
        return max(self.find_max(0, m), self.find_max(m+1, len(self.input)-1))

in1 = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
# assert(Solver(in1).solve(1) == 50)
# assert(Solver(in1).solve(2) == 24)
parts = [1, 2]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10s\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
