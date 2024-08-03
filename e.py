import numpy as np
import matplotlib.pyplot as plt

def analyze_signal_fft(f1, f2, fs, duration):
    """
    Analyze the frequency components of a signal s(t) = sin(2πf1t) + sin(2πf2t)
    using Fast Fourier Transform (FFT).

    Parameters:
    f1 (float): Frequency of the first sine component in Hz
    f2 (float): Frequency of the second sine component in Hz
    fs (float): Sampling frequency in Hz
    duration (float): Duration of the signal in seconds

    Returns:
    None (displays plots)
    """
    # Generate time array
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)

    # Generate the signal
    s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

    # Compute the FFT
    fft_result = np.fft.fft(s)
    
    # Compute the frequency array
    freqs = np.fft.fftfreq(len(t), 1/fs)

    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(fft_result)

    # Plot the original signal
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 1, 1)
    plt.plot(t, s)
    plt.title('Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Plot the magnitude spectrum
    plt.subplot(3, 1, 2)
    plt.plot(freqs[:len(freqs)//2], magnitude_spectrum[:len(freqs)//2])
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')

    # Plot the magnitude spectrum (zoomed)
    plt.subplot(3, 1, 3)
    plt.plot(freqs[:len(freqs)//2], magnitude_spectrum[:len(freqs)//2])
    plt.title('Magnitude Spectrum (Zoomed)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.xlim(0, max(f1, f2) * 1.5)

    plt.tight_layout()
    plt.show()

    # Print the detected frequency components
    threshold = 0.1 * np.max(magnitude_spectrum)
    detected_freqs = freqs[magnitude_spectrum > threshold]
    detected_freqs = detected_freqs[detected_freqs > 0]
    print("Detected frequency components:")
    for freq in detected_freqs:
        print(f"{freq:.2f} Hz")

# Analyze the signal
analyze_signal_fft(f1=50, f2=120, fs=1000, duration=1)