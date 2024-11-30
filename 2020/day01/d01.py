f = open('d01.in', 'r')


def findTwoEntriesProduct(lines, needed_sum, i, j):
    while i <= j:
        if lines[i] + lines[j] == needed_sum:
            return lines[i] * lines[j]
        elif lines[i] + lines[j] < needed_sum:
            i += 1
        else:
            j -= 1
    return -1


def findThreeEntriesProduct(lines, needed_sum, i, j):
    # At first, I thought I might have to look for 3 distinct elements.
    # However the extra complexity will be O(N) in addition to O(N).
    # But then I thought it would be OK because the test case should be
    # random and duplicated elements are rare and the question is even
    # not clear about if it is possible to take one element twice. Thus
    # I went with a classic set. Actually it is O(N^2) but could be
    # reduced to O(N) using double pointer as in the first part. But I
    # don't care because I'm already late. It's December 7th today.
    s = set(lines)
    for a in range(j-i):
        for b in range(a+1, j+1):
            c = needed_sum-lines[a]-lines[b]
            if c > 0 and c in s:
                return lines[a]*lines[b]*c
    return -1


lines = sorted(list(map(int, f.read().strip().split('\n'))))
print("Puzzle 1: ", findTwoEntriesProduct(lines, 2020, 0, len(lines)-1))
print("Puzzle 2: ", findThreeEntriesProduct(lines, 2020, 0, len(lines)-1))
