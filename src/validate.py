import matplotlib.pyplot as plt
from loadmitdb import loadmitdb

time, signal, fs, true_peaks = loadmitdb("100", 10)
print("annotated beats:", len(true_peaks))
plt.plot(time, signal)
plt.plot(time[true_peaks], signal[true_peaks], "go", label="cardiologist")
plt.legend()
plt.show()
