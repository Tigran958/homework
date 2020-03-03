'''Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
# num_7 = 7
# num_5 = 5
# list_num = []
# for i in range(2000,3201):
# 	if i % 7 == 0 and i % 5 != 0:
# 		list_num.append(i)
# print(list_num)

'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
'''
# def factor(a):
	
# 	if a > 0:
# 		a *= factor(a-1)
# 		return a
# 	elif a == 0:
# 		return 1
	

# print(factor(5))

'''With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:'''
# user_input = int(input("num"))

# dict_1 = {}
# for i in range(1,user_input + 1):
# 	dict_1[str(i)] = i*i

# print(dict_1)


'''Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:'''
# us_input = input("something")
# list1 = us_input.split(",")
# tuple1 = tuple(list1)
# print(tuple1)

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
import re
value = []
items=[x for x in input().split(',')]
print(items)
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    print(re.search("[a-z]",p))    
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))