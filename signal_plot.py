import matplotlib.pyplot as plot
import numpy as np
from scipy.io import wavfile
import wave


def main():
    sound = wave.open("Bird Call.wav", "r")
    # Extract Raw Audio from Wav File
    # signal = sound.readframes(-1)
    # signal = np.fromstring(signal, "Int16")
    sampling_rate = 48000
    Tg = 1000000000 / sampling_rate

    # TODO: make time axis sub divide into 22 secs
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

    # Using scipy.io to import wav file

    # TODO: find a good python library for manipulating and processing sound
    # https://pythontic.com/visualization/signals/spectrogram
    # TODO: get the two graphs in example 2

    sampling_frequency = 48000
    # signal_data = wavfile.read('Bird Call.wav')
    signalData = wave.open("Bird Call.wav", "r")

    # Plot the signal read from wav file

    plot.subplot(211)

    plot.title('Spectrogram of a wav file with piano music')

    plot.plot(signalData)

    plot.xlabel('Sample')

    plot.ylabel('Amplitude')

    plot.subplot(212)

    plot.specgram(signalData, Fs=samplingFrequency)

    plot.xlabel('Time')

    plot.ylabel('Frequency')

    plot.show()


if __name__ == '__main__':
    main()
