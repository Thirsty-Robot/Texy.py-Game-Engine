from colorama import *

init(autoreset=True)

def text(string):
	color = Fore.WHITE + string
	return color

def alert(string):
	color = Fore.RED + string
	return color

def notification(string):
	color = Fore.YELLOW + string
	return color

def emphasis(string):
	color = Fore.YELLOW + Back.BLUE + string
	return color

def empasis2 (string):
	color = Style.BRIGHT + string
	return color

def dim(string):
	color = Style.DIM + string
	return color 