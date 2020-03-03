import threading
import time

def threading_function():
	for i in range(0,10):
		print(i)
		time.sleep(1)

# threading_function()
x = threading.Thread(target = threading_function)

x.start()
print("asda")

# import threading
# import time

# def a_func():
# 	for i in range(0,101):
# 		print(i)
		
# # threading_function()

# def b_func():
# 	for i in range(-100,0):
# 		print(i)

# x = threading.Thread(target = a_func)


# x.start()
# b_func()

# import M_t_1
# import datetime
# import threading


# f = datetime.datetime.now()
# # j = M_t_1.calculate()
# # print(b)
# g = threading.Thread(target=M_t_1.calculate)

# l = g.start()
# k = 0
# while k < 30:
# 	print(f)
# 	k += M_t_1.calculate()

# i = 0
# while i < 30:
	
# 	print(b)
# 	i += 1

