f = open('d24.in', 'r')


def findCoordinates(tile):
    global moves
    x, y = 0, 0
    i = 0
    while i < len(tile):
        move = tile[i]
        i += 1
        if move in 'ns':
            move += tile[i]
            i += 1
        x, y = x + moves[move][0], y + moves[move][1]
    return (x,y)


def findBlackTiles(tiles):
    swap = {}
    for tile in tiles:
        coordinates = findCoordinates(tile)
        if coordinates not in swap:
            swap[coordinates] = 0
        swap[coordinates] = 1 - swap[coordinates]
    return list(swap.values()).count(1)


def findBlackTiles2(tiles):
    global moves
    swap = {}
    for tile in tiles:
        coordinates = findCoordinates(tile)
        if coordinates not in swap:
            swap[coordinates] = 0
        swap[coordinates] = 1 - swap[coordinates]
    blackTiles = set([coordinates for coordinates in swap if swap[coordinates]])
    deltaMoves = moves.values()
    for day in range(100):
        whiteTiles = set()
        for tile in blackTiles:
            for move in deltaMoves:
                x, y = tile[0] + move[0], tile[1] + move[1]
                if (x,y) not in blackTiles:
                    whiteTiles.add((x,y))
        flipBlack = set()
        flipWhite = set()
        for tile in blackTiles:
            countBlack = 0
            for move in deltaMoves:
                x, y = tile[0] + move[0], tile[1] + move[1]
                if (x,y) in blackTiles:
                    countBlack += 1
            if countBlack == 0 or countBlack > 2:
                flipBlack.add(tile)
        for tile in whiteTiles:
            countBlack = 0
            for move in deltaMoves:
                x, y = tile[0] + move[0], tile[1] + move[1]
                if (x,y) in blackTiles:
                    countBlack += 1
            if countBlack == 2:
                flipWhite.add(tile)
        blackTiles, whiteTiles = (blackTiles | flipWhite) - flipBlack, (whiteTiles | flipBlack) - flipWhite
    return len(blackTiles)


tiles = f.read().strip().split('\n')
moves = {'e': (2, 0), 'w': (-2, 0), 'ne': (1, 1), 'nw': (-1, 1), 'se': (1, -1), 'sw': (-1, -1)}
print("Puzzle 1: ", findBlackTiles(tiles))
print("Puzzle 2: ", findBlackTiles2(tiles))
