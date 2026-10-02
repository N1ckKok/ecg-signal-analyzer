import matplotlib.pyplot as plt 
from peak_detection import detect_peaks
from load_data import load_ecg
from filtering import bandpass_filter



time, signal , fs = load_ecg(10)
filtered = bandpass_filter(signal, fs)
peaks = detect_peaks(filtered, fs)
print("beats found:", len(peaks)) 
print("time: from", time.min(), "to" , time.max())
print("signal: from", signal.min(), "to", signal.max())

plt.plot(time , signal, label="raw", alpha=0.5)
plt.plot(time, filtered, label="filtered")
plt.xlabel("TIME (s)")
plt.ylabel("VOLTAGE (mV)")
plt.title("ECG Signal")
plt.plot(time[peaks],filtered[peaks], "ro", label="peaks")
plt.legend()
plt.savefig("results/ecg_plot.png")
plt.show()
