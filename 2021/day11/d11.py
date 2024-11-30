import math
import time
import copy


f = open(__file__[:-3] + '.in', 'r')


class Octopus:

    positions = []
    N = 0
    L = 0

    def __init__(self, positions):
        self.positions = positions
        self.L = len(self.positions)
        self.N = round(math.sqrt(self.L))


    def formatPosition(self, i, highlights):
        if self.positions[i] == 0:
            color = '35'
        elif i in highlights:
            color = '31'
        else:
            color = '0'
        return '\033[' + color + 'm{0:>3}\033[0m'


    def print(self, status='', highlights=[], delay=3, delete=True):
        time.sleep(delay/2)
        print(status + '...')
        for i in range(self.N):
            print(''.join(map(lambda x: self.formatPosition(x, highlights).format(self.positions[x]), range(i*self.N, (i+1)*self.N))))
        if delete:
            print('\033[' + str(self.N+2) + 'F')
        time.sleep(delay/2)


    def flash(self, i):
        self.positions[i] = 0
        neighbors = [i-self.N-1, i-self.N, i-self.N+1, i-1, i+1, i+self.N-1, i+self.N, i+self.N+1]
        neighbors = list(filter(lambda x: 0<=x<self.L and abs((x%self.N)-(i%self.N))<=1 and self.positions[x] > 0, neighbors))
        #octopus.print('Do flash {}'.format(i), neighbors)
        for x in neighbors:
            self.positions[x] += 1
        #octopus.print('Done'.format(i))


    def oneStep(self):
        self.positions = [x+1 for x in self.positions]
        #octopus.print('Next step')
        total = 0
        while True:
            flashed = False
            for i in range(self.L):
                if self.positions[i] > 9:
                    total += 1
                    self.flash(i)
                    flashed = True
            if not flashed:
                break
        #octopus.print('End step')
        return total


def solvePart1(octopus: Octopus):
    x = sum(octopus.oneStep() for i in range(100))
    #octopus.print(delete=False, delay=0)
    return x


def solvePart2(octopus: Octopus):
    step = 0
    while True:
        step += 1
        octopus.oneStep()
        if sum(octopus.positions) == 0:
            break
    return step


octopus = Octopus(list(map(int, ''.join(f.read().strip().split('\n')))))
print("Puzzle 1: ", solvePart1(copy.copy(octopus)))
print("Puzzle 2: ", solvePart2(octopus))
