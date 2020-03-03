import random


numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10","V", "D", "K", "T"]
mast = ["Heart", "Diamond", "Spade", "Clubs"]
deck = []

for i in mast:
	for j in numbers:
		a = i + " " + j		
		deck.append(a)
print(deck)



def comp_choice(deck):	
	dealer_hand = []
	random.shuffle(deck)
	random.shuffle(deck)

	dealer_hand.append(deck.pop())	
	dealer_hand.append(deck.pop())

	summ = 0
	while summ < 17:

		# print(dealer_hand)	
		
		for i in dealer_hand:
			a = i.split(" ")
			if a[1].isdigit():
				i = int(a[1])
				# print("i = ", i)
			elif a[1] == "V" or a[1] == "D" or a[1] == "K":
				i = 10
				# print("i = ", 10)
			elif a[1] == "T":
				i = 11
				# print("i = ", 11)

			summ += i
			# print("sum = ", summ)
			if summ == 21:
				print("sum = ", summ)
				print("dealer win")
				return "you win"
				break
			elif summ > 21:
				print("sum = ", summ)
				print("dealer loose")
				return "you loose"
				break
			elif summ >= 17 and summ < 21:				
				print("dealers final hand SUM is ", summ)
				return summ
				break
			elif summ < 17:				
				dealer_hand.append(deck.pop())




def user_choice(deck):
	user_hand = []
	random.shuffle(deck)
	random.shuffle(deck)
	# print(deck)

	user_hand.append(deck.pop())	
	user_hand.append(deck.pop())

	# print(user_hand)
	summ = 0
	for i in user_hand:		
		a = i.split(" ")
		if a[1].isdigit():
			i = int(a[1])			
		elif a[1] == "V" or a[1] == "D" or a[1] == "K":
			i = 10		
		elif a[1] == "T":
			i = 11
		
		summ += i
	print("sum of your card is: ", summ)

	while True:
		answer = input("do you want another card? type y or n: ")
		if answer == "y":			
			user_hand.append(deck.pop())			
			for i in user_hand:
				a = i.split(" ")
				if a[1].isdigit():
					i = int(a[1])			
				elif a[1] == "V" or a[1] == "D" or a[1] == "K":
					i = 10		
				elif a[1] == "T":
					i = 11
			summ += i
			if summ == 21:
				print("sum = ", summ)
				print("you win")
				return "you win"
				break
			elif summ > 21:
				print("sum = ", summ)
				print("you loose")
				return "you loose"
				break
			else:
				print("sum of your card is: ", summ)

		elif answer == "n":
			print("your final hand SUM is ", summ)
			return summ
			break





while True:
	
	fin = user_choice(deck)
	if fin == "you win":
		break
	elif fin == "you lose":
		break
	else:
		user = fin

	
	fin = comp_choice(deck)
	if fin == "you win":
		break
	elif fin == "you lose":
		break
	else:
		dealer = fin

	if user > dealer:
		print("YOU WIN !!!")
		break
	if user == dealer:
		print("NO ONE")
		break
	else:
		print("YOU LOSE")
		break