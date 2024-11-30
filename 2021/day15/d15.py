
class Problem:

    def __init__(self):
        self.dist = {}
        self.prev = {}
        self.edges = {}
        self.vertices = set()
        self.risk = []


    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        self.risk = []
        for line in f.read().strip().split('\n'):
            self.risk.append(list(map(int, list(line))))
        N = len(self.risk)
        for i in range(N):
            for j in range(N):
                self.vertices.add((i, j))
                self.dist[(i, j)] = N*N*10
        self.dist[(0, 0)] = 0


    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())

    def update(self, u, v):
        if self.dist[u] + self.risk[u[0]][u[1]] < self.dist[v]:
            self.dist[v] = self.dist[u] + self.risk[u[0]][u[1]]
            self.prev[v] = u

    def solvePart1(self):
        while self.vertices:
            m = min(self.vertices, key=lambda v: self.dist[v])
            self.vertices.remove(m)
            # For each neighbor of m
            for n in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if (m[0]+n[0], m[1]+n[1]) in self.vertices:
                    self.update(m, (m[0]+n[0], m[1]+n[1]))
        # Reconstruct path and calculate distance
        N = len(self.risk)
        target = (N-1, N-1)
        S = 0
        while True:
            S += self.risk[target[0]][target[1]]
            target = self.prev[target]
            if target == (0, 0):
                break
        return S


problem = Problem()
problem.solve()
