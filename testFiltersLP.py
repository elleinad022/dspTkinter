import numpy as np
from scipy.signal import butter, lfilter, freqz
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def apply_lp_filter(file_Input_lp):
    # Load audio file using librosa
    audio, fs = librosa.load(file_Input_lp, sr=None, mono=False)

    # Filter parameters
    order = 5
    cutoff_frequency = 3000  # 3000 Hz cutoff frequency
    


    # Get the filter coefficients
    b, a = butter_lowpass(cutoff_frequency, fs, order)

    # Compute frequency response
    w, h = freqz(b, a, fs=fs)

    # Apply low-pass filter
    if audio.ndim == 2:
        # Handle stereo audio
        audio_left = audio[0, :]
        audio_right = audio[1, :]
        filtered_audio_left = butter_lowpass_filter(audio_left, cutoff_frequency, fs, order)
        filtered_audio_right = butter_lowpass_filter(audio_right, cutoff_frequency, fs, order)
        filtered_audio = np.vstack((filtered_audio_left, filtered_audio_right))
    else:
        # Handle mono audio
        filtered_audio = butter_lowpass_filter(audio, cutoff_frequency, fs, order)

    # Save filtered audio to a new file
    sf.write('filtered_audio_lp.wav', filtered_audio.T, fs)


# Plot the frequency response with a logarithmic scale
def plot_lpfilter_response(cutoff_lp, file_input_lp, order=5):
    audio, fs = librosa.load(file_input_lp, sr=None, mono=False)
    b, a = butter_lowpass(cutoff_lp, fs, order=order)
    w, h = freqz(b, a, worN=8000)
    plt.figure(figsize=(12, 6))
    plt.plot(0.5 * fs * w / np.pi, 20 * np.log10(np.abs(h)), 'b')  # Convert amplitude to dB
    plt.plot(cutoff_lp, -3, 'ko')  # Mark -3 dB point
    plt.axvline(cutoff_lp, color='k', linestyle='--')
    plt.xlim(0, 0.5 * fs)
    plt.title("Low-Pass Filter Frequency Response")
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Gain [dB]')
    plt.grid()
    plt.show()



