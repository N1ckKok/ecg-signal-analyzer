import numpy as np
from scipy.datasets import electrocardiogram



def load_ecg(seconds=10):
    ecg = electrocardiogram() 
    fs = 360

    n_samples= seconds * fs 
    signal = ecg[0:n_samples]
    time = np.arange(n_samples) / fs
    return time, signal, fs
