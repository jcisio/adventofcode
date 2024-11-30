f = open('d15.in', 'r')


def findRound(rounds, n):
    current = len(rounds)
    while current < n:
        rounds.reverse()
        try:
            i = rounds.index(rounds[0], 1)
        except ValueError:
            i = 0
        rounds.reverse()
        rounds.append(i)
        current += 1
    return rounds[-1]


def findRoundOptimize(rounds, n):
    # Use array instead of dict to optimize performance. It's 25% faster in
    # CPython (15s vs 20s) and 66% faster in Pypy (3.3s vs 10s).
    positions = [-1] * (n + max(rounds))
    for i in range(len(rounds)-1):
        positions[rounds[i]] = i
    last_number = rounds[-1]
    current = len(rounds)
    while current < n:
#        print(current, last_number, rounds)
        if positions[last_number] != -1:
            new_last_number = current - positions[last_number] - 1
        else:
            new_last_number = 0
        positions[last_number] = current - 1
        last_number = new_last_number
        current += 1
        rounds.append(last_number)
    return last_number


rounds = list(map(int, f.read().strip().split(',')))
print("Puzzle 1: ", findRound(rounds, 2020))
print("Puzzle 2: ", findRoundOptimize(rounds, 30000000))
