
first_input = input("Tell me a number ")
number_1 = int(first_input)

if number_1 >= 0:
    if number_1 != 0:
       print("It is positive")
    else:
       print("it is 0")
else:
	print("it is negativ")
###########second##########
first_1_input = input("Tell me the temperature and I'll  tell you what to do ")
temp = int(first_input)
if temp > 0:
	if temp > 20:
		print("It is hot outside, take off your jacket")
	elif temp > 10:
		print("You can go out with your jack")
	else:
		print("take your coat")
elif temp < 0 and temp > -10:
	print("Find somthing to burn fire")
else:
	print("what are you doing? go back to your bad")

