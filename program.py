import numpy as np
import matplotlib.pyplot as plt

beta, gamma = 0.4, 0.1 #wartosci dla covid19
s, i, r = 0.99, 0.01, 0.0

czas = np.linspace(0, 100, 100)
sw, iw, rw = [], [], []
#w dla wartosci
for t in czas:
    ds = -beta * s * i
    di = beta * s * i - gamma * i
    dr = gamma * i
    s += ds
    i += di
    r += dr
    sw.append(s)
    iw.append(i)
    rw.append(r)

sw = np.array(sw) * 100
iw = np.array(iw) * 100
rw = np.array(rw) * 100
plt.plot(czas, sw, label='S (podatni)')
plt.plot(czas, iw, label='I (zakazeni)')
plt.plot(czas, rw, label='R (wyzdrowiali)')
plt.xlabel('dni')
plt.ylabel('procent populacji')
plt.grid(True)
plt.legend()
plt.show()
