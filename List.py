'''my_list = [1,0,2,3, 4, 5, 6, 7, 8, 9, 10 ]

my_list.remove(10)
print(my_list, ': After removing 10')

my_list.sort()
print(my_list, ': After sorting')

my_list.reverce()
print(my_list, ': After revercing')

my_list.pop()
print(my_list, ': poping')

del my_list[-5:]
print(my_list, ": After deleting the last 5 items")

my_list = [1, 2, 3, 4]

my_list.append(5)
print(my_list, ": After appending")

new_list = [6, 7, 8]
my_list.extend(new_list)
print(my_list, ": After extending")

my_list.insert(0, 0)
print(my_list, ": After inserting zero")

def average(in_list):
	sum = 0
	for number in in_list:
		sum += number
	return sum / len(in_list)


my_list1 = [1, 2, 3, 4, 5, 6, 7]
my_list2 = [91,92,93,94,95,96,97]

print("The average of my_list1 is: ", average(my_list1))
print("The average of my_list2 is: ", average(my_list2))

def two_D_average(in_2d_list):
	result = []
	for num_list in in_2d_list:
		sum = 0
		for number in num_list:
			sum += number

		result.append(sum / len(num_list))
	return result

my_2d_list = [[61, 32, 12, 123], [123, 131, 131, 123], [4, 1, 2]]
print("averages: ", two_D_average(my_2d_list))


def max_of_numbers(list_n):
	a = 0
	for i in list_n:
		if i > a:
			a = i
	return a

list_n = [1,2,3,4]
print(max_of_numbers(list_n))

'''


