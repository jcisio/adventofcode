f = open('d10.in', 'r')


def findDifference(adapters):
    diff = [0]*4
    current = 0
    for adapter in adapters:
        diff[adapter-current] += 1
        current = adapter
    diff[3] += 1 # built-in adapter
    return diff[1] * diff[3]


def findTotalChoices(adapters):
    adapters = [0] + adapters + [adapters[-1]+3]
    L = len(adapters)
    c = [1]*L
    for i in range(L-2, -1, -1):
        j = i + 1
        while j+1 < L and adapters[j+1] - adapters[i] <= 3:
            j += 1
        c[i] = sum(c[i+1:j+1])
    return c[0]


adapters = sorted(list(map(int, f.read().strip().split('\n'))))
print("Puzzle 1: ", findDifference(adapters))
print("Puzzle 2: ", findTotalChoices(adapters))
