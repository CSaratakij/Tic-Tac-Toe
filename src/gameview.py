import game
import kivy


from game import TicTacToeGame
from game import Player
from game import Bot


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class SinglePlayerView(Widget):

	dictIndexToButtonName = { 1: "btn1", 2: "btn2", 3: "btn3", 4: "btn4", 5: "btn5", 6: "btn6", 7: "btn7", 8: "btn8", 9: "btn9" }
	
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
		
		
	def restart_game(self, btn):
		
		self.game = TicTacToeGame()
		self.player = Player("Player", "X")
		self.enemy = Bot("Enemy", "O")
		
		self.game.add_player([ self.player, self.enemy ])
		
		self.player.start_first()
		self.game.start()
		
		self.set_all_button_text("")
		self.set_all_button_disable(False)


	def button_press(self, btn):
		
		if (not self.game.isOver and self.player.isTurn):
			
			selectedNum = 0
		
			if (btn == self.ids[ self.dictIndexToButtonName[1] ]):
				selectedNum = 1
		
			elif (btn == self.ids[ self.dictIndexToButtonName[2] ]):
				selectedNum = 2
			
			elif (btn == self.ids[ self.dictIndexToButtonName[3] ]):
				selectedNum = 3
		
			elif (btn == self.ids[ self.dictIndexToButtonName[4] ]):
				selectedNum = 4
		
			elif (btn == self.ids[ self.dictIndexToButtonName[5] ]):
				selectedNum = 5
		
			elif (btn == self.ids[ self.dictIndexToButtonName[6] ]):
				selectedNum = 6
		
			elif (btn == self.ids[ self.dictIndexToButtonName[7] ]):
				selectedNum = 7
		
			elif (btn == self.ids[ self.dictIndexToButtonName[8] ]):
				selectedNum = 8
		
			elif (btn == self.ids[ self.dictIndexToButtonName[9] ]):
				selectedNum = 9


			self.player.lstSelectedNum.append(selectedNum)
			self.game.lstAvailableChoice.remove(selectedNum)
			
			btn.text = self.player.marking
			btn.disabled = True
			
			
			self.game.check_winner()
			
			
			if (self.player.isWin or self.enemy.isWin or len(self.game.lstAvailableChoice) == 0):
				self.game.over()


			self.player.isTurn = False
			self.enemy.isTurn = True


		if (not self.game.isOver and self.enemy.isTurn):
			selectedNum = self.enemy.random_pick(self.game.lstAvailableChoice)

			if (selectedNum > 0):
				self.enemy.lstSelectedNum.append(selectedNum)
				self.game.lstAvailableChoice.remove(selectedNum)
				
				self.ids[ self.dictIndexToButtonName[selectedNum] ].text = self.enemy.marking
				self.ids[ self.dictIndexToButtonName[selectedNum] ].disabled = True
			
			
			self.game.check_winner()
			
			
			if (self.player.isWin or self.enemy.isWin or len(self.game.lstAvailableChoice) == 0):
				self.game.over()
			
			
			self.enemy.isTurn = False
			self.player.isTurn = True


	def button_release(self, btn):
		
		if (self.game.isOver):
			
			self.set_all_button_disable(True)
			
			boxLayout = BoxLayout(orientation = "vertical")
			
			dlgGameOver = Popup(title = "GameOver",
					size_hint = (None, None),
					size = (400, 400),
					auto_dismiss = False)


			lblWinner = Label(text = "Winner is : ")

			btnRestart = Button(text = "Restart")
			btnRestart.bind(on_press = self.restart_game)
			btnRestart.bind(on_release = dlgGameOver.dismiss)
			
			
			btnExit = Button(text = "Exit")
			btnExit.bind(on_release = App.get_running_app().stop)
			
			
			if (self.player.isWin):
				lblWinner.text += "Player."
				
			elif (self.enemy.isWin):
				lblWinner.text += "Computer."
				
			else:
				lblWinner.text = "This game is Tie."

			
			boxLayout.add_widget(lblWinner)
			boxLayout.add_widget(btnRestart)
			boxLayout.add_widget(btnExit)
			
			dlgGameOver.content = boxLayout
			dlgGameOver.open()
			