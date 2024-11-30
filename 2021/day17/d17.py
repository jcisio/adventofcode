import re


class Problem:

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        m = re.search(r'x=([0-9\-]+)\.\.([0-9\-]+), y=([0-9\-]+)\.\.([0-9\-]+)', f.read().strip())
        self.target = list(map(int, m.groups()))

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def findVx(self):
        for vx in range(1, self.target[1] + 1):
            x = 0
            vx_init = vx
            while x < self.target[0] and vx > 0:
                x += vx
                if self.target[0] <= x <= self.target[1]:
                    break
                vx = vx - 1
            if vx > 0:
                break
        return vx_init

    def solvePart1(self):
        vx = self.findVx()
        vy = -1 - self.target[2]
        return vy*(vy+1)//2

    def testVelocity(self, vx, vy):
        x, y = 0, 0
        while ((vx > 0 and x < self.target[1]) or (vx == 0 and self.target[0] <= x <= self.target[1])) and (y >= self.target[2]):
            x += vx
            y += vy
            if self.target[0] <= x <= self.target[1] and self.target[2] <= y <= self.target[3]:
                return 1
            vx = max(vx - 1, 0)
            vy = vy - 1
        return 0

    def solvePart2(self):
        vx = self.findVx()
        vy = -1 - self.target[2]
        min_vy = self.target[2]
        max_vx = self.target[1]
        return sum(sum(self.testVelocity(vx, y) for y in range(min_vy, vy+1)) for vx in range(vx, max_vx+1))


problem = Problem()
problem.solve()
