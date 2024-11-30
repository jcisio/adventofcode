f = open('d06.in', 'r')


def countLanternFish(lanternfish, days):
    for i in range(days):
        new_lanternfish = {}
        for fish in lanternfish:
            if fish == 0:
                new_lanternfish[6] = (0 if 6 not in new_lanternfish else new_lanternfish[6]) + lanternfish[0]
                new_lanternfish[8] = lanternfish[0]
            else:
                new_lanternfish[fish - 1] = (
                    0 if fish - 1 not in new_lanternfish else new_lanternfish[fish - 1]) + lanternfish[fish]
        lanternfish = new_lanternfish
    return sum(lanternfish.values())


lanternfish = {}
for f in map(int, f.read().strip().split(',')):
    if f in lanternfish:
        lanternfish[f] += 1
    else:
        lanternfish[f] = 1

print("Puzzle 1: ", countLanternFish(lanternfish, 80))
print("Puzzle 2: ", countLanternFish(lanternfish, 256))
