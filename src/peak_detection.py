from scipy.signal import find_peaks


def detect_peaks(signal, fs):
    if abs(signal.min()) > abs(signal.max()):
        signal = -signal                  

    mindistance = int(0.3 * fs)
    height = 0.5 * (signal.max() - signal.min()) + signal.min()

    peaks, _ = find_peaks(signal, height=height, distance=mindistance)
    return peaks