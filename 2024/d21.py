"""
Advent Of Code
--- Day 21: Keypad Conundrum ---
https://adventofcode.com/2024/day/21
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

import time


class Problem:
    def __init__(self, input):
        self.input = input[:5]
        self.D = '^>v<'
        self.K1 = {
            '7': '.84.',
            '8': '.957',
            '9': '..68',
            '4': '751.',
            '5': '8624',
            '6': '9.35',
            '1': '42..',
            '2': '5301',
            '3': '6.A2',
            '0': '2A..',
            'A': '3..0'
        }
        self.K2 = {
            '^': '.Av.',
            'A': '..>^',
            '<': '.v..',
            'v': '^>.<',
            '>': 'A..v'
        }

    def find_shortest(self, A, B, keypad):
        q = [(0, A, '')]
        result = []
        while q:
            d, p, seq = q.pop(0)
            if p == B:
                result.append(seq)
                continue
            if result and d > len(result[0]):
                continue
            trials = [2,3,0,1]
            if seq:
                # Favor the same key
                prev = self.D.index(seq[-1])
                trials.remove(prev)
                trials.insert(0, prev)
            for k in trials:
                if keypad[p][k] != '.':
                    q.append((d+1, keypad[p][k], seq+self.D[k]))
        return max(result, key=self.score)

    def score(self, seq):
        s = sum(1 for i in range(len(seq)-1) if seq[i]==seq[i+1])
        # print(seq, s)
        return s

    def encode(self, seq, keypad):
        res = []
        p = 'A'
        for s in seq:
            res.append(self.find_shortest(p, s, keypad))
            res.append('A')
            p = s
        return ''.join(res)

    def decode(self, seq, keypad):
        res = []
        p = 'A'
        for s in seq:
            if s == 'A':
                res.append(p)
            else:
                p = keypad[p][self.D.index(s)]
        return ''.join(res)

    def find_complexity(self, seq):
        s1 = self.encode(seq, self.K1)
        # s1 = s1.replace('^^<<A', '<<^^A')
        s2 = self.encode(s1, self.K2)
        # s2 = s2.replace('^^<<A', '<<^^A')
        s3 = self.encode(s2, self.K2)
        # print(s1)
        # print(s2)
        # print(s3)
        # print(seq, len(s3))
        return int(seq[:-1]) * len(s3)

    def debug(self, s3):
        s2 = self.decode(s3, self.K2)
        s1 = self.decode(s2, self.K2)
        print(f"{s1}\n{s2}\n{s3}")

    def solve(self):
        # print(self.find_complexity("179A"))
        # print(self.find_shortest("A", "1", self.K1))
        # self.debug("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")
        return sum(self.find_complexity(seq) for seq in self.input)
        # return 0

    def solve2(self):
        return 0

in1 = """
029A
980A
179A
456A
379A

<^<A^^A>>AvvvA
v<<A>^Av<A>>^A<AA>AvAA^Av<AAA^>A
v<A<AA>>^AvA<^A>Av<A<A>>^AvAA<^A>Av<<A>>^AAvA^Av<A^>AA<A>Av<A<A>>^AAA<Av>A^A


^<<A^^A>>AvvvA
<Av<AA>>^A<AA>AvAA^A<vAAA>^A
<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
"""

assert(Problem([]).find_complexity("029A")//29 == 68)
assert(Problem([]).find_complexity("980A")//980 == 60)
assert(Problem([]).find_complexity("179A")//179 == 68)
assert(Problem([]).find_complexity("456A")//456 == 64)
assert(Problem([]).find_complexity("379A")//379 == 64)
# assert(Solver(in1).solve(1) == 126384)
# assert(Solver(in1).solve(2) == 0)
parts = [1]

### No change after this ###

solver = Solver('.test')
for part in parts:
    start = time.time()
    result = solver.solve(part)
    print("Part %d: \033[1;31m%-10d\033[0m (%.0f ms)" % (part, result, (time.time() - start)*1000))
