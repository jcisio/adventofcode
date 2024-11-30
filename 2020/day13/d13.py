import math

f = open('d13.in', 'r')


def findFirstBus(start_time, bus):
    delta = [id*math.ceil(start_time/id) - start_time for k, id in bus]
    index = delta.index(min(delta))
    return bus[index][1] * delta[index]


def findMatchedTime(bus):
    current_mutiplier = bus[0][1]
    current_offset = 0
    for i in range(1, len(bus)):
        for j in range(bus[i][1]):
            rem = -bus[i][0] % bus[i][1]
            if (current_offset + current_mutiplier*j) % bus[i][1] == rem:
                current_offset += current_mutiplier * j
                current_mutiplier *= bus[i][1]
                break
    return current_offset

start_time = int(f.readline())
bus = [(k,int(id)) for k, id in enumerate(f.readline().strip().split(',')) if id != 'x']
print("Puzzle 1: ", findFirstBus(start_time, bus))
print("Puzzle 2: ", findMatchedTime(bus))
