from collections import Counter

class Die:

    def __init__(self):
        self.current = 0
        self.rolls = 0

    def roll(self):
        self.current = (self.current % 100) + 1
        self.rolls += 1
        return self.current


class Problem:

    def __init__(self):
        self.players = [
            {'position': 0, 'score': 0},
            {'position': 0, 'score': 0},
        ]
        self.current_player = 0

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        for i, line in enumerate(f.read().strip().split('\n')):
            _, p = line.split(': ')
            self.players[i]['position'] = int(p) - 1
            self.players[i]['score'] = 0

    def solve(self):
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def solvePart1(self):
        self.readInput()
        die = Die()
        while True:
            next = die.roll() + die.roll() + die.roll()
            self.players[self.current_player]['position'] = (self.players[self.current_player]['position'] + next) % 10
            self.players[self.current_player]['score'] += self.players[self.current_player]['position'] + 1
            if self.players[self.current_player]['score'] >= 1000:
                break
            self.current_player = 1 - self.current_player
        return die.rolls * self.players[1 - self.current_player]['score']

    def getStateIndex(self):
        return (((((self.players[0]['position'] * 10)
                   + self.players[1]['position']) * 30)
                   + self.players[0]['score']) * 30
                   + self.players[1]['score']) * 2 + self.current_player

    def solvePart2(self):
        self.readInput()
        rolls = Counter((a+b+c) for a in (1,2,3) for b in (1,2,3) for c in (1,2,3))
        states = {}
        i = 0
        while True:
            stop = False
            i+=1
            for roll in rolls.items():
                self.players[self.current_player]['position'] = (self.players[self.current_player]['position'] + roll[0]) % 10
                self.players[self.current_player]['score'] += self.players[self.current_player]['position'] + 1
                if self.players[self.current_player]['score'] >= 21:
                    stop = True
                index = self.getStateIndex()
                states[index] = (states[index] if index in states else 1) * roll[1]
                self.players[self.current_player]['score'] -= (self.players[self.current_player]['position'] + 1)
                self.players[self.current_player]['position'] = (self.players[self.current_player]['position'] - roll[0]) % 10
            print(states.items())
            if stop or i == 2:
                break
            self.current_player = 1 - self.current_player
        wins = [0, 0]
        for item in states.items():
            score2 = (item[0]//2) % 30
            score1 = (item[0]//60) % 30
            wins[0 if score1 > score2 else 1] += item[1]
        print(wins)
        return max(wins)
problem = Problem()
problem.solve()
