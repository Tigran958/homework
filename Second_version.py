import M_t_1
import datetime
import threading


f = datetime.datetime.now()
# j = M_t_1.calculate()
# print(b)
g = threading.Thread(target=M_t_1.calculate)

l = g.start()

while g.is_alive():
	print(f)
print(g.is_alive())