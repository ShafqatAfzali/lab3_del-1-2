import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


filnavn = './hist_mydaq.csv'

binST = 0.05
B = 3828
K = 0.0263
# målt verdi
målt_Resistans = 10000
målt_Voltage = 5


def V_til_T(Uth_vektor):
    tt = B/np.log(Uth_vektor*målt_Resistans /
                  (K*(målt_Voltage-Uth_vektor)))-273.15
    return tt


fortsett = True


def avslutt():
    global fortsett
    input("\n trykk enter for å avslutte\n")
    fortsett = False


# font = {'family': 'serif',
#        'color': 'white',
#        'weight': 'normal',
#        'size': 10,
#        }

# font2 = {'family': 'san-serif',
#         'color': 'white',
#         'weight': 'bold',
#         'size': 12,
#         }

# plt.style.use('dark_background')


def stream_hist():
    data = pd.read_csv(filnavn)

    temp_vekt = V_til_T(data["voltage"])
    binner = np.arange(start=temp_vekt.min()-binST,
                       stop=temp_vekt.max()+binST, step=binST)

    av = np.mean(temp_vekt)
    std = np.std(temp_vekt, ddof=1)

    plt.cla()
    plt.gcf().autofmt_xdate()

    plt.hist(temp_vekt, binner, color="red", ec="lightblue")
    # plt.vlines(av, linestyle = "--", color = "black")
    # plt.vlines(av-std, linestyle = '--', color = 'dimgray')
    # plt.vlines(av+std, linestyle = '--', color = 'dimgray')
    plt.title("temperatur antall per temperature")
    plt.xlabel("temperatur")
    plt.ylabel("antall")
    plt.tight_layout()


FuncAnimation(plt.gcf(), stream_hist, interval=100)
plt.tight_layout()
plt.show()
