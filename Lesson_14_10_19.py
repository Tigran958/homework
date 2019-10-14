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