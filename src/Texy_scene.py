import uuid
import os
import inspect

def move_room(room_to_move):
	os.system('python '+room_to_move)
	sys.exit()

def destroy_object(object_uuid):
	objects_on_room.remove(object_uuid)
