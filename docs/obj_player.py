from texy import Texy_dialogue

class player():
	def __init__(self):
		self.hp = 100;
		self.dialogues = ['Hello everyone how are you', 'Hello everyone, how are you again']

	def hp_down(self, damage):
		self.hp-=damage
		return self.hp

	def talk(self):
		Texy_dialogue.multiple_dialog(self.dialogues)