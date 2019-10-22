# 1. Write a Python class which has two methods get_String and print_String. get_String accept a string from 
# the user and print_String print the string in upper case.

class MyClass:
	def input_string(self,u_input):
		self.user_input = u_input

	def upper_string(self):
		return self.user_input.upper()
		

first = MyClass()
first.input_string(input("Enter something! "))
print(first.upper_string())

# 2. Create a vehicle class. Create two new vehicles called car1 and car2. Set car1 to be a red convertible
# worth $60,000.00 with a name of Fer, and car2 to be a blue van named 
# mp worth $10,000.00.

class Vehicle:
	def __init__(self, name, type_, color, price):
		self.name = name
		self.type = type_
		self.color = color
		self.price = price

car1 = Vehicle("Fer", "convertible", "Red", '$60000')
car2 = Vehicle("Jump", "van", "Blue", "$10000")
print(car1.name, car1.type, car1.color, car1.price)
print(car2.name, car2.type, car2.color, car2.price)

