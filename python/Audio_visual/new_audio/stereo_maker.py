import wave, struct, math, random

sampleRate = 44100.0 # hertz
duration = 1.0 # seconds
freq = 440.0 # hertz
max_amplitude = ((2 ** 8) ** 2) / 2

ampli = lambda x: abs(x * max_amplitude)
def pitch(frequency, amplitude, time):
   """
   0 <= amplitude <= 1
   """
   a = abs(amplitude * max_amplitude)
   return int(a * math.sin(2 * math.pi * frequency * time / sampleRate))

obj = wave.open('sound.wav','w')

nchannels = 2 # mono
sampwidth = 2
framerate = sampleRate
nframes = int(sampleRate * duration)
comptype = "NONE"
compname = "not compressed"
obj.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

audios = []
for i in range(nframes):
   left = int(ampli(16**(-i/sampleRate)) * math.sin(2*math.pi*freq*i/sampleRate))
   right = int(ampli(16**(i/sampleRate-1)) * math.sin(2*math.pi*freq*i/sampleRate))
   audios += [(left,right,),]


for i in range(nframes):
   left, right = audios[i]
   data_l = struct.pack('<h', left)
   obj.writeframesraw(data_l)
   data_r = struct.pack('<h', right)
   obj.writeframesraw(data_r)
obj.close()