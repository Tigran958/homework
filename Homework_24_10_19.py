# 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a 
# list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# [‘34’, ‘67’, ‘55’, ‘33’, ‘12’, ‘98’]
# (‘34’, ‘67’, ‘55’, ‘33’, ‘12’, ‘98’)
# numbers_input = input("Enter your numbers! ")

# elements_list = numbers_input.split(",")
# print(elements_list)

# elements_tuple = tuple(elements_list)
# print(elements_tuple)


# 2. Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

words_input = input("Enter the words! ")
list_add = []
list_original = words_input.split(" ")
print(list_original)
list_original.sort()
print(list_original)

for i in list_original:
	if i not in list_add:
		list_add.append(i)

print(list_add)
string = ""
for i in range(len(list_add)):
	if i != 0:
		string += " " + list_add[i]
	else:
		string += list_add[i]
print(string)