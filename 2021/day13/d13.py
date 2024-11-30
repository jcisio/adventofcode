
class Problem:

    def __init__(self):
        self.dots = {}
        self.instructions = []

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        first_half = True
        for line in f.read().strip().split('\n'):
            if not line:
                first_half = False
            elif first_half:
                a, b = line.split(',')
                self.dots[(int(a), int(b))] = True
            else:
                self.instructions.append((line[11], int(line[13:])))

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def fold(self, instruction):
        i = instruction[1]
        for k in list(self.dots):
            if instruction[0] == 'y':
                if k[1] == i:
                    del(self.dots[k])
                elif k[1] > i:
                    del(self.dots[k])
                    self.dots[(k[0], i*2 - k[1])] = True
            else:
                if k[0] == i:
                    del(self.dots[k])
                elif k[0] > i:
                    del(self.dots[k])
                    self.dots[(i*2 - k[0], k[1])] = True

    def solvePart1(self):
        dots = self.dots.copy()
        self.fold(self.instructions[0])
        result = len(self.dots)
        self.dots = dots
        return result

    def solvePart2(self):
        for instruction in self.instructions:
            self.fold(instruction)
        width = max(self.dots, key=lambda x: x[0])[0] + 1
        height = max(self.dots, key=lambda x: x[1])[1] + 1
        result = '\n'
        for y in range(height):
            for x in range(width):
                result += '#' if (x, y) in self.dots else ' '
            result += '\n'
        return result

problem = Problem()
problem.solve()
