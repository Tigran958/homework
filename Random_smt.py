import random 
import time
list_game = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

list_game_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
list_game_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0
# Functions
def func_1(list_game):
	print(list_game[0:3], "\n", list_game[3:6], "\n", list_game[6:], "\n", sep = '')

def func_input(list_game):
	a = "X"
	b = "O"
	y = True
	
	while y:
		try:
			ind_g = input("Enter x index \n")
			if not ind_g.isdigit():
				raise ValueError

			ind_g = int(ind_g) - 1
			
			while list_game[ind_g].isalpha():

				ind_g = int(input("Enter x index \n")) - 1

			list_game[ind_g] = a
			list_game_2[ind_g] = True
			
			y = False

		except ValueError:
			print("It's not a number!")		
		except IndexError:
			print("Wrong index!")
	

def func_comp(list_game):
	a = "X"
	b = "O"
	print("Now is my turn \n")
	time.sleep(0.2)
	comp = random.randint(0,8)

	while list_game[comp] == a or list_game[comp] == b:
		comp = random.randint(0,8)

	list_game[comp] = b
	list_game_3[comp] = True

# Conditions_function
def check_func(list_game_2,list_game_3):
	if (list_game_2[0] and list_game_2[1] and list_game_2[2]) or \
		(list_game_2[3] and list_game_2[4] and list_game_2[5]) or \
		(list_game_2[6] and list_game_2[7] and list_game_2[8]) or \
		(list_game_2[0] and list_game_2[3] and list_game_2[6]) or \
		(list_game_2[1] and list_game_2[4] and list_game_2[7]) or \
		(list_game_2[2] and list_game_2[5] and list_game_2[8]) or \
		(list_game_2[0] and list_game_2[4] and list_game_2[8]) or \
		(list_game_2[6] and list_game_2[4] and list_game_2[2]):
		check = 'win'
	elif (list_game_3[0] and list_game_3[1] and list_game_3[2]) or \
		(list_game_3[3] and list_game_3[4] and list_game_3[5]) or \
		(list_game_3[6] and list_game_3[7] and list_game_3[8]) or \
		(list_game_3[0] and list_game_3[3] and list_game_3[6]) or \
		(list_game_3[1] and list_game_3[4] and list_game_3[7]) or \
		(list_game_3[2] and list_game_3[5] and list_game_3[8]) or \
		(list_game_3[0] and list_game_3[4] and list_game_3[8]) or \
		(list_game_3[6] and list_game_3[4] and list_game_3[2]):
		check = 'lose'
	else:
		check = True
	return check


# Actions
func_1(list_game)
for i in range(3):
	
	func_input(list_game)
	func_1(list_game)
	func_comp(list_game)
	func_1(list_game)


while True:
	if check_func(list_game_2, list_game_3) == 'win':
		print(check_func(list_game_2, list_game_3))
		print("You won!!!")
		break
	elif check_func(list_game_2, list_game_3) == 'lose':
		print(check_func(list_game_2, list_game_3))
		print("You lost this game")
		break
	func_input(list_game)
	
	if count >= 1:
		if check_func(list_game_2, list_game_3) == 'win':
			print(check_func(list_game_2, list_game_3))
			print("You won!!!")
			break
		else:
			print("Game over!!!")
			break
	func_comp(list_game)
	func_1(list_game)
	count += 1
