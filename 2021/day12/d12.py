
class Problem:

    def __init__(self):
        # List of caves, True = big cave, False = small cave
        self.caves = {}
        # List of edge between two caves.
        self.edges = {}

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        for line in f.read().strip().split('\n'):
            s, e = line.split('-')
            self.edges[(s, e)] = 1
            self.edges[(e, s)] = 1
            if s not in self.caves:
                self.caves[s] = (s == s.upper())
            if e not in self.caves:
                self.caves[e] = (e == e.upper())

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def findNextCave(self, current_path, revisit=False):
        found = []
        for cave in self.caves:
            if (current_path[-1], cave) not in self.edges:
                continue
            if cave == 'end':
                found.append(current_path + [cave])
            elif (cave not in current_path) or self.caves[cave] or (revisit and cave != 'start'):
                can_revisit = (cave not in current_path or self.caves[cave]) and revisit
                found += self.findNextCave(current_path + [cave], can_revisit)
        return found

    def solvePart1(self):
        return len(self.findNextCave(['start']))

    def solvePart2(self):
        return len(self.findNextCave(['start'], True))


problem = Problem()
problem.solve()
