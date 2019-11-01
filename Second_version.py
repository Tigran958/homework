import M_t_1
import datetime
import threading



# j = M_t_1.calculate()
# print(b)
g = threading.Thread(target=M_t_1.calculate)

l = g.start()

while g.is_alive():
	f = datetime.datetime.now()
	print(f)
print(g.is_alive())