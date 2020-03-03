import M_t_1
import datetime
import threading


f = datetime.datetime.now()

g = threading.Thread(target=M_t_1.calculate)


k = 0
l = g.start()
while k < 30:
	print(f)
	k += M_t_1.calculate()
	print(k)
print(k)