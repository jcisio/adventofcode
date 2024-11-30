
class Problem:

    def __init__(self):
        self.map = []
        self.m = 0
        self.n = 0

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        self.map = [list(line) for line in f.read().strip().split('\n')]
        self.m = len(self.map)
        self.n = len(self.map[0])

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def move(self):
        c = 0
        moves = []
        for m in range(self.m):
            for n in range(self.n):
                if self.map[m][n] == '>' and self.map[m][(n+1) % self.n] == '.':
                    moves.append((m,n))
        c += len(moves)
        for move in moves:
            self.map[move[0]][move[1]] = '.'
            self.map[move[0]][(move[1]+1) % self.n] = '>'
        moves = []
        for m in range(self.m):
            for n in range(self.n):
                if self.map[m][n] == 'v' and self.map[(m+1) % self.m][n] == '.':
                    moves.append((m, n))
        c += len(moves)
        for move in moves:
            self.map[move[0]][move[1]] = '.'
            self.map[(move[0] + 1) % self.m][move[1]] = 'v'
        return c

    def print(self):
        for line in self.map:
            print(''.join(line))

    def solvePart1(self):
        n = 1
        while self.move():
            n += 1
        return n


problem = Problem()
problem.solve()
