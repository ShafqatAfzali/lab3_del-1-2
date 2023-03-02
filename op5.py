import pyvas as pv
# from pyvisa.highlevel import ResourceManager as RM
# import visa as pv
from datetime import datetime
# print(dir(pv))

# gir en lliste over funksjoner som kan kommunisere og printe
rm = pv.ResourceManager()
l = rm.list_resourses()
print(l)


keithley = rm.open_resource(l[0])
# måler resistans med MEAS.RES, kan bruke flere kode_ord til å lese andre egenskaper
value = float(keithley.query("MEAS:RES?"))

# tidblir gitt en variabel
timestamp = datetime.now()

# printer tid og resistans(5 siffer før og 3 etter komma)/(spenning/etc om det ble valgt i linje 19)
print("%s - termistor motstand: %5.3f ohm" % (timestamp.time(), value))
rm.close()
