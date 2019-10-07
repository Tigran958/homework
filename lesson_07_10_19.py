'''my_integer = 14
print(id(my_integer))
my_integer += 1
print(id(my_integer))

my_str = "A"
print(id(my_str))
my_str += 'f'
print(id(my_str))

a = 1 
b = 1 
print(id(a))
print(id(b))

a = 1 + 1
b = 1 + 1
print(id(a)==id(b))
print(a is b)

a = 1.0 
b = 1.0 
print(id(a)==id(b))
print(a is b)
# '''
# count = 0
# first_in = input("enter something ")
# ord_var = ord("!")

# for i in first_in:
# 	if ord(i) == ord_var:
# 		count +=1
# print(count)

some_1 = "1234567"
print(some_1[0])
print(some_1[0:3])
print(some_1[-3:-1])
 
print(some_1[-1])

my_string = 'this is MY string!'

print(my_string)
print(my_string.capitalize())
print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string.replace("MY","Your"))
