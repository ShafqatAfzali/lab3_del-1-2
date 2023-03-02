import nidaqmx
from nidaqmx import constants
from nidaqmx import stream_readers
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

MYDAQ = "myDAQ2"
CHANNEl = "ai0"
fs = 10000
DAQ_TIME = 0.3
PLOT_TIME = 0.3
NUMOFSAMPLES = int(DAQ_TIME*fs)
BUFFERSIZE = NUMOFSAMPLES
NUMOFSAMPLESPLOT = int(PLOT_TIME*fs)

with nidaqmx.Task() as readTask:
    readTask._ai_channels.add_ai_voltage_chan(
        physical_channel=MYDAQ+"/"+CHANNEl)
    readTask.timing.cfg_samp_clk_timing(
        rate=fs, sample_mode=constants.AcquisitionType.CONTINUOUS, samps_per_chan=BUFFERSIZE)
    reader = stream_readers.AnalogMultiChannelReader(readTask.in_stream)

    measure = np.zeros([1, NUMOFSAMPLES])
    readTask.start()
    reader.read_many_sample(
        data=measure, number_of_samples_per_channel=NUMOFSAMPLES, timeout=-1)

    balanced_signal = measure[0]-np.mean(measure[0])
    measuretime = np.linspace(0, NUMOFSAMPLES/fs, NUMOFSAMPLES)

    cubic_inter = interp1d(measuretime, balanced_signal, kind="cubic")
    interpolate_time = np.linspace(0, NUMOFSAMPLES/fs, NUMOFSAMPLES)
    cuic_sample = interp1d(interpolate_time)

    start = 0
    end = NUMOFSAMPLESPLOT

    if end > NUMOFSAMPLES:
        end = NUMOFSAMPLES
        plt.plot(measuretime[start:end], balanced_signal[start:end],
                 ".", ms=6, label="samplinger")
        plt.plot(interpolate_time[start*10:end*10],
                 cubic_inter[start*10:end*10], label="cubic interpolation")
        plt.xlabel("tid")
        plt.ylabel("amplitude")
        plt.legend(loc="upper right")
        plt.grid()
        plt.show()
