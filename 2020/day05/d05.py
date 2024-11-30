import re

f = open('d05.in', 'r')


def calculate_seat_id(seat):
    id = 0
    for c in seat:
        id = id*2 + (0 if c in 'FL' else 1)
    return id


def find_highest_seat_id(seats):
    return max([calculate_seat_id(seat) for seat in seats])


def find_missing_seat_id(seats):
    ids = sorted([calculate_seat_id(seat) for seat in seats])
    for i in range(len(ids)):
        if ids[i] + 1 < ids[i+1]:
            return ids[i] + 1


seats = list(f.read().strip().split('\n'))
print("Puzzle 1: ", find_highest_seat_id(seats))
print("Puzzle 2: ", find_missing_seat_id(seats))
