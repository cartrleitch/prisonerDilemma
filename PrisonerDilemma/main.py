import pDilemmaMain as pdm
from pDilemmaStrats import *

strategyList = [violentIgnorer, titForTat, otherCheek, loco, 
                randomChoice, scaredyCat, meanGuy, greatIgnorer, 
                steadfastFriend, forgivingSteadfastFriend, lazyFriend,
                selfishFriend]

#pdm.playGame(otherCheek, titForTat, printResults=True)
#pdm.playAllStrategies(strategyList)
pdm.playAllStrategiesMultiple(strategyList, 200)