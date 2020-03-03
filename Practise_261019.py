# # a = int(input("Enter the number "))

# # list_1 = [10, 20, 10, 40, 50, 60, 30]
# # list_2 = []

# # for i in range(len(list_1)):
# # 	for j in range(len(list_1)):
# # 		if list_1[i] + list_1[j] == a and i != j:
# # 			b = [i,j]
# # 			if b not in list_2 and b.reverse() not in list_2:
# # 				list_2.append(b)

# # print(list_2)

# # class Account:
# # 	def __init__(self, name, sname, age = '10', a = 10):
# # 		self.name = name
# # 		self.sname = sname
# # 		self.age = age
# # 		self.a = a


# # account = Account('Tigran', 'Danielyan', age =1000)
# # print(account.age)

# # list1=[1,"j"]
# # print(list1.isalpha())
# # def encrypt(text,s):
# # 	result = ""
# # # transverse the plain text
# # 	for i in range(len(text)):
# # 		char = text[i]
# # # Encrypt uppercase characters in plain text
      
# # 		if (char.isupper()):
# # 			result += chr((ord(char) + s-65) % 26 + 65)
# # 			print(chr(ord(char)))
# # # Encrypt lowercase characters in plain text
# # 		else:
# # 			result += chr((ord(char) + s - 97) % 26 + 97)
# # 			print(chr(ord(char)))
# # 	return result
# # #check the above function
# # text = "CEASER CIPHER DEMO"
# # s = 1000

# # print("Plain Text : " + text)
# # print("Shift pattern : " + str(s))
# # print("Cipher: " + encrypt(text,s))

# # print(chr(2))
# list0 = "abcdefghijklmnopqrstuvwxyz"
# list1 = input("Write your sentence: ")
# list1 = list1.lower()
# a = int(input("Write your step: "))
# b = a % 26
# new_list = ""
# for i in range(len(list1)):
# 	h = list0.find(list1[i])
# 	if h != -1:
# 		new_list += list0[(h+b)%26]    
# 	else:
# 		new_list += list1[i]
# print(new_list)



# import random
# import string
# import threading

# str_input = int(input("Tell how many chars will your pasword contain "))
# int_input = int(input("Tell how many numbers will your pasword contain "))


# b = string.ascii_lowercase
# list_str = []
# list_int = []

# for i in range(str_input):
# 	list_str.append(b[i])

# for i in range(int_input):
# 	a = random.randint(1,100)
# 	list_int.append(str(a))

# pasword_list = []
# pasword_list.extend(list_int)
# pasword_list.extend(list_str)
# print(pasword_list)
# password1 = []

# for i in pasword_list:
# 	print(i)
# 	password1.insert(random.randint(0,len(pasword_list)), i)

# print(password1)

# pasword_string = ""
# for i in password1:
# 	pasword_string += i
# print(pasword_string)

import random
user_deck = []
user_deck_value = []
dealer_deck = []
dealer_deck_value = []
deck = []
numbers = {"Ace": 11, "King": 4, "Queen" : 3, "Jack": 2, "10":10, "9":9,
            "8":8, "7": 7, "6": 6, "5" : 5, "4": 4, "3": 3, "2": 2}
suit = ["Heart", "Diamond" , "Club", "Spade"]
for i in numbers.keys():
    for j in suit:
        deck.append(str(j) + " of " + str(i))
# print(deck)    
# a = f"{deck[random.randint(0, len(deck)-1)]}"
# print(a)
for i in range(2):
    s = random.randint(0,len(deck)-1)
    user_deck.append(deck[s])
    # user_deck_value.append(numbers)
    del deck[s]
for j in range(2):
    h = random.randint(0,len(deck)-1)
    dealer_deck.append(deck[h])
    del deck[h]
        
print("user deck", user_deck)
print("dealer deck",dealer_deck)
print(deck)
user_turn = input("Do your turn"  )
u1 = random.randint(0,len(deck)-1)
user_deck.append(deck[u1])
print("Your suit is - ", deck[u1])
del deck[u1]
dealer_turn = input("Dealer turn"  )
d1 = random.randint(0,len(deck)-1)
dealer_deck.append(deck[d1])
print("Your suit is - ", deck[d1])
del deck[d1]
print("user deck", user_deck)
print("dealer deck",dealer_deck)