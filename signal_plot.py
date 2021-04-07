import matplotlib.pyplot as plot
import numpy as np
from scipy.io import wavfile
import wave


def main():
    sound = wave.open("Bird Call.wav", "r")
    sampling_rate = 48000
    Tg = 1000000000 / sampling_rate

    # NOTES: Geophysical time is real time Tg (22 secs)
    # Arrival time

    # Find what stuff does
    print("get n channels (1 is mono 2 is stereo:")
    print(sound.getnchannels())
    print("sample width in bytes:")
    print(sound.getsampwidth())
    print("sampling frequency:")
    print(sound.getframerate())
    print("number of audio frames:")
    print(sound.getnframes())

    # Used this website
    # https://pythontic.com/visualization/signals/spectrogram

    # Using scipy package instead of wave
    sampling_frequency, signal_data = wavfile.read('Bird Call.wav')  # creates a vector with the frequency in 0,
    # and the array of signals in [1]

    print(sampling_frequency)
    print(signal_data)

    # Plot the signal read from wav file

    plot.subplot(211)  # tall enough for 2, wide enough for 1, plot #1
    plot.title("Spectogram of a Bird's Call")
    plot.plot(signal_data)
    plot.xlabel('Sample')
    plot.ylabel('Amplitude')

    plot.subplot(212)  # tall enough for 2, wide enough for 1, plot #2
    plot.specgram(signal_data, Fs=sampling_frequency)
    plot.xlabel('Time')
    plot.ylabel('Frequency')
    plot.show()

    # Nyquist frequency is the minimum sampling frequency to resolve the waveform
    # The sampling rate must be at least twice the desired highest frequency.
    # The human ear can hear from 20 hertz to 20 kilohertz, realistically up to 16khz

    # as you go further from the source the amplitude goes down by 1/r^2, where r is the "range"
    # (distance in spherical). amplitude measured in pressure (pascals) (force/area).
    # Energy is the integral of amplitude in time.
    # TODO: find out the units of Force, Power, pressure, energy, work, and intensity. And what they are.
    # TODO: learn about fourier transforms
    # TODO: whistle and hum to make different signals and look at them in the frequency domain
    # TODO: make high and low frequencies and see how they look

if __name__ == '__main__':
    main()
