f = open('d25.in', 'r')


def transformSubject(subject, loop_count = 0, result = -1):
    loop = 0
    value = 1
    while True:
        loop += 1
        value = (value * subject) % 20201227
        if loop == loop_count or value == result:
            break
    return loop, value


def findEncryptionKey(pubkey1, pubkey2):
    privkey1, value = transformSubject(7, result= pubkey1)
    return transformSubject(pubkey2, loop_count=privkey1)[1]


pubkey1, pubkey2 = map(int, f.read().strip().split('\n'))
print("Puzzle 1: ", findEncryptionKey(pubkey1, pubkey2))
