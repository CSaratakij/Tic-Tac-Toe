class Game:

    def __init__(self):
        self._isStart = False
        self._isOver = False
        self._lstPlayer = []


    @property
    def isStart(self):
        return self._isStart

    @property
    def isOver(self):
        return self._isOver

    @property
    def lstPlayer(self):
        return self._lstPlayer


    def check_winner(self):
        raise NotImplementedError("Please implement this method.")


    def add_player(self, lstPlayer):
        
        for player in lstPlayer:
            self._lstPlayer.append(player)


    def start(self):
        self._isStart = True


    def over(self):
        self._isOver = True
