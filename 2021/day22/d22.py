import re

class Problem:

    def __init__(self):
        self.cubes = {}
        self.instructions = []

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        for line in f.read().strip().split('\n'):
            m = re.match(r'(on|off) x=([0-9\-]+)..([0-9\-]+),y=([0-9\-]+)..([0-9\-]+),z=([0-9\-]+)..([0-9\-]+)', line)
            self.instructions.append([1 if m.group(1) == 'on' else 0] + [int(x) for x in m.groups()[1:]])


    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def solvePart1(self):
        for a in range(-50, 51):
            for b in range(-50, 51):
                for c in range(-50, 51):
                    self.cubes[(a, b, c)] = 0
        for instruction in self.instructions:
            if all((-50 <= instruction[i*2+1] <= 50) and (-50 <= instruction[i*2+2] <= 50) for i in range(3)):
                for a in range(instruction[1], instruction[2]+1):
                    for b in range(instruction[3], instruction[4]+1):
                        for c in range(instruction[5], instruction[6]+1):
                            self.cubes[(a, b, c)] = instruction[0]
        return sum(i[1] for i in self.cubes.items())

problem = Problem()
problem.solve()
