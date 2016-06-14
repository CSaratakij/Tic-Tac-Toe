from kivy.app import App
from kivy.uix.screenmanager import Screen


class MainMenuView(Screen):

    def btnSinglePlayer_release(self):
        self.manager.current = "singleplayer-gameplay"


    def btnMultiplayerOption_release(self):
        self.manager.current = "multiplayer-option"


    def btnExit_release(self):
        App.get_running_app().stop()
