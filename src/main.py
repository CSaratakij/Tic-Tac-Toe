import actor
from actor import Actor

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class TicTacToeGame(Widget):

	isGameOver = False
	
	player = Actor("Player", False)
	enemy = Actor("Computer", True)
	
	lstAvailableChoice = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
	dictIndexToButtonName = { 1: "btn1", 2: "btn2", 3: "btn3", 4: "btn4", 5: "btn5", 6: "btn6", 7: "btn7", 8: "btn8", 9: "btn9" }

	player.start_first()
	
	
	def is_all_in(self, lstExpect, lstNum):
		
		isAllIn = True

		for number in lstExpect:
			isNumberInList = number in lstNum
			
			if (not isNumberInList):
				isAllIn = False
				break

		return isAllIn


	def check_winner(self, actor):

		if (self.is_all_in([ 1, 2, 3 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 4, 5, 6 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 7, 8, 9 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 1, 4, 7 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 2, 5, 8 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 3, 6, 9 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 1, 5, 9 ], actor.lstSelectedNum)):
			actor.win()
			
		elif (self.is_all_in([ 3, 5, 7 ], actor.lstSelectedNum)):
			actor.win()

							
	def set_all_button_disable(self, isDisable):
		
		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].disabled = isDisable
  

	def set_all_button_text(self, value):
		
		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].text = value
		
		
	def restart_game(self, btn):
		
		self.isGameOver = False
		self.player = Actor("Player", False)
		self.enemy = Actor("Enemy", True)
		self.lstAvailableChoice = list(self.dictIndexToButtonName.keys())
		
		self.player.start_first()
		
		self.set_all_button_text("")
		self.set_all_button_disable(False)


	def button_press(self, btn):
		
		if (not self.isGameOver and self.player.isTurn):
			
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
			self.lstAvailableChoice.remove(selectedNum)
			
			btn.text = "X"
			btn.disabled = True
			
			
			self.check_winner(self.player)
			self.check_winner(self.enemy)
			
			
			if (self.player.isWin or self.enemy.isWin or len(self.lstAvailableChoice) == 0):
				self.isGameOver = True


			self.player.isTurn = False
			self.enemy.isTurn = True


		if (not self.isGameOver and self.enemy.isTurn):
			selectedNum = self.enemy.random_pick(self.lstAvailableChoice)

			if (selectedNum > 0):
				self.enemy.lstSelectedNum.append(selectedNum)
				self.lstAvailableChoice.remove(selectedNum)
				
				self.ids[ self.dictIndexToButtonName[selectedNum] ].text = "O"
				self.ids[ self.dictIndexToButtonName[selectedNum] ].disabled = True
			
			
			self.check_winner(self.enemy)
			self.check_winner(self.player)
			
			
			if (self.player.isWin or self.enemy.isWin or len(self.lstAvailableChoice) == 0):
				self.isGameOver = True
			
			
			self.enemy.isTurn = False
			self.player.isTurn = True


	def button_release(self, btn):
		
		if (self.isGameOver):
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
		
		return TicTacToeGame()


if __name__ == "__main__":
	TicTacToeApp().run()
