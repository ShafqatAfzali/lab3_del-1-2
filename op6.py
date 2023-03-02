import pyvas as pv
from datetime import datetime
import numpy as np

b_konstant = 3828
k_konstant = 0.0263

rm = pv.ResourceManager()
l = rm.list_resourses()
print(l)

# velg "m" basert på hvor keithley er i lista "l", dette vil jobbe med keithley utstyret
keithley = rm.open_resource(l[0])
value = float(keithley.query("MEAS:RES?"))


timestamp = datetime.now()

# til celcius istedet for motstands verdi


def R_til_T(verdi):
    temp_cel = b_konstant/np.log(verdi/k_konstant)-273.15
    return temp_cel


value = R_til_T(value)
print("%s - termistor motstand: %5.3f ohm" % (timestamp.time(), value))
rm.close()
