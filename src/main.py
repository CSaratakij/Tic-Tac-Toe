import kivy
import lib

kivy.require("1.9.1")


from kivy.app import App
from kivy.config import Config


from lib.view.singleplayerview import SinglePlayerView


class TicTacToeApp(App):

	title = "Tic-Tac-Toe"
	icon = "assets/icon.ico"


	def init_config(self):
		Config.set("graphics", "fullscreen", 0)
		Config.set("graphics", "resizable", 0)
		Config.set("graphics", "height", 600)
		Config.set("graphics", "width", 600)
		Config.set("kivy", "exit_on_escape", 0)
		Config.write()


	def build(self):
		self.init_config()
		return SinglePlayerView()


if __name__ == "__main__":
	TicTacToeApp().run()
