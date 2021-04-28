import matplotlib.pyplot as plot
import numpy as np
from scipy.io import wavfile
import wave
from scipy.fft import fft, fftfreq


def get_info(filename: str) -> dict:
    sound = wave.open(filename, "r")
    # Don't know what this is but it said 2
    # print("sample width in bytes:")
    # print(sound.getsampwidth())
    # Duration in seconds
    duration = sound.getnframes() / sound.getsampwidth()
    info_dict = {
        # 1 is mono 2 is stereo
        "num_channels": sound.getnchannels(),
        "sampling_freq": sound.getframerate(),
        "total_signals": sound.getnframes(),
        "duration": duration
    }
    return info_dict


def main():
    # filename = "Bird Call.wav"
    filename = "Whistling_tones.wav"
    # filename = "high_low_screaming.wav"
    filename = "Frog Resonance.wav"
    info_dict = get_info(filename)
    # NOTES: Geophysical time is real time Tg (22 secs)
    # Arrival time

    # Used this website
    # https://pythontic.com/visualization/signals/spectrogram

    # Using scipy package instead of wave
    sampling_frequency, signal_data = wavfile.read(filename)  # creates a vector with the frequency in 0,
    # and the array of signals in [1]

    # Plot the signal read from wav file

    plot.subplot(211)  # tall enough for 2, wide enough for 1, plot #1
    plot.title("Spectrogram of " + filename.replace(".wav", ""))
    plot.plot(signal_data)
    plot.xlabel('Sample')
    plot.ylabel('Amplitude')

    plot.subplot(212)  # tall enough for 2, wide enough for 1, plot #2
    spectrogram = plot.specgram(signal_data, Fs=sampling_frequency)
    plot.xlabel('Time (s)')
    plot.ylabel('Frequency (Hz)')
    plot.ylim(0, 5000)  # Make frequency range from 0-5000khz
    # colormap = plot.get_cmap("viridis")
    # colormap.set_under(color='k', alpha=None)
    # plot.colorbar(spectrogram)
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

    # TODO: Have a legend that says the amplitude of the signal. Yellow is loudest, green is lowest. (in decibels)
    # ^ is gonna need more time, is it actually important though
    # More than one frequency is a broadband signal while a single frequency is just one signal

    # TODO: learn about fourier transforms
    # https://www.youtube.com/watch?v=spUNpyF58BY

    print(info_dict["total_signals"])
    number_of_samples = info_dict["total_signals"]
    # fftfreq() calculates the frequencies in the center of each bin in the output of fft(). Without this,
    # there would be no way to plot the x-axis on your frequency spectrum.
    x_fourier = fftfreq(number_of_samples, 1 / sampling_frequency)
    y_fourier = fft(signal_data)
    plot.plot(np.abs(x_fourier), np.abs(y_fourier))
    # // rounds the divided number to the nearest whole number
    plot.xlabel("Frequency (Hz)")
    plot.ylabel("Amplitude")
    plot.show()

    # TODO: make a clap signal and look at it in the fourier transform graph, not the spectrogram graph
    # TODO: find what is power spectral density with the fourier transform

    # Taking out the motorcycle sound
    # TODO: make vector with length equal to total number of signals
    # TODO: make index 0-2000 in the vector equal to 0, and the rest 1s
    # TODO: multiply the signal data by the vector
    # TODO: use inverse fft on the resultant vector
    # TODO: turn the new signal data into a new cleaned up wav file

    # Decibels are
    # reference pressure is usually 20 micropascal/Hz in air
    # the reference pressure(p0) is divided by freq so that the pressure is standard at all frequency
    # Decibels = log10(pressure / reference pressure)

    # Convolution or match filter
    # replica correlation
    # multiplying the sound by itself

    # TODO: make the fourier transform run in real time
    # TODO: Take in real time sound and output real time graph

    # Resonance
    # When frequencies resonate, the amplitudes reach their highest signal to noise ratio
    # The longer the tube (saxophone) the higher the resonance frequency
    # Every object has multiple resonance frequencies called modes
    # 3 standing waves mean its at the mode 3 frequency
    # Helmholtz resonator


if __name__ == '__main__':
    main()
