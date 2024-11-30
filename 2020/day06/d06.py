import string

f = open('d06.in', 'r')


def find_total_yes_or(groups):
    c = 0
    for group in groups:
        c += len(set(group.replace('\n', '')))
    return c


def find_total_yes_and(groups):
    c = 0
    for group in groups:
        s = set(string.ascii_lowercase)
        for person in group.split('\n'):
            s = s.intersection(set(person))
        c += len(s)
    return c


groups = f.read().strip().split('\n\n')
print("Puzzle 1: ", find_total_yes_or(groups))
print("Puzzle 2: ", find_total_yes_and(groups))
