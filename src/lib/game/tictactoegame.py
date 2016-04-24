import lib


from lib.game.game import Game


class TicTacToeGame(Game):

    def __init__(self):
        super().__init__()
        self._lstAvailableChoice = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]


    @property
    def lstAvailableChoice(self):
        return self._lstAvailableChoice


    def is_all_in(self, lstExpect, lstNum):

        isAllIn = True

        for number in lstExpect:
            isNumberInList = number in lstNum

            if (not isNumberInList):
                isAllIn = False
                break

        return isAllIn


    def check_winner(self):

        for player in self._lstPlayer:

            if (self.is_all_in( [ 1, 2, 3 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 4, 5, 6 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 7, 8, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 1, 4, 7 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 2, 5, 8 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 3, 6, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 1, 5, 9 ], player.lstSelectedNum )):
                player.win()

            elif (self.is_all_in( [ 3, 5, 7 ], player.lstSelectedNum )):
                player.win()
