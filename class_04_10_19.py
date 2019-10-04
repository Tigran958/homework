my_string = "this string is not a number!"

try:
	print("Converting my_string to int...")
	1/0
	print("string #" + 1 + ": " + my_string)
	my_int = int(my_string)
	print(my_int)
except ValueError:
	print("Can't convert; my_string to a number")

except TypeError:
	print("Can't concatinate number with string")

except:
	print("Unknown error")


Print("done")	

try:
	input_file = open("NumberFile.txt", mode = "r")

	try:
		for line in input_file:
			print(int(line))

	except ValueError:
		print("A value error")

	else:
		print("No error occured")

	finally:
		input_file.close()

except IOError:
	print("An error occured while reading the file")					