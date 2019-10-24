class Veichle:
	def __init__(self, name, year):
		self.name = name
		self.year = year


class Model(Veichle):
	def __init__(self, name, year, color, price):
		super().__init__(name, year)	
		self.color = color
		self.price = price

	
model_1 = Model('red',"BMW", 2015, 20000)
print(model_1.name)
print(model_1.year)
print(model_1.color)
print(model_1.price)


class BankAccount:
	def __init__(self, name, amount):
		self.name = name
		self.__amount = amount

	def set_amount(self, amount_n):
		self.__amount = amount_n

	def show_amount(self):
		print(f"{self.name} your balance is {self.__amount}")

my_account = BankAccount("Tigran", 1000)
print(my_account.name)
my_account.show_amount()
my_account.__amount = 20000
my_account.show_amount()
my_account.set_amount(5000)
my_account.show_amount()

class Cat:
	def sound(self):
		print("miau")
class Dog:
	def sound(self):
		print("Haf")

cat1 = Cat()
dog1 = Dog()
dog1.sound()
cat1.sound()

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []

for i in list1:
	if i % 2 != 0:
		list3.append(i)

for i in list2:
	if i % 2 == 0:
		list3.append(i)

print(list3)

b = input("enter number! ")

if b == b[::-1]:
	print(True)
else:
	print(False)	


