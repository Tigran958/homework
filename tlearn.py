
# # class MyNumbers:
# #   def __iter__(self):
# #     self.a = 1
# #     return self

# #   def __next__(self):
# #     if self.a <= 20:
# #       x = self.a
# #       self.a += 1
# #       return x
# #     else:
# #       raise StopIteration

# # myclass = MyNumbers()
# # myiter = iter(myclass)

# # for x in myiter:
# #   print(x)
# numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10","V", "D", "K", "T"]
# mast = ["Heart", "Diamond", "Spade", "Clubs"]
# deck = []

# for i in mast:
# 	for j in numbers:
# 		a = i + " " + j		
# 		deck.append(a)
# print(deck)

# import_random.comp_choice(deck)

# def myfunc():
#   global x
#   x = 300

# myfunc()

# print(x)

# import platform

# x = platform.system()
# print(x)




# x = dir(ir)
# print(x)

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))



# x = datetime.datetime(2020, 5, 17)

# print(x)
# price = 49
# txt = F"The price is {price} dollars"
# print(txt.format(price))
# mylist = ["a", "b", "a", "c", "c"]
# # a = dict(mylist)
# # print(a)
# # mylist = list(dict.fromkeys(mylist))
# # print(mylist)
# c = 'sada'
# f = 2
b = {'asd':{'a':'popap', "bab":[5555]}, 'asda' : 242}

# a = b.fromkeys(b)
# print(a)
# print(b)
a = b["asd"]['a']
print(a)