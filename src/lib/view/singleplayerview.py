from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from lib.game.tictactoegame import TicTacToeGame
from lib.game.player import Player
from lib.game.bot import Bot


class SinglePlayerView(Screen):

	dictIndexToButtonName = {
								1: "btn1",
								2: "btn2",
								3: "btn3",
								4: "btn4",
								5: "btn5",
								6: "btn6",
								7: "btn7",
								8: "btn8",
								9: "btn9"
							}

	soundClick = SoundLoader.load("assets/menu_selection_click.ogg")

	game = TicTacToeGame()
	player = Player("Player", "X")
	enemy = Bot("Computer", "O")

	game.add_player( [player, enemy] )

	player.start_first()
	game.start()


	def set_all_button_disable(self, isDisable):

		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].disabled = isDisable


	def set_all_button_text(self, value):

		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].text = value


	def restart_game(self):

		self.game = TicTacToeGame()
		self.player = Player("Player", "X")
		self.enemy = Bot("Computer", "O")

		self.game.add_player([ self.player, self.enemy ])

		self.player.start_first()
		self.game.start()

		self.reset_button()


	def reset_button(self):
		self.set_all_button_text("")
		self.set_all_button_disable(False)


	def btnRestart_press(self, btn):
		self.restart_game()
		self.reset_button()


	def btnMainMenu_press(self, btn):
		self.restart_game()
		self.manager.current = "mainmenu"


	def btnGame_press(self, btn):

		if (self.soundClick):
			self.soundClick.play()


		if (not self.game.isOver):

			if (self.player.isTurn):

				selectedNum = 0
				totalButton = len(self.dictIndexToButtonName)

				for index in range(1, totalButton + 1):
					if (btn == self.ids[ self.dictIndexToButtonName[index] ]):
						selectedNum = index
						break


				self.player.pick(selectedNum)
				self.game.remove_choice(selectedNum)

				btn.text = self.player.marking
				btn.disabled = True


				self.game.check_winner()


				if (self.game.isHasWinner or len(self.game.lstAvailableChoice) == 0):
					self.game.over()


				self.game.next_turn()


			if (self.enemy.isTurn):

				selectedNum = self.enemy.get_random_from(self.game.lstAvailableChoice)

				if (selectedNum > 0):

					self.enemy.pick(selectedNum)
					self.game.remove_choice(selectedNum)

					self.ids[ self.dictIndexToButtonName[selectedNum] ].text = self.enemy.marking
					self.ids[ self.dictIndexToButtonName[selectedNum] ].disabled = True


				self.game.check_winner()


				if (self.game.isHasWinner or len(self.game.lstAvailableChoice) == 0):
					self.game.over()


				self.game.next_turn()


	def btnGame_release(self, btn):

		if (self.game.isOver):

			self.set_all_button_disable(True)

			boxLayout = BoxLayout(orientation = "vertical")

			dlgGameOver = Popup(title = "GameOver",
					size_hint = (None, None),
					size = (400, 400),
					auto_dismiss = False)


			lblWinner = Label(text = "Winner : ")
			lblWinner.font_size = 24

			btnRestart = Button(text = "Restart")
			btnRestart.bind(on_press = self.btnRestart_press)
			btnRestart.bind(on_release = dlgGameOver.dismiss)


			btnMainMenu = Button(text = "MainMenu")
			btnMainMenu.bind(on_press = self.btnMainMenu_press)
			btnMainMenu.bind(on_release = dlgGameOver.dismiss)


			if (self.player.isWin):
				lblWinner.text += self.player.name

			elif (self.enemy.isWin):
				lblWinner.text += self.enemy.name

			else:
				lblWinner.text = "Tie"


			boxLayout.add_widget(lblWinner)
			boxLayout.add_widget(btnRestart)
			boxLayout.add_widget(btnMainMenu)

			dlgGameOver.content = boxLayout
			dlgGameOver.open()
