import sys

f = open('d22.in', 'r')

max_game = 1

def calculateScore(cards):
    return sum([cards[i]*(len(cards)-i) for i in range(len(cards))])


def playGame(player1, player2):
    while player1 and player2:
        if (player1[0] > player2[0]):
            player1 = player1[1:] + [player1[0], player2[0]]
            player2 = player2[1:]
        else:
            player2 = player2[1:] + [player2[0], player1[0]]
            player1 = player1[1:]
    return calculateScore(player1 if player1 else player2)


def playRecursiveCombat(player1, player2, game):
    print('New game', game, player1, player2, file=sys.stderr)
    if game > 1 and max(player1) > max(player2):
        return 1
    states = set()
    round = 0
    while player1 and player2:
        round += 1
        state = ','.join(map(str, player1)) + ':' + ','.join(map(str, player2))
        if state in states:
            winner = 1
        elif player1[0] < len(player1) and player2[0] < len(player2):
            global max_game
            max_game += 1
            print('Round', round, 'game', game, 'play sub-rounds', file=sys.stderr)
            winner = playRecursiveCombat(player1[1:player1[0]+1], player2[1:player2[0]+1], max_game)
        else:
            winner = 2 if player1[0] < player2[0] else 1
        states.add(state)
        if winner == 1:
            player1 = player1[1:] + [player1[0], player2[0]]
            player2 = player2[1:]
        else:
            player2 = player2[1:] + [player2[0], player1[0]]
            player1 = player1[1:]
        print('Round', round, 'game', game, 'winner', winner, player1, player2, file=sys.stderr)
    winner = 1 if player1 else 2
    if game == 1:
        return player1 if winner == 1 else player2
    return winner


def playGame2(player1, player2):
    return calculateScore(playRecursiveCombat(player1, player2, 1))


lines = f.read().strip().split('\n')
cards = (len(lines) - 3)//2
player1 = list(map(int, lines[1:cards+1]))
player2 = list(map(int, lines[cards+3:]))
print("Puzzle 1: ", playGame(player1, player2))
# It will take quite a few minutes...
print("Puzzle 2: ", playGame2(player1, player2))
