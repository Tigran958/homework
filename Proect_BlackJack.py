import random

card_list = [2,3,4,5,6,7,8,9,10,11,12,13,14]

dict_card = {}
card_type = ["spades", "hearts", "diamonds", "clubs"]
key_list = []
for i in card_type:
	for j in card_list:
		if j < 11:
			key = str(j) + " of " + i 
			dict_card[key] = j 
			key_list.append(key)
		elif j == 11:	
			key = "T" + " of " + i
			dict_card[key] = j
			key_list.append(key)
		elif j == 12:	
			key = "J" + " of " + i
			dict_card[key] = j 
			key_list.append(key)
		elif j == 13:	
			key = "Q" + " of " + i
			dict_card[key] = j 
			key_list.append(key)
		elif j == 14:	
			key = "K" + " of " + i
			dict_card[key] = j
			key_list.append(key) 		
			
player = 0
comp = 0

def card_gen(nlist, ndict):
	random.shuffle(nlist)
	value = ndict[nlist[1]]
	print(nlist[1])
	nlist.remove(nlist[1])
	return value

def card_gen_c(nlist, ndict):
	random.shuffle(nlist)
	value = ndict[nlist[1]]
	nlist.remove(nlist[1])
	return value


print("Lets play Black Jack")
for i in range(2):
	player += card_gen(key_list,dict_card) 
	comp += card_gen_c(key_list,dict_card) 

print(F"Your start point is {player}" )


while True:
	if player > 21:
		print(f"You lost\nyour score is {player}")
		break
	elif player == 21:
		print("BLACK JACK!!! You Won!!!")
	
	elif player < 21:
		user_input = input("Do you want more? yes/no ")
		while user_input == "yes":
			player += card_gen(key_list,dict_card)
			print(player)
			if player == 21:
				print("BLACK JACK!!! You Won!!!")
				break
			elif player > 21:
				print(f"You lost\nyour score is {player}")
				break
			user_input = input("Do you want more? yes/no ")
		if player > 21:
			break	
	else:
		print(f"You Won!\nyour score is {player}, and the computer's {comp}")
	if comp > 21:
		print(f"You Won!\nyour score is {player}, and the computer's {comp}")
		break
	elif comp < 17:
		while comp < 17:
			comp += card_gen_c(key_list,dict_card)
		if comp > 21:
			print(F"You Won!\nyour score is {player}, and the computer's {comp}")	
		elif comp == 21:
			
			print(F"You Lost!\nyour score is {player}, and the computer's {comp}")
		else:
			if player > comp:
				print(F"You Won!\nyour score is {player}, and the computer's {comp}")
				break
			else:
				print(f"You Lost!\nyour score is {player}, and the computer's {comp}")
				break
	else:
		if player > comp:
			print(F"You Won!\nyour score is {player}, and the computer's {comp}")
			break
		elif player == comp:
			print("This time won friendship!!!")	
		else:
			print(comp," comp")
			print(f"You Lost!\nyour score is {player}, and the computer's {comp}")
			break
	break


