class Player:

    def __init__(self, name, marking):
        self._name = name
        self._marking = marking
        self._isWin = False
        self._isTurn = False
        self._lstSelectedNum = []


    @property
    def name(self):
        return self._name

    @property
    def marking(self):
        return self._marking

    @property
    def isWin(self):
        return self._isWin

    @property
    def isTurn(self):
        return self._isTurn

    @property
    def lstSelectedNum(self):
        return self._lstSelectedNum


    @marking.setter
    def marking(self, value):
        self._marking = value

    @isTurn.setter
    def isTurn(self, value):
        self._isTurn = value

    
    def pick(self, value):
        self._lstSelectedNum.append(value)


    def start_first(self):
        self._isTurn = True


    def win(self):
        self._isWin = True


    def lose(self):
        self._isWin = False
