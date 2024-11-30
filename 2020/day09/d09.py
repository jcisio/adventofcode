f = open('d09.in', 'r')


def testPosition(numbers, p):
    if p < 25:
        return True
    for i in range(p-25, p-1):
        for j in range(i+1, p):
            if numbers[i] != numbers[j] and numbers[i] + numbers[j] == numbers[p]:
                return True
    return False


def findOddNumber(numbers):
    p = 25
    while True:
        if not testPosition(numbers, p):
            return numbers[p]
        p += 1


def findOddSeries(numbers, total):
    accumulated_sum = [0]*(len(numbers)+1)
    for i in range(len(numbers)):
        accumulated_sum[i+1] = numbers[i] + accumulated_sum[i]
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            if accumulated_sum[j+1] - accumulated_sum[i] == total:
                return min(numbers[i:j+1]) + max(numbers[i:j+1])


numbers = list(map(int, f.read().strip().split('\n')))
print("Puzzle 1: ", findOddNumber(numbers))
print("Puzzle 2: ", findOddSeries(numbers, findOddNumber(numbers)))
