import numpy as np
from loadmitdb import loadmitdb
from filtering import bandpass_filter
from peak_detection import detect_peaks


def evaluate_record(record_name, seconds=60):
    time, signal, fs, true_peaks = loadmitdb(record_name, seconds)
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
    return len(true_peaks), len(found_peaks), sensitivity, precision


records = ["100", "101", "105", "108", "203", "207"]

for name in records:
    n_true, n_found, sens, prec = evaluate_record(name)
    print(f"{name}: true={n_true} found={n_found} sens={sens*100:.1f}% prec={prec*100:.1f}%")