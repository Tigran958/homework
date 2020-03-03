class Cards:
	def __init__(self, type_, values):
		self.type1 = type_
		self.value = values

	def show(self):
		print(f"{self.value} of {self.type1} ")

class Deck:
	def __init__(self):
		self.list = []
		self.build()

	def build(self):
		for t in ["spades", "hearts", "diamonds", "clubs"]:
			for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "Q", "K", "T"]:
				self.list.append(Cards(t, v))

	def shoow(self):
		for c in self.list:
			c.show()

first = Deck()

first.shoow()
print(first.list[1])

##################
# def name_print(x):
# 	print(x)

# class MyClass:
# 	def __init__(self,name):
# 		self.name = name

# 	def show(self):
# 		name_print(self.name)



# a = MyClass("T")
# a.show()
# print(a.name)

# a.name = 5
# print(a.name)

list1 = [1, 2, 3, 4, 5]

for i in range(0, -len(list1), ):
	print(list1[i])


