######1#######
print("Task_1: List_check\nIn this APP a valid list form is: [element1, element2, element3, ... elementN] without  " + '"-s' )
list_input = input('Input Your List! ')
list_input = list_input[1:len(list_input)-1]
range_limit = 1

for i in list_input:
	if i == ',':
		range_limit += 1

my_list = []
l = 0
k = 0 

for j in range(0, range_limit):

	if 	list_input.find(',', k) != -1:
		
		l = list_input.find(',', k) 
		
		my_list.append(list_input[k:l])
		
		k = l + 2
		
	else:
		
		my_list.append(list_input[l+1:len(list_input)])

count_i = 0
for i in my_list:
	if len(i) >= 4:
		if i[0] == i[-1]:
			
			count_i += 1
print("The resualt is: ", count_i)
print("\n")	

###########2###########
print("Task_2: check empty\n")

check_list = []

def check_empty(list_):
	len(list_)
	if len(list_) == 0:
		return "Empty"
	return "There is something"

print(check_empty(check_list))
print("\n")

#############3#############
print("Task_3: Find the longest word\n")

list_3 = ['asdas', 'asdasfadfaf', 'assaassdffgdhgfjh']

def longest_word(word_list):
	count_w = ""

	for i in word_list:
		if len(i) > len(count_w):
			count_w = i
	return count_w
print(longest_word(list_3))
print("\n")

##########4##########
print("Task_4: List_comparing_f\n")

l_1 = [1, 2, 3, 4]
l_2 = ['ab', 'dcda', 6]
def compare_lists(list_1,List_2):
	for i in list_1:
		if i in List_2:
			return True	
		return False
			
print(compare_lists(l_1,l_2))



