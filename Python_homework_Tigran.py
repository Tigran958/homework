###########First. Word/sentence/number check#############
first_print = "Hello, tell me something and I'll try to guess if it is a sentence or a word or a number. "
word_print = "You have input a word"
sentence_print = "You have input a sentence"
number_print = "You have input a number"
pb = " "
n_0 = "0"
n_1 = "1"
n_2 = "2"
n_3 = "3"
n_4 = "4"
n_5 = "5"
n_6 = "6"
n_7 = "7"
n_8 = "8"
n_9 = "9"

input_first = input(first_print)
check_number_in = (n_0 in input_first) or (n_1 in input_first) or (n_2 in input_first) or (n_3 in input_first) or (n_4 in input_first) or (n_5 in input_first) or (n_6 in input_first) or (n_7 in input_first) or (n_8 in input_first) or (n_9 in input_first)

if check_number_in:
	if pb not in input_first:
	    print(number_print)
	else:
	    print(sentence_print) 
elif pb in input_first:
    print(sentence_print)
else:
	print(word_print)


##############Second. 5 and 11 div check #################
input_number = "Tell me a number and I'll tell you wheather it divides by 5 and 11 or not "
div_5_not_11 = "It is divisible by 5 but not 11"
div_5_and_11 = "It is divisible by 5 and 11"
div_11_not_5 = "It is divisible by 11 but not 5"
div_n_5_n_11 = "It is divisible neither 5 nor 11"

number_check = int(input(input_number))
check_5 = number_check / 5 
check_11 = number_check / 11

if check_5 // 1 == check_5:
	if check_11 // 1 == check_11:
		print(div_5_and_11)
	else:
		print(div_5_not_11)
elif check_11 // 1 == check_11:
	print(div_11_not_5)
else:
	print(div_n_5_n_11)

#########Third. Leep year check############
third_print = "Do you want to know is it a leep year? Then input a number "
leep_print = "This is a leep year"
no_leep_print = "This is not a leep year"
year_input = int(input(third_print))

year_4 = (year_input / 4) // 1 == (year_input / 4)
year_100 = (year_input / 100) // 1 == (year_input / 100)
year_400 = (year_input / 400) // 1 == (year_input / 400)

if year_4:
    if year_400:
        print(leep_print)
    elif year_100:
        print(no_leep_print)
    else:
    	print(leep_print)
else:
    print(no_leep_print)







	


