import random
import os
import sys
import keyboard

def dice_roll_array(array):
	choice = random.choice(array)
	return choice

def dice_roll_number():
	roll = random.randint(1, 6)
	return roll

def add_object_to_inventory(object_name, inventory, object_to_add):
	inventory.append(object_to_add)
	print ("%s has received %s and has been added to inventory" % (object_name, object_to_add))
	return inventory

def irandom (min, max):
	return random.randint(min, max)	

def encounter(bool_encounter, object_to_encounter):
	if (bool_encounter):
		print ("You've encounter "+object_to_encounter)

	else:
		return False
		
def exit_game():
	sys.exit()