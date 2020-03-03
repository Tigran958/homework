# The function for Caesar cipher
def caesar(b,num):
	alpha = "abcdefghijklmnopqrstuvwxyz"

	if b.isupper():
		alpha = alpha.upper()
	
	ind_l = alpha.find(b)

	# ind_new = ind_l + num
	# while ind_new >= 26:
	# 	ind_new -= 26
	# or we can solve in better way
	ind_new = (ind_l + num) % 26
	return alpha[ind_new]	


# Checks of input values
y = True
while y:
	try:
		first_input = input("Enter the string ")
		if not first_input.isalpha():
			raise
		y = False
	except:
		print("Ther should be only letters!")
		
y = True
while y:
	try:
		shift_input = int(input("Enter the shift number "))
		y = False
	except ValueError:
		print("It wasn't a number!")

caesar_string = ""
for i in first_input:
	caesar_string += caesar(i,shift_input)

print(caesar_string)
		
