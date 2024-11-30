f = open('d14.in', 'r')


def applyInstruction(memory, mask, name, value):
    address = name[4:-1]
    data = 0
    multiplier = 1
    for bitmask in mask[-1::-1]:
        bit = value % 2
        value = value // 2
        if bitmask != 'X':
            bit = int(bitmask)
        data = data + bit*multiplier
        multiplier *= 2
    memory[address] = data
    return memory


def applyInstruction2(memory, mask, name, value):
    address = int(name[4:-1])
    masked_address = []
    masked_positions = []
    i = 0
    for bitmask in mask[-1::-1]:
        bit = address % 2
        address = address // 2
        masked_address.append(bit if bitmask == '0' else 1 if bitmask == '1' else 'X')
        if bitmask == 'X':
            masked_positions.append(i)
        i += 1
    masked_address.reverse()
    for i in range(2**len(masked_positions)):
        dynamic_address = i
        for j in range(len(masked_positions)):
            masked_address[-1-masked_positions[j]] = dynamic_address % 2
            dynamic_address //= 2
        address = 0
        for bit in masked_address:
            address = address * 2 + bit
        memory[address] = value

    return memory


def findSum(instructions, callable):
    memory = {}
    for name, value in instructions:
        if name == 'mask':
            mask = value
        else:
            memory = callable(memory, mask, name, int(value))
    return sum(memory.values())


instructions = [line.split(' = ') for line in f.read().strip().split('\n')]
print("Puzzle 1: ", findSum(instructions, applyInstruction))
print("Puzzle 1: ", findSum(instructions, applyInstruction2))
