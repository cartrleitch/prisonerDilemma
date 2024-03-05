#H = Help, I = Ignore, A = Attack
# 1. If both players attack, both players lose 5 points.
# 2. If both players ignore, both players gain 1 point.
# 3. If one player attacks and the other helps, the attacker gains 9 points and the defender loses 10 points.
# 4. If both players help, both players gain 8 points.
# 5. If one player ignores and the other attacks, the attacker gains 6 points and the defender loses 7 points.

import random

# strategy defintions
def titForTat(enemyBoard, round):
    if round != 0:
        if enemyBoard[round-1] == 'A':
            return 'A'
        else:
            return 'H'
    else:
        return 'H'

def violentIgnorer(enemyBoard, round):
    if round != 0:
        if enemyBoard[round-1] == 'A':
            return 'A'
        elif round == 10:
            return 'A'
        elif round > 1 and enemyBoard[round-1] == 'H' and enemyBoard[round-2] == 'H':
            return 'H'
        else:
            return 'I'
    else:
        return 'I'
    
def otherCheek(enemyBoard, round):
    return 'H'

def loco(enemyBoard, round):
    return 'A'

def randomChoice(enemyBoard, round):
    return random.choice(['A', 'H', 'I'])

def scaredyCat(enemyBoard, round):
    if round != 0:
        if enemyBoard[round-1] == 'A':
            return 'I'
        else:
            return 'H'
    else:
        return 'H'
    
def meanGuy(enemyBoard, round):
    if round != 0:
        if enemyBoard[round-1] == 'H':
            return 'H'
        else:
            return 'I'
    else:
        return 'A'
    
def greatIgnorer(enemyBoard, round):
    return 'I'


        
# play game function
def playGame(p1, p2, numRounds=50):
    p1Score = 0
    p2Score = 0
    p1Board = []
    p2Board = []

    # play game
    for round in range(numRounds):
        # each round player 1 board gets reads previous move of player 2, then responds
        p1Board.append(p1(p2Board, round))
        p2Board.append(p2(p1Board, round))

    print(f"Player 1: {p1Board}")
    print(f"Player 2: {p2Board}")

    # calculate scores
    for round in range(numRounds):
        if p1Board[round] == 'A' and p2Board[round] == 'A':
            p1Score -= 5
            p2Score -= 5
        elif p1Board[round] == 'A' and p2Board[round] == 'H':
            p1Score += 9
            p2Score -= 10
        elif p1Board[round] == 'H' and p2Board[round] == 'A':
            p1Score -= 10
            p2Score += 9
        elif p1Board[round] == 'H' and p2Board[round] == 'H':
            p1Score += 8
            p2Score += 8
        elif p1Board[round] == 'I' and p2Board[round] == 'I':
            p1Score += 1
            p2Score += 1
        elif p1Board[round] == 'I' and p2Board[round] == 'H':
            p1Score += 5
        elif p1Board[round] == 'H' and p2Board[round] == 'I':
            p2Score += 5
        elif p1Board[round] == 'I' and p2Board[round] == 'A':
            p1Score -= 7
            p2Score += 6
        elif p1Board[round] == 'A' and p2Board[round] == 'I':
            p1Score += 6
            p2Score -= 7
        else:
            print('Error')
    
    print(f"Player 1 score: {p1Score}")
    print(f"Player 2 score: {p2Score}")

    return [p1Score, p2Score]


# list of strategies:
# titForTat, violentIgnorer, otherCheek, loco, randomChoice, 
# scaredyCat, meanGuy, greatIgnorer
    
strategyList = [titForTat, violentIgnorer, otherCheek, loco, randomChoice, scaredyCat, meanGuy, greatIgnorer]
scores = []

# plays all strategies against each other and against itself
def playAllStrategies():
    gameNum = 0
    stratTotal = 0
    stratAvgs = []

    for strategy1 in strategyList:
        stratTotal = 0
        for strategy2 in strategyList:
            print(f"Playing {strategy1.__name__} vs {strategy2.__name__}")
            result = playGame(strategy1, strategy2)
            gameNum += 1
            stratTotal += result[0]
            scores.append(f"{gameNum}\n{strategy1.__name__} score: {result[0]}\n{strategy2.__name__} score: {result[1]}\n")
            print("\n\n")
        stratAvgs.append(f"{strategy1.__name__} Average: {stratTotal / len(strategyList)}")

    for i in scores:
        print(i)
    
    for i in stratAvgs:
        print(i)
    
#playGame(loco, loco)
playAllStrategies()