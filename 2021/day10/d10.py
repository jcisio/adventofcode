f = open(__file__[:-3] + '.in', 'r')


chunks = '()[]{}<>'

def get_current_trunk(line):
    global chunks
    current_chunk = []
    corrupted = None
    for i in range(len(line)):
        index = chunks.index(line[i])
        if index % 2 == 0:
            current_chunk.append(line[i])
        elif chunks.index(current_chunk[-1]) == index - 1:
            current_chunk.pop()
        else:
            corrupted = line[i]
            break
    return current_chunk, corrupted


def calculateCheckerScore(line):
    global chunks
    scores = [3, 57, 1197, 25137]
    _, corrupted = get_current_trunk(line)
    return scores[chunks.index(corrupted)//2] if corrupted else 0


def calculateCorrectorScore(line):
    global chunks
    scores = [1, 2, 3, 4]
    current_trunk, corrupted = get_current_trunk(line)
    score = 0
    if not corrupted:
        while current_trunk:
            score = score*5 + scores[chunks.index(current_trunk.pop())//2]
    return score


def solvePart1(lines):
    return sum(calculateCheckerScore(line) for line in lines)


def solvePart2(lines):
    scores = [calculateCorrectorScore(line) for line in lines]
    scores = sorted([score for score in scores if score])
    return scores[len(scores)//2]


lines = f.read().strip().split('\n')
print("Puzzle 1: ", solvePart1(lines))
print("Puzzle 2: ", solvePart2(lines))
