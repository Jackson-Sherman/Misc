filepath = "/Users/jacksonsherman/Documents/MuseScore3/Scores/Hyrule Field Intro.wav"
while not(filepath):
    filepath = input("Click and drag or manually type file path here: ")

#####
# copied from https://stackoverflow.com/questions/5120555/how-can-i-convert-a-wav-from-stereo-to-mono-in-python#answer-13384150
# posted by user https://stackoverflow.com/users/2908/jiaaro
#####
# from pydub import AudioSegment

# sound = AudioSegment.from_wav(filepath)
# sound = sound.set_channels(2)
# sound.export(filepath, format="wav")
#####
# end copied segment
#####

#####
# copied from https://stackoverflow.com/questions/44787437/how-to-convert-a-wav-file-to-a-spectrogram-in-python3
# posted by user https://stackoverflow.com/users/7919125/tom-wyllie editted by user https://stackoverflow.com/users/997162/emix
#####
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile

sample_rate, samples = wavfile.read(filepath)

###
# <mine>
###

if samples.ndim == 2:
    newlist = []
    for row in samples:
        newlist += [sum([i for i in row]) / len(row)]
    # maxi = max(newlist)
    # mini = min(newlist)
    # newerlist = [(newlist[i] - mini) / (maxi - mini) for i in range(len(newlist))]
    # print(mini, maxi)
    # print(min(newerlist), max(newerlist))
    samples = np.array(newlist)#erlist)
print(sample_rate)
print(samples)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

print("frequencies: count:{0}; min: {1}; max: {2}; full: {3}".format(len(frequencies),np.amin(frequencies),np.amax(frequencies),frequencies))
print("times: {}".format(len(times)))
print("spectrogram: [{}, {}]".format(len(spectrogram),len(spectrogram[0])))
print("OLD: min, max: ({}, {})".format(np.amin(spectrogram), np.amax(spectrogram)))
damax = np.amax(spectrogram)
spectrogram = np.array([[val / damax for val in row] for row in spectrogram])
print("NEW: min, max: ({}, {})".format(np.amin(spectrogram), np.amax(spectrogram)))
from PIL import Image
from matplotlib import cm
im = Image.fromarray(np.uint8(cm.gist_earth(spectrogram)*255))
im.show()
###
# </mine>
###

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
#####
# end copied segment
#####