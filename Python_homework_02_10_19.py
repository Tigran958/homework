##########1##########

def max_number(num1, num2, num3):
	if num1 > num2:
		if  num2 >= num3:
			return num1
		elif num2 < num3 and num3 < num1:
			return num1
		elif num2 < num3 and num3 == num1:
			return num1
		return num3

	elif num1 == num2:
		if num2 > num3:
			return num1
		elif num2 == num3:
			return "Numbers are equal."
		return num3	

	elif num1 < num2:
		if num2 > num3:
			return num2
		elif num2 < num3:
			return num3
		return	num2

print("Tell me three numbers and see wich is the bigist!")
first_input = float(input("Enter first number: "))
second_input = float(input("Enter second number: "))
third_input = float(input("Enter third number: "))
print("The bigist number is: ", max_number(first_input,second_input,third_input))

#############2#############
print('')
print("")
def fizz_buzz(number):
	if number % 3 == 0:
		if number % 5 == 0:
			return "FizzBuzz!"
		return "Fizz!"

	elif number % 5 == 0:
		if number % 3 == 0:
			return "FizzBuzz!"
		return "Buzz!"
	
	return number	

print("Let's see, whether the number is Fizzable or Buzzable or both.")
number_input = float(input("FizzBuzz_Number: "))
print(fizz_buzz(number_input))

#########3#########
print("")
print("")
print("See the type of numbers in a given range")			
range_input = int(input("Enter the end of your range ")) + 1

def showNumbers(limit):
	for i in range(0,limit):
		if i % 2 == 0:
			print(str(i) + " EVEN")
		elif i % 2 != 0:	
			print(str(i) + " ODD")
showNumbers(range_input)				

