def add_to_numbers(num1,num2):
	return int(num1) + int(num2)

first_number = input("first enter ")
second_number = input("second enter ")

print(add_to_numbers(first_number,second_number))

def print_hello_world():
	print("Hello world")

print_hello_world()


def call_function(func):
	if func > 0:
		return "it's hot"
	else:
		return "it's cold"

first_input = int(input("temperature ? "))
print(call_function(first_input))

def check_num(number):
	if number % 2 == 0:
		return "even"
	return "odd"

our_number = input("enter a number ")
print(check_num(int(our_number)))