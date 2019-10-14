# #########Fibonacci######
# a1 = []

# a = int(input("fist"))
# b = int(input("second"))
# d = input("range")
# a1.append(a)
# a1.append(b)
# c = 0
# for i in range(int(d)):
# 	c = a + b
# 	a1.append(c)
# 	a = b
# 	b = c 
	
# print(a1)
# def calculate_members(string):
# 	digits = 0
# 	letters = 0
# 	for char in string:
# 		if char.isalpha():
# 			letters += 1 
# 		if char.isdigit():
# 			digits += 1 
# 	return digits, letters

# user_string = input("Enter some sting ")
# digits, letters = calculate_members(user_string)
# print("Num of digits: ", digits, ", and number of letters: ", letters)

#ex4
import random
import string
def randomString(stringLenght=3):
    """Generate a arandom string of fixed length"""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range (stringLenght))
rand_string = randomString()
print(rand_string)
check_list = []
for i in rand_string:
	check_list.append(i)
print(check_list)

def guess_letters():
    guess = False
    len_of_random_string = len(rand_string)
    guessed_letters_amount = 0
    while guess == False:
        if guessed_letters_amount != len_of_random_string:
            letter = input("Enter a letter ->")
            while not (letter.isalpha() and len(letter) == 1):
                print("You have entered a not valid letter.")
                letter = input("Enter a new letter ->")
            for i in check_list:
                if letter == i:
                    guessed_letters_amount += 1
                    print("Letter was found.")
                    check_list.remove(i)
        else:
            guess = True
            print("You found the string:", rand_string)
            
guess_letters()