# OOP
# class Name:
# 	def __init__(self):
# 		self.first_name = "[no first name]"
# 		self.last_name = "[no last name]"

# class Person:
# 	def __init__(self):
# 		self.name = Name()
		
# 		self.eyecolor = "[no eye color]"

# my_person = Person()

# print(my_person.name.first_name)
# print(my_person.name.last_name)
# print(my_person.eyecolor)

# class Person:
# 	def __init__(self, first_name, last_name):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.eyecolor = "[no eye color]"



# my_person = Person("Tigran", "Danielyan")

# print(my_person.first_name)
# print(my_person.last_name)

# print(my_person.eyecolor)
# my_person.eyecolor = "Brown"
# print(my_person.eyecolor)

# my_person2 = Person("sda", "Dasd")
# print(my_person2.first_name)
# print(my_person2.last_name)

class BankAccount:
	def __init__(self, name, balance=0.0):
		self.log("Account created")
		self.name = name
		self.balance = balance

	def getBalance(self):
		self.log("Balanc checked at " + str(self.balance))
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		self.log("+ " + str(amount) + ": " + str(self.balance))

	def withdraw(self, amount):
		self.balance -= amount
		self.log("- " + str(amount) + ": " + str(self.balance))

	def log(self, message):
		print(message)

my_bank_account = BankAccount("Tigran Danielyan")
my_bank_account.deposit(20.0)		
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()
