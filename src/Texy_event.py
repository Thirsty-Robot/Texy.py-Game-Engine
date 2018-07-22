from colorama import *

init(autoreset=True)

def alert(string):
	color = Fore.RED + string
	return color

def notification(string):
	color = Fore.YELLOW + string
	return color

def emphasis(string):
	color = Fore.YELLOW + Back.BLUE + string
	return color

def dim(string):
	color = Fore.DIM + string
	return color 