from collections import Counter

f = open('d08.in', 'r')


def solvePart1(data):
    return sum(sum(1 if len(digit) in [2,3,4,7] else 0 for digit in item[1].split()) for item in data)


def decodeDigits(mapping, digits):
    number = 0
    segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for digit in digits:
        realDigit = ''.join(sorted([mapping[d] for d in digit]))
        number = number*10 + segments.index(realDigit)
    return number


def decodeItem(item):
    hist = Counter(item[0])
    digits = item[0].split()
    mapping = {}
    digit1 = [digit for digit in digits if len(digit) == 2][0]
    digit4 = [digit for digit in digits if len(digit) == 4][0]
    print(hist.items())
    mapping['a'] = [segment for segment in 'abcdefg' if hist[segment]==8 and segment not in digit1][0]
    mapping['b'] = [segment for segment in 'abcdefg' if hist[segment]==6][0]
    mapping['c'] = [segment for segment in 'abcdefg' if hist[segment]==8 and segment in digit1][0]
    mapping['d'] = [segment for segment in 'abcdefg' if hist[segment]==7 and segment in digit4][0]
    mapping['e'] = [segment for segment in 'abcdefg' if hist[segment]==4][0]
    mapping['f'] = [segment for segment in 'abcdefg' if hist[segment]==9][0]
    mapping['g'] = [segment for segment in 'abcdefg' if hist[segment]==7 and segment not in digit4][0]
    mapping = {v: k for k, v in mapping.items()}
    return decodeDigits(mapping, item[1].split())


def solvePart2(data):
    return sum(decodeItem(item) for item in data)
#['aecgdbf badcg fbcage gdabce be gaedb bced dfeag adbfgc abe', 'gedbacf be bdfcga bedfgca']

data = [line.split(' | ') for line in f.read().strip().split('\n')]
print("Puzzle 1: ", solvePart1(data))
print("Puzzle 2: ", solvePart2(data))
