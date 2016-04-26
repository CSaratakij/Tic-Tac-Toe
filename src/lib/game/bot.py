import random
import lib


from lib.game.player import Player


class Bot(Player):

    def __init__(self, name, marking):
        super().__init__(name, marking)


    def get_random_from(self, lstNum):

        randomNum = 0

        if (len(lstNum) > 0):
            index = random.randint(0, len(lstNum) - 1)
            randomNum = lstNum[index]

        return randomNum