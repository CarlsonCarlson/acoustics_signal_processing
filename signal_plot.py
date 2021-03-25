import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import wave


def main():
    print("hello world")
    sound = wave.open("Bird Call.wav", "r")

    # Extract Raw Audio from Wav File
    signal = sound.readframes(-1)
    signal = np.fromstring(signal, "Int16")

    plt.plot(signal)
    plt.show()


if __name__ == '__main__':
    main()
