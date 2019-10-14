'''my_int1 = 1
my_int2 = 2
my_int3 = 3

out_put_file = open("OutputFile.txt", "w")

out_put_file.write(str(my_int1))
out_put_file.write(str(my_int2))
out_put_file.write(str(my_int3))

out_put_file.close()

my_list = ['Tiran', 'Tiran', 'Tiran', 'Tiran',]

out_put_file = open("OutputFile.txt", "w")
for line in my_list:
	out_put_file.write(line)

out_put_file.close()


my_list = ['Tiran', 'Tiran', 'Tiran', 'Tiran',]

out_put_file = open("OutputFile.txt", "w")

out_put_file.writelines(line)

out_put_file.close()


my_list = ['Tiran', 'Tiran', 'Tiran', 'Tiran',]

out_put_file = open("OutputFile.txt", "w")
for line in my_list:
	out_put_file.write(line + "\n")

out_put_file.close()


my_list = ['Tiran', 'Tiran', 'Tiran', 'Tiran',]

out_put_file = open("OutputFile.txt", "a")
for line in my_list:
	out_put_file.write(line + "\n")

out_put_file.close()

out_put_file = open("OutputFile.txt", "r")

print(out_put_file.readline())
print(out_put_file.readline())

out_put_file.close()


names_list = []

out_put_file = open("OutputFile.txt", "r")
for line in out_put_file:
	names_list.append(line)

out_put_file.close()

print(names_list)




def list_creat(list_f,n):
	list_1 =[]

	for i in list_f:
		if len(i) > n:
			list_1.append(i)
	return list_1		 

a = ['sa', 'asdas', 'asdsa']

print(list_creat(a,1))

'''
user_input = input('somer string ')

for i in range(len(user_input)):
	if i % 2 != 0:
		user_input[i] = ''
print(user_input)


