import pyaudio
import keyboard
import numpy as np
from scipy import signal
from scipy.fft import fft, fftfreq, rfftfreq
import time
import process

chunk_size = 1024  # number of audio samples per buffer
sample_rate = 44100  # number of samples per second
FORMAT = pyaudio.paInt16
CHANNELS = 1

audio = pyaudio.PyAudio()

# open microphone stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

# loop through stream and process audio in chunks
onString = False
while True:
    stringPluck = input("Enter a String: E2, A, D, G, B, E4")
    if stringPluck == "E2" or stringPluck == "A" or stringPluck == "D" or stringPluck == "G" or stringPluck == "B" or stringPluck == "E4":
        onString = True
    else:
        print("Enter an allowed string")
    print("(Listening for sound)")
    while onString:
        frames = []

        #get audio data in a range of 5 seconds
        for i in range(0, int(sample_rate / chunk_size * 3)):
            if keyboard.is_pressed('q'):
                onString = False
                break
            data = stream.read(chunk_size)
            frames.append(data)

        if not onString:
            print("Quit!")
            break

        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        window = signal.hamming(len(audio_data))
        windowed_audio = audio_data * window
        normalized_audio = windowed_audio / np.max(window)

        #convert audio data to frequency
        fft_data = fft(normalized_audio)

        #list of frequencies
        freqs = fftfreq(len(fft_data)) * sample_rate

        #find most common frequency in list
        idx = np.argmax(np.abs(fft_data))
        freq = freqs[idx]

        print("Current frequency for string " + stringPluck + ": " + str(int(freq)) + "hz")
        eval("process." + stringPluck + '("' + str(int(freq)) + '")')


# close stream and terminate PyAudio
print("recording done")
stream.stop_stream()
stream.close()
audio.terminate()
