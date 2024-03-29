import random

# list of strategies:
# titForTat, violentIgnorer, otherCheek, loco, randomChoice, 
# scaredyCat, meanGuy, greatIgnorer, steadfastFriend

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

def steadfastFriend(enemyBoard, round):
    if round != 0:
        if round > 1 and enemyBoard[round-1] == 'A' and enemyBoard[round-2] == 'A':
            return 'A'
        else:
            return 'H'
    else:
        return 'H'

def forgivingSteadfastFriend(enemyBoard, round):
    if round != 0:
        if round > 1 and enemyBoard[round-1] == 'A' and enemyBoard[round-2] == 'A':
            if random.randint(1, 10) == 1:
                return 'H'
            else:
                return 'A'
        else:
            return 'H'
    else:
        return 'H'
    
def lazyFriend(enemyBoard, round):
    if round != 0:
        if round > 1 and enemyBoard[round-1] == 'A' and enemyBoard[round-2] == 'A':
            return 'I'
        elif round > 2 and enemyBoard[round-1] == 'A' and enemyBoard[round-2] == 'A' and enemyBoard[round-3] == 'A':
            return 'A'
        else:
            return 'H'
    else:
        return 'H'
    
def selfishFriend(enemyBoard, round):
    if round != 0:
        if enemyBoard[round-1] == 'H':
            return 'H'
        else:
            return 'I'
    else:
        return 'H'