import kivy


from kivy.uix.screenmanager import Screen


class MultiplayerOptionView(Screen):

    def btnLocalMultiplayer_release(self, btn):
        self.manager.current = "localmultiplayer-gameplay"


    def btnOnlineMultiplayer_release(self, btn):
        pass


    def btnBack_release(self, btn):
        self.manager.current = "mainmenu"