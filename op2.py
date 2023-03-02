import matplotlib.pyplot as plt
import numpy as np


k_konstant = 0.0263
b_konstant = 3828


def cels_to_kelv(temp):
    x = temp+273.15
    return x


def resist(temp):
    R = k_konstant*np.exp(b_konstant/temp)
    return R


xx = [i for i in range(0, 501, 1)]
temp_cels = []  # fra 0-50 mellomrom=0.1
temp_kelv = []  # fra 273-323.15 ish mellomrom=0.1
resistans = []

for i in xx:
    tc = i/10
    tk = cels_to_kelv(tc)
    res = resist(tk)
    temp_cels.append(tc)
    temp_kelv.append(tk)
    resistans.append(res)


plt.plot(temp_cels, resistans)
plt.axis([-10, 120, -20, 35000])
plt.title("temperatur vs resistans")
plt.xlabel("temperatur i celsius")
plt.ylabel("resistansen i ohm")
plt.show()
