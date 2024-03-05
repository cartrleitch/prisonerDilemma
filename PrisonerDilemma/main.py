import pDilemmaMain as pdm
from pDilemmaStrats import *

strategyList = [violentIgnorer, titForTat, otherCheek, loco, randomChoice, scaredyCat, meanGuy, greatIgnorer, steadfastFriend]

#pdm.playAllStrategies(strategyList)
pdm.playAllStrategiesMultiple(strategyList, 200)