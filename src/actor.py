import random

class Actor:

    def __init__(self, name, isBot, marking):
        self.name = name
        self.isBot = isBot
        self.lstSelectedNum = []
        self.marking = marking
        self.isWin = False
        self.isTurn = False


    def start_first(self):
        self.isTurn = True
        

    def random_pick(self, lstNum):
        
        randomNum = 0
        
        if (self.isBot and len(lstNum) > 0):
            index = random.randint(0, len(lstNum) - 1)
            randomNum = lstNum[index]
        
        return randomNum


    def win(self):
        self.isWin = True