human = {'name': 'Tigran', 'surname': 'Danielyan', 'age': 23, 'is_married': False}
print(human)
print(human['name'], human['age'], human['is_married'])

human = {'name': 'Tigran', 'surname': 'Danielyan', 'age': 23, 'is_married': False}
print(human)

human['age'] = 30

human['have_pet'] = False

del human['age']

print(human)

human = {'name': 'Tigran', 'surname': 'Danielyan', 'age': 23, 'is_married': False}
print(human.keys())
print(human.values())

for value in human.values():
	print(value)

fruits = {'apple': 5, 'orange': 14, 'pineapple': 1, 'bananas': 4, 'pomegranade': 6}

for key in fruits.keys():
	if fruits[key] > 5:
		print(key)

grades = {'Gor': 26, 'David': 26, 'Vardges': 26, 'Rafayel': 28, 'Khachatur': 23, 'Marat': 24, 'Artur': 23, 'Sedrak': 24, 'Marianna': 25, 'Vardges D': 28, 'Tigran': 28}

print(grades)

for i in grades.keys():
	print(i, grades[i])

grades['Tigran'] = 25

print(grades)

for i in grades.keys():
	print(i, grades[i])

for (i,j) in grades.items():
	print(i, j)

classes = {"Math": ["David", "Lucy", "Anne"],
			"Phisics": ["Addison", 'Benjamin'],
			"Chemistery": ["Sara", "Pele"]}

print("Students in math classes: ", classes["Math"])
classes['Math'].append("Tigran")
print("Students in math classes: ", classes["Math"])

persons = {'Anne': {"phone": 21233123, "age": 56}, 'Mary': {"phone": 255869, "age": 19}}

print(persons['Anne']['phone'])

for (i,j) in persons.values():
 	print(i, j)

text = "text messaging or texting is the act of composing and sending electronic messages typically consisting of alphabetic and numeric characters between two or more users of mobile devices desktops laptops or other type of compatible computer Text messages may be sent over a cellular network or may also be sent via an Internet connection"
text = text.lower()
words_dict = {}

text = text.split(" ")

for word in text:
	if word in words_dict.keys():
		words_dict[word] += 1
	else:
		words_dict[word] = 1


for (word, amount) in words_dict.items():
	if amount > 1:
		print(word, ":", amount)

