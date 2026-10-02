from scipy.signal import find_peaks


def detect_peaks(signal, fs):
    min_distance = int(0.3 * fs)
    height = 0.5 * (signal.max() - signal.min()) + signal.min()


    peaks, _ = find_peaks(signal, height=height, distance=min_distance)
    return peaks
