import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

binST = 0.01

filnavn = './hist_mydaq.csv'
B = 3828
K = 0.0263
# målt verdi
målt_Resistans = 10000
målt_Voltage = 5
data = pd.read_csv(filnavn)


def V_til_T(Uth_vektor):
    tt = B/np.log(Uth_vektor*målt_Resistans /
                  (K*(målt_Voltage-Uth_vektor)))-273.15
    return tt


temp_vekt = V_til_T(data["voltage"])

binner = np.arange(start=temp_vekt.min()-binST,
                   stop=temp_vekt.max()+binST, step=binST)


font = {'family': 'serif',
        'color': 'white',
        'weight': 'normal',
        'size': 10,
        }
font2 = {'family': 'sans-serif',
         'color': 'white',
         'weight': 'bold',
         'size': 12,
         }

plt.style.use('dark_background')
plt.hist(temp_vekt, bins=binner, color="red", ec="lightblue")
plt.title("temperatur antall per temperature", fontdict=font2)
plt.xlabel("temperatur", fontdict=font)
plt.ylabel("antall", fontdict=font)
plt.gca()
plt.tight_layout()
plt.show()
