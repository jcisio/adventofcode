f = open('d08.in', 'r')


def readProgram(f):
    program = []
    for line in f.read().strip().split('\n'):
        op, num = line.split()
        program.append([op, int(num)])
    return program


def runProgram(program):
    executed = set()
    acc, i = 0, 0
    while i < len(program):
        if i in executed:
            return (False, acc)
        executed.add(i)
        if program[i][0] == 'nop':
            i += 1
        elif program[i][0] == 'acc':
            acc += program[i][1]
            i += 1
        else:
            i += program[i][1]
    return (True, acc)


def runProgramCorrectly(program):
    for i in range(len(program)):
        if program[i][0] == 'acc':
            continue
        else:
            op = program[i][0]
            program[i][0] = 'jmp' if op == 'nop' else 'nop'
            ok, acc = runProgram(program)
            if ok:
                return acc
            program[i][0] = op


program = readProgram(f)
print("Puzzle 1: ", runProgram(program)[1])
print("Puzzle 2: ", runProgramCorrectly(program))
