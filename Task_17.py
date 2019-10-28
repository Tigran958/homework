dict_1 = {"a": 1, "b": 4, "c": 5, "h": 9}
dict_2 = {"h": 1, "b": 4, "c": 1, "h": 9}
dict_3 = {}

for key in dict_1.keys():
	if key in dict_2.keys() and dict_1[key] == dict_2[key]:
		dict_3[key] = dict_1[key]

print(dict_3)