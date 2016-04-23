import gameview
import kivy

kivy.require("1.9.1")


from gameview import SinglePlayerView


from kivy.app import App
from kivy.config import Config


class TicTacToeApp(App):

	title = "Tic-Tac-Toe"
	icon = "icon.ico"
	
	def build(self):
	
		Config.set("graphics", "fullscreen", 0)
		Config.set("graphics", "resizable", 0)
		Config.set("graphics", "height", 600)
		Config.set("graphics", "width", 600)
		Config.set("kivy", "exit_on_escape", 0)
		Config.write()
		
		return SinglePlayerView()


if __name__ == "__main__":
	TicTacToeApp().run()
