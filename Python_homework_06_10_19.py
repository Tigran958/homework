############1##########
print("Kilometer_converter_rewrited:\n")
def kilometer_converter(lenght):
	kilo_to_mile = 0.621371
	if lenght * kilo_to_mile > 1:
		return str(lenght) + ' kilometers equal ' + str(lenght * kilo_to_mile) + ' miles'
	return str(lenght) + ' kilometer equals ' + str(lenght * kilo_to_mile) + ' mile'
	

first_input = "a"
while type(first_input) != int or first_input == 0: 
	try:
		first_input_f = input("How many kilometers  do you want to convert? ")
		first_input = int(first_input_f)
		zero_div_er = 5 / first_input
		
	except ValueError:
		print("You should input a number")
	except ZeroDivisionError:
		print('There is no sence in inputing zero')	
	
	
print(kilometer_converter(first_input))
print("\n")