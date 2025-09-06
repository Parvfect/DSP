
from scipy.signal import butter, filtfilt, savgol_filter
import numpy as np


def clean_signal(signal, fs=4000, cutoff=20):
    b, a = butter(2, cutoff/(0.5*fs), btype='high') # high pass filter
    signal = filtfilt(b, a, signal) # digital filter
    signal = savgol_filter(signal, window_length=11, polyorder=3) # smoothing
    return(signal - np.mean(signal)) / np.std(signal) # norming


def cross_correlation_fft(x, y):
    # Ensure equal length
    n = len(x) + len(y) - 1
    n_padded = 1 << (n - 1).bit_length()  # next power of 2 for efficiency
    
    # FFT of both signals
    X = np.fft.fft(x, n_padded)
    Y = np.fft.fft(y, n_padded)
    
    # Multiply X with conjugate of Y
    corr = np.fft.ifft(X * np.conj(Y))
    
    # Only the real part is meaningful
    return np.real(corr)