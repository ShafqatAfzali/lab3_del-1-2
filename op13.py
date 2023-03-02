import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime


filnavn = './hist_mydaq.csv'


B = 3828
K = 0.0263
# målt verdi
målt_Resistans = 10000
målt_Voltage = 5


def V_til_T(Uth_vektor):
    tt = B/np.log(Uth_vektor*målt_Resistans /
                  (K*(målt_Voltage-Uth_vektor)))+273.15
    return tt


dt_format = '%Y-%m-%d %H:%M:%S.%f'


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
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('dark_background')


# Hent og plott funksjon
def stream_plott(i):
    data = pd.read_csv(filnavn)

    tid_vektor = list(
        map(lambda x: datetime.strptime(x, dt_format), data['timestamp']))

    # gjør V til T
    temp_vektor = V_til_T(data["voltage"])

    plt.cla()
    plt.gcf().autofmt_xdate()

    # --- SKRIV KODE HER
    plt.plot(tid_vektor, temp_vektor)
    plt.title("tid vs temperatur", fontdict=font2)
    plt.xlabel("tid", fontdict=font)
    plt.ylabel("temperatur i celsius", fontdict=font)
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), stream_plott, interval=100)
plt.tight_layout()
plt.show()
