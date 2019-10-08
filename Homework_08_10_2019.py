'''string_t = "abhskdakssa"
print(string_t[len(string_t) :1])
print(string_t.find("a",string_t.find("a")+1 ))
x = (string_t.replace("a", "$",3)[1:len(string_t)])
print(string_t.)

print(x)

#########1#######
print("Task_1: char -> '$' converter \n")
check = 0
first_input = input("Enter something! ")	
while check != 1:
	try:
		char_first = first_input[0]
		check = 1
	except IndexError:
			
		first_input = input("You should enter something! ")
	except TypeError:
				
		first_input = input("You should enter something!")	

for i in first_input:
	if ord(i) == 0:
		continue
	elif char_first == i:
		first_input_1 = first_input.replace(i , '$' , ord(i))

text_half = first_input_1[1 : len(first_input_1)]
print('\nSample String: ' + first_input)
print('Expected Result: ' + char_first + text_half)
print("\n")
'''
##############2###########
print('Task_2: ing/ly\n')

add_ing = "ing"
add_ly = "ly"
input_2 = input('Input something to add ing or ly: ')

if len(input_2) < 3:
	print(input_2)
elif len(input_2) == 3:
	if input_2.find("ing") < 0:
		print('Result: ' + input_2 + add_ing)
	else:
		print('Result: ' + input_2 + add_ly)
elif len(input_2) > 3:
	if input_2.find("ing" , len(input_2)-3) < 0:
		print('Result: ' + input_2 + add_ing)
	else:
		print('Result: ' + input_2 + add_ly)		
print("\n")

###########3##########		
print("Task_3: Poor/good\n")

text_input = input("Enter a sentence: ")
poor_ord = text_input.find("poor")
not_ord = text_input.find("not")
if not_ord < poor_ord and not_ord >= 0:
	print_text_1 = text_input.replace("not", "")
	print_text = print_text_1.replace("poor", "good")
else:
	print_text = text_input

print(print_text)



