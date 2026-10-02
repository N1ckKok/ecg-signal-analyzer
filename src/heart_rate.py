import numpy as np

def  calculate_heart_rate(peaks, fs):
    rr_samples = np.diff(peaks)
    rr_seconds = rr_samples / fs 
    mean_rr = np.mean(rr_seconds)
    bpm = 60 / mean_rr
    return bpm
