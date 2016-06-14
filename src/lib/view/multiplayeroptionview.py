from kivy.uix.screenmanager import Screen


class MultiplayerOptionView(Screen):

    def btnLocalMultiplayer_release(self):
        self.manager.current = "localmultiplayer-gameplay"


    def btnOnlineMultiplayer_release(self):
        pass


    def btnBack_release(self):
        self.manager.current = "mainmenu"
