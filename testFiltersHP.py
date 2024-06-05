import numpy as np
from scipy import signal
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def plot_hpfilter_response(cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    w, h = signal.freqz(b, a, worN=8000)
    plt.figure(figsize=(12, 6))
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.plot(cutoff, 0.5 * np.sqrt(2), 'ko')
    plt.axvline(cutoff, color='k', linestyle='--')
    plt.xlim(0, 0.5 * fs)
    plt.title("High-Pass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain')
    plt.grid()
    plt.show()

cutoff_frequency = 1000  # 1000 Hz cutoff frequency
order = 5  # Order of the filter

# Load audio file using librosa
 
    

def apply_hp_filter(fileinput):
    audio, fs = librosa.load(fileinput, sr=None, mono=False)
    if audio.ndim == 2:
        # Handle stereo audio
        audio_left = audio[0, :]
        audio_right = audio[1, :]
        filtered_audio_left = butter_highpass_filter(audio_left, cutoff_frequency, fs, order)
        filtered_audio_right = butter_highpass_filter(audio_right, cutoff_frequency, fs, order)
        filtered_audio = np.vstack((filtered_audio_left, filtered_audio_right))
    else:
        # Handle mono audio
        filtered_audio = butter_highpass_filter(audio, cutoff_frequency, fs, order)

    # Save filtered audio to a new file
    sf.write('filtered_audio_hp.wav', filtered_audio.T, fs)
    
    

# Plot the frequency response of the filter

