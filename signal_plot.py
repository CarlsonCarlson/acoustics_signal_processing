import matplotlib.pyplot as plot
import numpy as np
import scipy.io.wavfile
from scipy.io import wavfile
import wave
from scipy.fft import fft, fftfreq, ifft


# To convert the file from m4a to wav I use the audioconverter package
# Sample command line
# audioconvert convert input_dir/ output_dir/ --output-format .mp3


def get_info(filename: str) -> dict:
    sound = wave.open(filename, "r")
    # Don't know what this is but it said 2
    # print("sample width in bytes:")
    # print(sound.getsampwidth())
    # Duration in seconds
    duration = sound.getnframes() / sound.getframerate()
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
    # filename = "Whistling_tones.wav"
    # filename = "high_low_screaming.wav"
    filename = "Clap sounds.wav"
    # filename = "Frog Resonance.wav"
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

    plot.xlabel('Time (seconds)')
    plot.ylabel('Amplitude')
    print(info_dict["total_signals"])
    print(info_dict["sampling_freq"])
    print(info_dict["duration"])

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

    # More than one frequency is a broadband signal while a single frequency is just one signal

    print(info_dict["total_signals"])
    number_of_samples = info_dict["total_signals"]
    # fftfreq() calculates the frequencies in the center of each bin in the output of fft(). Without this,
    # there would be no way to plot the x-axis on your frequency spectrum.
    x_fourier = fftfreq(number_of_samples, 1 / sampling_frequency)
    y_fourier = fft(signal_data)
    plot.plot(np.abs(x_fourier), np.abs(y_fourier))
    # // rounds the divided number to the nearest whole number
    plot.xlabel("Frequency (Hz)")
    plot.ylabel("Amplitude^2")
    plot.show()

    # the fourier transform is nothing but an integral of the frequency domain
    # the result of a fourier transform is the power spectral density with axes frequency vs amplitude^2
    # power spectral density is a function that tells you how much energy is in the signal
    # then by squaring the amplitude of the normal amplitude vs time signal data you can combine it with the PSD
    # a spectrogram is a 3d function equal time, frequency, energy (amplitude^2)
    #
    # The power spectral density (PSD) of the signal describes the power present in the signal as a function of
    # frequency, per unit frequency. Power spectral density is commonly expressed in watts per hertz (W/Hz).

    # Taking out the motorcycle sound
    # this makes a (10,0) array of zeroes
    # zeros_array = np.zeros(10)
    # print(zeros_array)
    # print(zeros_array.shape)

    # this creates an array of 1s that is (5,10)
    # so a list of 5 elements, each element is a list of 10 1s
    # example_ones_array = np.ones(5,10)
    # print(example_ones_array)
    # print(example_ones_array.shape)

    # ones_array = np.ones(5)
    # print("")
    # combined_array = np.concatenate((zeros_array, ones_array))
    # print(combined_array)

    filter_array = np.ones(info_dict["total_signals"])
    np.put(filter_array, np.arange(0, 2000), [0])
    cleaned_data = y_fourier * filter_array
    print(cleaned_data)

    plot.plot(np.abs(x_fourier), np.abs(cleaned_data))
    # // rounds the divided number to the nearest whole number
    plot.xlabel("Frequency (Hz)")
    plot.ylabel("Amplitude^2")
    plot.show()

    # changing back to time domain so we can write the wav file
    time_cleaned_data = ifft(cleaned_data)
    print(time_cleaned_data)

    plot.specgram(signal_data, Fs=sampling_frequency)
    plot.xlabel('Time (s)')
    plot.ylabel('Frequency (Hz)')
    plot.ylim(0, 5000)  # Make frequency range from 0-5000khz
    # colormap = plot.get_cmap("viridis")
    # colormap.set_under(color='k', alpha=None)
    # plot.colorbar(spectrogram)
    plot.show()

    converted_time_cleaned_data = cleaned_data.astype(dtype="float32")
    scipy.io.wavfile.write("filtered_audio.wav", info_dict["sampling_freq"], converted_time_cleaned_data)
    # that did not work, but I'm not sure why

    # Decibels are
    # reference pressure is usually 20 micropascal/Hz in air
    # the reference pressure(p0) is divided by freq so that the pressure is standard at all frequency
    # Decibels = 10 * log10(pressure / reference pressure)
    # pressure^2 = intensity
    # Decibel is 20 * log10(pressure)

    # Convolution or match filter
    # replica correlation
    # multiplying the sound by itself


    # Resonance
    # When frequencies resonate, the amplitudes reach their highest signal to noise ratio
    # The longer the tube (saxophone) the higher the resonance frequency
    # Every object has multiple resonance frequencies called modes
    # 3 standing waves mean its at the mode 3 frequency
    # Helmholtz resonator whirrs when you blow into the opening from a certain angle
    #
    # 3 mediums in sound
    # source (generator), medium (propagation), receiver
    #
    # cos function is just a normal
    # integrating from 0 to 2 pi of cos is equal to pressure^2 which equals intensity


if __name__ == '__main__':
    main()
