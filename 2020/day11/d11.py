f = open('d11.in', 'r')


def countOccupied(seats, j, i):
    nearby = [(-1,-1), (-1,1), (1,-1), (1,1), (0,1), (0,-1), (1,0), (-1,0)]
    return sum([1 if seats[j + y][i + x]=='#' else 0 for (x, y) in nearby])


def countOccupied2(seats, j, i):
    nearby = [(-1,-1), (-1,1), (1,-1), (1,1), (0,1), (0,-1), (1,0), (-1,0)]
    L = len(seats)
    N = len(seats[0])
    c = 0
    for (y, x) in nearby:
        delta = 1
        while 0 < j+y*delta < L and  0 < i + x*delta < N:
            if seats[j+y*delta][i+x*delta] == '.':
                delta += 1
                continue
            elif seats[j+y*delta][i+x*delta] == '#':
                c += 1
            break
    return c

def stabilizeSeats(seats, functionCount, tolerant):
    L = len(seats)
    N = len(seats[0])
    extended_seats = ['.'*(N+2)]
    for n in range(L):
        extended_seats.append('.' + seats[n] + '.')
    extended_seats.append('.'*(N+2))
    while True:
        changed = False
        new_seats = ['.'*(N+2)]*(L+2)
        for j in range(L):
            for i in range(N):
                if extended_seats[j+1][i+1] == '.':
                    continue
                c = functionCount(extended_seats, j+1, i+1)
                if extended_seats[j+1][i+1] == '#' and c >= tolerant:
                    new_seat = 'L'
                    changed = True
                elif extended_seats[j+1][i+1] == 'L' and c == 0:
                    new_seat = '#'
                    changed = True
                else:
                    new_seat = extended_seats[j+1][i+1]
                new_seats[j+1] = new_seats[j+1][:i+1] + new_seat + new_seats[j+1][i+2:]

        if not changed:
            break
        extended_seats = new_seats
    return sum([1 if extended_seats[j+1][i+1] == '#' else 0 for i in range(N) for j in range(L)])


seats = list(f.read().strip().split('\n'))
print("Puzzle 1: ", stabilizeSeats(seats, countOccupied, 4))
print("Puzzle 2: ", stabilizeSeats(seats, countOccupied2, 5))
