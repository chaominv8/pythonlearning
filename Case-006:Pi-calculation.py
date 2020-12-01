#Calculate Pi
import random
import time
start = time.perf_counter()
c = 0
s = 0
for i in range(1000000):
    s += 1
    x = random.random()
    y = random.random()
    if pow(x, 2) + pow(y, 2) <= 1:
        c += 1
pi = (c / s) * 4
print("圆周率的值是: {0:.6f} \n运行时间为 {1:.3f} 秒".format(pi,time.perf_counter()-start))


