import os
import pickle

## FUNCTIONS

def display_title_bar():
	os.system('cls')
	print("\t\t\t\t****************************************************")
	print("\t\t\t\t***  Recommendator - Give me vidya suggestions!  ***")
	print("\t\t\t\t****************************************************")

def get_user_choice():
	print("\n\n[1] Recommend me a new game.\n")
	print("[2] See the current list of games.\n")
	print("[q] Quit.")
	return input("\n\nWhat would you like to do? ")

def show_games():
	print("\nHere are the games I've been suggested so far.")
	for game in gamelist:
		print(game.title())

def get_new_game():
	new_game = input("\nWhat's the game's name?: ")
	if new_game in gamelist:
		print("\n%s is already on the list. Thank you though." % new_game.title())
	else:
		gamelist.append(new_game)
		print("\nI'll play %s when I get the chance!" % new_game.title())

def load_games():
	try:
		file_object = open('games.pydata','rb')
		games = pickle.load(file_object)
		file_object.close()
		return games
	except Exception as e:
		print(e)
		return []

def quit():
	try:
		file_object = open('games.pydata', 'wb')
		pickle.dump(gamelist, file_object)
		file_object.close()
		
		print("\nThanks, I will remember these games.")
	except Exception as e:
		print("\nThanks, though I won't remember these games.")
		print(e)

## MAIN PROGRAM
gamelist = load_games()
choice = ''
display_title_bar()
while choice != 'q':
	choice = get_user_choice()
	display_title_bar()
	if choice == '2':
		show_games()
	elif choice == '1':
		get_new_game()
	elif choice == 'q':
		quit()
		print("Goodbye.")
	else:
		print("I did not understand your input.\n")
