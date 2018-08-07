from texy import Texy_scene
import obj_player as op

player = op.player()

def run():
	player.talk()
	Texy_scene.move_scene('scene_2.py')

if (__name__ == '__main__'):
	run()