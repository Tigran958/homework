############1##########
print("Kilometer_coverter: \n")
def kilometer_coverter(lenght):
	kilo_to_mile = 0.621371
	if lenght * kilo_to_mile > 1:
		return str(lenght) + ' kilometers equal ' + str(lenght * kilo_to_mile) + ' miles'
	return str(lenght) + ' kilometer equals ' + str(lenght * kilo_to_mile) + ' mile'
	
first_input = int(input("How many kilometers  do you want to convert? "))
print(kilometer_coverter(first_input))
print("\n")

###########2###########
print("Temperature converter \n")
def celsius_farenheit(temp):
	cel_to_far = 33.8
	return str(temp) + ' celsius temerature is ' + str(temp * cel_to_far) + ' grade in farenheit'

temp_input = int(input('Enter the grade in celsius '))
print(celsius_farenheit(temp_input))
print("\n")

###########3############
print("Task 4 \n")
def random_number():
	import random
	hidden_number = random.randint(1,2)
	return hidden_number

print_text = "Let's toss a coin, heads or tails, you know. \n Enter a question and see the result. \n enter FINISH to end:"
print(print_text)

def quest_answ():
	quest = input("Ask something ")
	heads_tails = ""
	while quest != "FINISH":
		number = random_number()
		heads_tails = input('Heads/Tails? ')

		if quest == "":
			quest = input("Ask something ")

		elif number == 2:
			result_coin = "Heads"
			print("Heads!")
			if result_coin == heads_tails:
				print("Just, do it!")
			else:
				print("Maybe, another time?")	
			quest = input("Another question: ")
			
		else:
			result_coin = "Teils"
			print("Teils!")
			if result_coin == heads_tails:
				print("Just, do it!")
			else:
				print("Maybe, another time?")
			quest = input("Another question: ")
			
quest_answ()
print("\n")

###########4############
print("Task 5 - word_counter\n")

def word_counter():
	sentence = input("Enter a sentence ")
	count = 0
	for i in sentence:
		if i == " ":
			count += 1
	print(count)

word_counter()
print("\n")
#########5#######
print('Task 6 - Letter checker \n')

def letter_checker(word):
	letters = 'qwertyuiopasdfghjklzxcvbnm'
	for i in word:
		
		if i not in letters:
			return i, ' is not an English letter!'
		continue
	return 'All letters are from English alphabet!'

print(letter_checker(input("Tell something!!! ")))


