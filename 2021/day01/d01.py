f = open(__file__[:-3] + '.in', 'r')


def findMeasurementIncreases(lines, window_size = 1):
    return sum(1 if lines[i] < lines[i+window_size] else 0 for i in range(len(lines)-window_size))


lines = list(map(int, f.read().strip().split('\n')))
print("Puzzle 1: ", findMeasurementIncreases(lines))
print("Puzzle 2: ", findMeasurementIncreases(lines, 3))
