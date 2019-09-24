##############1#################
first_print = "Check odd/even numbers"
print(first_print)
input_number = input("Hello, tell me a number, and I will tell you wether it is odd or even ")
check_number = int(input_number) % 2 
last_print = "your number is odd -> "
last_print_2 = "your number is even -> "
last_print_3 = "your number is 0 -> "
check_odd = check_number == 1
check_even = check_number == 0 and input_number != "0"
check_zero = input_number == "0"
print(last_print + str(check_odd))
print(last_print_2 + str(check_even))
print(last_print_3 + str(check_zero))

##############2#################

f_text = "Let's calculate area of the circle with area = Pi*r**2 function"
f_2_text = "The value of Pi is constant and equals 3.1426968"
quest = "So tell me the value of the radius "
calc_area = "The area of the circle with the given radius is "
pi = 3.1426968
print(f_text)
print(f_2_text)
radius_1 = float(input(quest))
radius_1 *= radius_1 * pi
print(calc_area + str(radius_1))

##############3#################

import datetime
current_date = datetime.datetime.now()
txt_time = "Curren date is :"
print(txt_time)
print(current_date)