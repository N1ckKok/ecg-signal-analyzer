import matplotlib.pyplot as plt 
from peak_detection import detect_peaks
from load_data import load_ecg
from filtering import bandpass_filter
from heart_rate import calculate_heart_rate




time, signal , fs = load_ecg(10)
filtered = bandpass_filter(signal, fs)
peaks = detect_peaks(filtered, fs)
bpm = calculate_heart_rate(peaks, fs)
print ("Estimated heart rate:", round(bpm, 1), "bpm")
print("beats found:", len(peaks)) 
print("time: from", time.min(), "to" , time.max())
print("signal: from", signal.min(), "to", signal.max())

plt.plot(time , signal, label="raw", alpha=0.5)
plt.plot(time, filtered, label="filtered")
plt.title(f"ECG Signal - {bpm: .0f} bpm (educational, not diagnostic)")
plt.xlabel("TIME (s)")
plt.ylabel("VOLTAGE (mV)")
plt.title("ECG Signal")
plt.plot(time[peaks],filtered[peaks], "ro", label="peaks")
plt.legend()
plt.savefig("results/ecg_plot.png")
plt.show()
