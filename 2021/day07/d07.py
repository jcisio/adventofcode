import statistics

f = open('d07.in', 'r')


def calculateFuel(positions, destination):
    return sum([abs(x - destination)*(abs(x - destination)+1)//2 for x in positions])


def findMinimumFuel(positions):
    median = int(statistics.median(positions))
    return sum([abs(x - median) for x in positions])


def findMinimumFuel2(positions):
    fuels = {position:-1 for position in range(min(positions)-1, max(positions)+2)}
    median = int(statistics.median(positions))
    fuels[median] = calculateFuel(positions, median)
    destination = median
    while True:
        if fuels[destination-1] == -1:
            fuels[destination-1] = calculateFuel(positions, destination-1)
        if fuels[destination+1] == -1:
            fuels[destination+1] = calculateFuel(positions, destination+1)
        if min(fuels[destination-1], fuels[destination+1]) > fuels[destination]:
            return fuels[destination]
        if fuels[destination-1] < fuels[destination+1]:
            destination -= 1
        else:
            destination += 1


positions = list(map(int, f.read().strip().split(',')))
print("Puzzle 1: ", findMinimumFuel(positions))
print("Puzzle 2: ", findMinimumFuel2(positions))
