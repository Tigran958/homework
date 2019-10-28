list_1 = ["Oh yeah, I'll tell you somethin'", "I think you'll understand", "When I say that somethin'", "I want to hold your hand", "I want to hold your hand", "I want to hold your hand"]

while True:
	try:
		a = int(input("Tell me the line ")) - 1
		print(list_1[a])
		break
	except IndexError:
		print("try again ")
	except ValueError:
		print("Enter number ")
	except:
		print("again try again")