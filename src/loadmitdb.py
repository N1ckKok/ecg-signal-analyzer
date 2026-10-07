import numpy as np
import wfdb

def loadmitdb(record_name="100", seconds=10):
  
    fs = 360
    n_samples = seconds * fs
    record = wfdb.rdrecord(record_name, pn_dir="mitdb", sampto=n_samples)
    annotation = wfdb.rdann(record_name, "atr", pn_dir="mitdb", sampto=n_samples)
    signal = record.p_signal[:, 0]
    time = np.arange(n_samples) / fs 

    beat_symbols = set("NLRBAaJSVrFejnE/fQ?")
    true_peaks = [s for s, sym in zip(annotation.sample, annotation.symbol) if sym in beat_symbols]
    true_peaks = np.array(true_peaks)

    return time, signal, fs, true_peaks