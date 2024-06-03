import numpy as np
from scipy import signal
import librosa
import soundfile as sf

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

# Load audio file using librosa
audio, fs = librosa.load('input_audio_hp.wav', sr=None, mono=False)

# Define filter parameters
cutoff_frequency = 1000  # 1000 Hz cutoff frequency
order = 5  # Order of the filter

# If the audio is stereo, separate the channels
if audio.ndim == 2:
    audio_left = audio[0, :]
    audio_right = audio[1, :]
    
    # Apply high-pass filter to both channels
    filtered_audio_left = butter_highpass_filter(audio_left, cutoff_frequency, fs, order)
    filtered_audio_right = butter_highpass_filter(audio_right, cutoff_frequency, fs, order)
    
    # Combine the filtered channels
    filtered_audio = np.vstack((filtered_audio_left, filtered_audio_right))
else:
    # If the audio is mono, just filter it
    filtered_audio = butter_highpass_filter(audio, cutoff_frequency, fs, order)

# Save filtered audio to a new file using soundfile
sf.write('filtered_audio_hp.wav', filtered_audio.T, fs)
