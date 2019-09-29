###########1############

number_q = input("Enter a number to see the multiplication table: ")
number_input = int(number_q)
range_number = range(0,11)

for i in range_number:
	print(number_q + "*" + str(i) + "=", number_input * i)

###########2############
print("")
number_1 = input("Enter a number and se the count of digits: ")
print(len(number_1))

############3###########

star = "*"
a_range = range(1,15)
count = 0 
first_count = 1
second_count = 4

print("Here we go for third task ")
print("")

for j in a_range:
	if count <= 4:
		print(first_count * star)
		count += 1
		first_count += 1

	elif count > 4:
		print(second_count * star)
		second_count -= 1
		if second_count == 0:
			break
	 

