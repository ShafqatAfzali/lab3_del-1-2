
import nidaqmx
import csv
from datetime import datetime
import threading as th


filnavn = 'data_mydaq.csv'

# navn for myDQA
MYDAQ_navn = 'myDAQ?'
inngang_navn = 'ai0'


fortsett = True

# funksjon som lytter etter tastetrykk, og hvis dette skjer så avsluttes scriptet


def avslutt():
    global fortsett
    input("\n trykk enter eller hold ctrl og trykk på denne lenken: https://www.youtube.com/watch?v=crUQ2rAk5AE&ab_channel=vinii_35i\n")
    fortsett = False


def read_voltage():
    th.Thread(target=avslutt, args=(), name='avslutt',
              daemon=True).start()

    # åpner kommunikasjon med myDQA
    inngangs_spenning = nidaqmx.Task()
    inngangs_spenning.ai_channels.add_ai_voltage_chan(
        MYDAQ_navn, "/", inngang_navn)

    # lager cvs fil og legger til header
    fieldnames = ["tid", "spenning"]
    with open(filnavn, 'w') as csv_file:
        skriver = csv.DictWriter(csv_file, fieldnames=fieldnames)
        skriver.writeheader()

    # leser verdi og setter det inn i csv filen
    while fortsett == True:
        with open(filnavn, 'a') as csv_file:
            skriver = csv.DictWriter(csv_file, fieldnames=fieldnames)
            data = {
                "tid": datetime.now(),
                "spenning": inngangs_spenning.read(number_of_samples_per_channel=1)[0]
            }
            skriver.writerow(data)
            print(
                "bare hold ctrl og trykk lenken pls: https://www.youtube.com/watch?v=crUQ2rAk5AE&ab_channel=vinii_35i", data)

    # slutter kommunikajson med mydqa
    inngangs_spenning.close()


read_voltage()
