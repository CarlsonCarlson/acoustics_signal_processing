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
    # sampling_frequency, signal_data = wavfile.read('Bird Call.wav')  # creates a vector with the frequency in 0,
    # sampling_frequency, signal_data = wavfile.read('Whistling_tones.wav')
    sampling_frequency, signal_data = wavfile.read('high_low_screaming.wav')
    # and the array of signals in [1]

    print(sampling_frequency)
    print(signal_data)

    # Plot the signal read from wav file

    plot.subplot(211)  # tall enough for 2, wide enough for 1, plot #1
    # plot.title("Spectrogram of a Bird's Call")
    # plot.title("Spectrogram of Whistling Tones")
    plot.title("Spectrogram of Carlson Screaming")
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
    # find out the units of Force, Power, pressure, energy, work, and intensity. And what they are. (done)

    # Force: Newtons (equal to force required to make 1kg of mass an acceleration of 1m/s^2
    # Power: Watts (work(Joules) / time(second))
    # Pressure: Pascals (N/m^2)
    # Energy: Joules (the ability of something to do work)
    # Work: Joules (Force*Distance)
    # Intensity: Power per Area (W/m^2)

    # Sound moves faster in denser mediums because there's less space between the molecules.
    # a time series is a series of signals
    # fourier discovered that any time series can be decomposed into a bunch of sin and cos time series'
    # fourier coefficients are the coeffecients a,b,c in a*sin() + b*cos()
    # you can go between time and frequency domains with the fourier transform

    # TODO: make the program able to file select at the top, instead of commenting
    # TODO: make the frequency range from 0 to 5000khz
    # TODO: Have a legend that says the amplitude of the signal. Yellow is loudest, green is lowest. (in decibels)
    # TODO: what is the difference between single frequency vs broadband signals

    # TODO: learn about fourier transforms

    # TODO: make fast fourier transform of my 3 signals, not spectrogram

    # TODO: make a clap signal and look at it in the fourier transform graph, not the spectrogram graph
    # TODO: find what is power spectral density with the fourier transform


if __name__ == '__main__':
    main()
