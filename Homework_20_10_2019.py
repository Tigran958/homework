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

		out_put_file = open("OutputFile.txt", "a")
		
		out_put_file.write(message)
		out_put_file.write("\n")
		
		out_put_file.close()

my_bank_account = BankAccount("Tigran Danielyan")
my_bank_account.deposit(20.0)		
my_bank_account.getBalance()
my_bank_account.withdraw(10.0)
my_bank_account.getBalance()
