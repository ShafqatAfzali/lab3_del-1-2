# Importerer nødvendige biblioteker
import nidaqmx
from datetime import datetime
# Oppretter konstanter for kommunikasjon med myDAQ
MYDAQ_NAME = 'myDAQ2'
CH_NAME = 'ai0'
# Oppretter en task og forteller at Tasken skal lese inputspenning fra
# myDAQ og kanaler gitt av konstantene
get_ai0_V = nidaqmx.Task()
get_ai0_V.ai_channels.add_ai_voltage_chan(
    physical_channel=MYDAQ_NAME + "/" + CH_NAME)
# Tidsstempler målingen
timestamp = datetime.now()
# read funksjonen returnerer en liste med 1 verdi siden vi kun leser 1 sample
# Vi er dermed kun interessert i verdien på index 0 i listen
value = get_ai0_V.read(number_of_samples_per_channel=1)[0]
# Vi skriver den ut på kommandolinjen med tidsstempel
print("%s - Spenning U_theta: %5.2f Volts" % (timestamp.time(), value))
# Avslutter med å lukke myDAQ ressursen
get_ai0_V.close()
