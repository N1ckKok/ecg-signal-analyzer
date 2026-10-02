import matplotlib.pyplot as plt 
from load_data import load_ecg


time, signal , fs = load_ecg(10)
print("time: from", time.min(), "to" , time.max())
print("signal: from", signal.min(), "to", signal.max())

plt.plot(time , signal)
plt.xlabel("TIME (s)")
plt.ylabel("VOLTAGE (mV)")
plt.title("ECG Signal")
plt.savefig("results/ecg_plot.png")
plt.show()
