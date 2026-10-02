from scipy.signal import butter, filtfilt

def bandpass_filter(signal, fs, low=0.5, high=40, order=3):
    nyquist = 0.5 * fs
    low_norm = low / nyquist
    high_norm = high / nyquist

    b, a = butter(order, [low_norm, high_norm], btype="band")
    return filtfilt(b, a, signal)