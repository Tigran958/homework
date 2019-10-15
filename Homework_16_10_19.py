########1########
print("Task 1 \n")
dict_1 = {"key1": 1, 'key2': 2, "key3": 3, 'key4': 1, 'key5': 2}
dict_new = {}

for key in dict_1.keys():
	if dict_1[key] not in dict_new.values():
		dict_new[key] = dict_1[key]
print(dict_new)

print('\n')
##########2############
print('Task 2 \n')

dict_2 = {"key1": 1, 'key2': 2, "key3": 3, 'key4': 6, 'key5': 9}
dict_check = {}

def max_number(dict_n,dict_a):
	max_num = 0
	max_item = ''
	for (key,value) in dict_n.items():
		if value >= max_num:
			max_num = value
			max_item = key
	dict_a[key] = max_num	
	return max_item
	
for i in range(3):
	z = max_number(dict_2,dict_check)
	del dict_2[z]	
	
print(dict_check,'\n')		
############3############
print('Task 3 \n')
string_var = input('Enter a string: ')
dict_string = {}
for i in string_var:
	if i in dict_string.keys():
		dict_string[i] += 1
	else:
		dict_string[i] = 1

print(dict_string,'\n')

########4############
print('Task 4 \n')
products_dict = {'meet': 3000, 'water': 100, 'juice': 1000, 'bread': 300, 'wine': 4000, 'brandy': 6000,
				'whiskey': 7000, 'bear': 1500, 'flour': 2000}
user_price = int(input('Enter the top level of the prices: '))
products_filtr = {}

for key in products_dict.keys():
	if products_dict[key] <= user_price:
		products_filtr[key] = products_dict[key]

print(products_filtr, '\n')

#########5############
print('Extra Task \n')

a = int(input('Enter the value of a, from ax**2 +bx + c = 0: a = '))
b = int(input('Enter the value of b, from ax**2 +bx + c = 0: b = '))
c = int(input('Enter the value of c, from ax**2 +bx + c = 0: c = '))

def solution_x(a,b,c):
	

	diskr = b**2 - 4 * a * c
	
	if diskr > 0: 
		x_1 = (-b + diskr**(1/2)) / (2 * a)
		x_2 = (-b - diskr**(1/2)) / (2 * a)
		return x_1,x_2
	elif diskr == 0:
		x_1 = (-b ) / (2 * a)
		x_2 = ''
		return x_1,x_2
	else:
		x_1 = "There isn't any solution"
		x_2 = ''
		return x_1,x_2

print(solution_x(a,b,c))
