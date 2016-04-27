import kivy
import lib


from kivy.app import App
from kivy.uix.screenmanager import Screen


class MainMenuView(Screen):

    def btnPlay_release(self, btn):
        self.manager.current = "singleplayer"


    def btnExit_release(self, btn):
        App.get_running_app().stop()
