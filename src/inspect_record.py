import matplotlib.pyplot as plt
from loadmitdb import loadmitdb
from filtering import bandpass_filter
from peak_detection import detect_peaks

record_name = "108"        

time, signal, fs, true_peaks = loadmitdb(record_name, 20)
filtered = bandpass_filter(signal, fs)
found_peaks = detect_peaks(filtered, fs)

plt.plot(time, filtered)
plt.plot(time[true_peaks], filtered[true_peaks], "go", label="Cardiologist")
plt.plot(time[found_peaks], filtered[found_peaks], "rx", label="My detector")
plt.title(f"Record {record_name}")
plt.legend()
plt.show()