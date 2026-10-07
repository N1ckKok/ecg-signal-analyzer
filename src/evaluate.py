import numpy as np
from loadmitdb import loadmitdb
from filtering import bandpass_filter
from peak_detection import detect_peaks

time, signal, fs, true_peaks = loadmitdb("100", 60)   

filtered = bandpass_filter(signal, fs)
found_peaks = detect_peaks(filtered, fs)

tolerance = int(0.1 * fs)     


tp = 0
for beat in true_peaks:
    if np.any(np.abs(found_peaks - beat) <= tolerance):
        tp += 1

fn = len(true_peaks) - tp
fp = len(found_peaks) - tp
sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
precision = tp / (tp + fp) if (tp + fp) > 0 else 0

print("true beats:", len(true_peaks))
print("found:", len(found_peaks))
print("sensitivity:", round(sensitivity * 100, 1), "%")
print("precision:", round(precision * 100, 1), "%")