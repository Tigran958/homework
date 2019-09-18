# variables
first_text = "Hello, lets do some calculation, I can show you an intersting fact"
name_quest = "What if we get to know each other at first, tell me your name "

#actions
import datetime
print(first_text)
answer_first = input(name_quest)
answer_name = "I'm really glad that we've met, " + answer_first
print(answer_name)
print("I can show you, how much your weight shuld be at the given height ")
height_quest = input("So tell me, how toll are you in cm-s? ")
height_float = float(height_quest)
print(height_quest + " cm" + " is a good height!")
weight_quest = input(" What about your weight and birth year, first how much do you weight in kilos? ")
weight_int = int(weight_quest)
date_birth_year = input("and the birth year? ")
birth_year = 2019 - int(date_birth_year)
print("Hmm " + weight_quest + " at " + str(birth_year) + "..., let me think")
input("Ok I've finished, if you want to see the result, please push Enter bottom")
index_bmi = weight_int/(height_float/100)**2
date_of_act = datetime.datetime.now()
print("So, " + answer_first + " in " + str(date_of_act)  + ", your body mass index (BMI) is -> " + str(index_bmi))
input("There are 6 stages of BMI, push Enter and find your result bellow")
print("	1. less than 18.5 -> Body mass deficit")
print("	2. 18.5-24.9      -> Normal body mass")
print("	3. 25.0-29.9      -> Excessive body mass")
print("	4. 30.0-34.9      -> Obesity 1st degree")
print("	5. 35.0-39.9      -> Obesity 2nd degree")
print("	6. 40 and more    -> Obesity 3rd degree")
print("Hope you liked it")