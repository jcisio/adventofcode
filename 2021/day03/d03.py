f = open('d03.in', 'r')


def findPowerConsumption(lines):
    gamma, epsilon = 0, 0
    for i in range(len(lines[0])):
        nbits = sum([int(line[i]) for line in lines])
        major_bit = 1 if nbits > len(lines)/2 else 0
        gamma = gamma*2 + major_bit
        epsilon = epsilon*2 + (1 - major_bit)
    return gamma * epsilon

def filterByBitCriteira(lines, bit):
    i = 0
    elements = lines.copy()
    while len(elements) > 1:
        nbits = sum([int(element[i]) for element in elements])
        if nbits < len(elements)/2:
            major_bit = 1 - bit
        else:
            major_bit = bit
        major_bit = str(major_bit)
        elements = [element for element in elements if element[i] == major_bit]
        i += 1
    return int(elements[0], 2)

def findLifeSupportRating(lines):
    return filterByBitCriteira(lines, 1) * filterByBitCriteira(lines, 0)

lines = f.read().strip().split('\n')
print("Puzzle 1: ", findPowerConsumption(lines))
print("Puzzle 2: ", findLifeSupportRating(lines))
