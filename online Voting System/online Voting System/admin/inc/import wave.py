import wave
import numpy as np
import matplotlib.pyplot as plt
import pygame
from scipy.signal import spectrogram

def load_audio(audio_file):
    with wave.open(audio_file, 'rb') as audio:
        frames = audio.readframes(-1)
        audio_array = np.frombuffer(frames, dtype=np.int16)
        sample_rate = audio.getframerate()
    return audio_array, sample_rate

def generate_waveform_and_spectrum(audio_array, sample_rate, i):
    # Create a waveform plot
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(audio_array)
    plt.title(f"Person {i+1} Waveform")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")

    # Create a spectrum plot
    plt.subplot(2, 1, 2)
    f, t, Sxx = spectrogram(audio_array, fs=sample_rate)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.title(f"Person {i+1} Spectrum")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="Power/Frequency (dB/Hz)")

    # Display both plots in Jupyter Notebook
    plt.tight_layout()
    plt.show()

def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def main(audio_files):
    for i, audio_file in enumerate(audio_files):
        print(f"Displaying waveform and spectrum for {audio_file}...")
        audio_array, sample_rate = load_audio(audio_file)
        generate_waveform_and_spectrum(audio_array, sample_rate, i)

        # Play the audio
        play_audio(audio_file)

if _name_ == "_main_":
    # List of input audio files with relative or absolute paths
    audio_files = [
        'audio/shreya.wav',
        
        # Add more audio files here
    ]
    
    main(audio_files)