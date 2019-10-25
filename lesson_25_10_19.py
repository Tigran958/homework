while True:
	
	try:
		first_input = input("Input string! ")
		a = "1234567890"
		for i in a:
			if i in first_input:
				raise
	break
	except:	
		print(first_input)
		

list1 = [1, 2, 3, "a", 'b', 4, 9, "i", "asd", "10"]



while True: 
	try:
		input_2 = int(input("enter an int "))
		print(list1[input_2])
		break
	except IndexError:
		print("wrong! ")
	except ValueError:
		print("wrong! ")


dict1 = {"s1": 15, "s2": 51}
while True: 
	try:
		input_2 = input("enter a key ")
		print(dict1[input_2])
		break
	except KeyError:
		print("wrong key ")
	