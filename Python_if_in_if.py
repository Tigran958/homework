weather = input("wheather ")
place = "Sahara"
grade_of_temp = int(input("temperature in Sahara? "))

if weather == "Summer" :
	if place == "Sahara" and grade_of_temp < 0:
	    print("Are you crazy?")
else:
	print("I cant tell you anything")