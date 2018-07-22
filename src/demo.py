import Texy

# Create object player
class Player:
	# Declare variables that object is going to use
	def __init__(self):
		self.hp = 100
		self.inventory = []
		self.output = ['hello there, nice to see you', 'I love no one']

	# Update function
	def dialog(self):
		dialog_1 = tx_di.multiple_dialog(self.output)

class Enemy:
	#Declare initial variables
	def __init__(self):
		self.hp = 100
		self.inventory = []
		self.damage = 100
	
	#Die
	def die(self):
		if (hp <= 0):
			tx_map.destroy_object(self.uuid)

def run():
	player_object = Player()
	Enemy_object = Enemy()

	print (player_object)
	print (Enemy_object)

if __name__ == '__main__':
	# Initialize objects
	Texy.run(run)
	