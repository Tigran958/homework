import M_t_1
import datetime
import threading


f = datetime.datetime.now()

g = threading.Thread(target=M_t_1.calculate)

l = g.start()
k = 0
while k < 30:
	print(f)
	k += M_t_1.calculate()
