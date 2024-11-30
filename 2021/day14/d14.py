from collections import Counter


class Problem:

    def __init__(self):
        self.template = ''
        self.rules = {}
        self.pairs = {}

    def readInput(self):
        f = open(__file__[:-3] + '.in', 'r')
        lines = f.read().strip().split('\n')
        self.template = lines[0]
        for rule in lines[2:]:
            source, destination = rule.split(' -> ')
            self.rules[source] = destination

    def solve(self):
        self.readInput()
        print("Puzzle 1: ", self.solvePart1())
        print("Puzzle 2: ", self.solvePart2())

    def doStep(self, template):
        new_template = template[0]
        for i in range(len(template) - 1):
            if template[i:i+2] in self.rules:
                new_template += self.rules[template[i:i+2]]
            new_template += template[i+1]
        return new_template

    def doStepFaster(self, pairs):
        new_pairs = {}
        for k, v in pairs.items():
            pair1 = k[0] + self.rules[k]
            pair2 = self.rules[k] + k[1]
            new_pairs[pair1] = (new_pairs[pair1] if pair1 in new_pairs else 0) + v
            new_pairs[pair2] = (new_pairs[pair2] if pair2 in new_pairs else 0) + v
        return new_pairs

    def solvePart1(self):
        template = self.template
        for i in range(10):
            template = self.doStep(template)
            counter = Counter(template)
        counter = Counter(template)
        return max(counter.values()) - min(counter.values())

    def solvePart2(self):
        counter = Counter(self.template[i:i+2] for i in range(len(self.template) - 1))
        pairs = {k: v for k, v in counter.items()}
        for i in range(40):
            pairs = self.doStepFaster(pairs)
        counter = {self.template[0]: 1, self.template[-1]: 1}
        for k, v in pairs.items():
            counter[k[0]] = (counter[k[0]] if k[0] in counter else 0) + v
            counter[k[1]] = (counter[k[1]] if k[1] in counter else 0) + v
        return (max(counter.values()) - min(counter.values()))//2

problem = Problem()
problem.solve()
