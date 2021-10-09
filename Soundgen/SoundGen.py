from random import randint
import math
from numpy import arcsin
import os

def generateRandom(duration, sampleRate, amplitude):
    samples = []
    for _ in range(0,duration*sampleRate):
        samples.append(randint(0,amplitude))
    return samples

def generateSin(freq,duration, sampleRate, amplitude):
    samples = []
    b = freq/245
    for s in range(0, duration*sampleRate):
        a = round(((math.sin(b*s*math.pi/180))**2) * amplitude)
        samples.append(a)

    return samples

def generateSquare(freq, duration, sampleRate, amplitude):
    samples = []
    b = freq/245
    for s in range(0, duration*sampleRate):
        a = round((math.sin(b*s*math.pi/180))**2) * amplitude
        samples.append(a)

    return samples

def generateTriangle(freq, duration, sampleRate, amplitude):
    samples = []
    b = freq/245
    for s in range(0,duration*sampleRate):
        a = round(abs(arcsin(math.sin(b*s*math.pi/180))/(math.pi*2)) * amplitude)
        samples.append(a)
    
    return samples
    

def generateSawtooth(freq, duration, sampleRate, amplitude):
    samples = []
    b = sampleRate/amplitude
    c = freq/b
    for s in range(0,duration*sampleRate):
        a = round(s*c) % amplitude
        samples.append(a)

    return samples
    

def save(filename, samples):
    f = open(filename, "wb")
    wavHeaderSize = 16
    bitsPerSample = 8  
    channels = 1
    wavTypeFormat = 1
    sampleFreq = 44100
    dataRate = sampleFreq * bitsPerSample // 8 
    blockAlignment = dataRate * channels
    dataSize = len(samples) * bitsPerSample//8
    fileSize = wavHeaderSize + dataSize
    f.write("RIFF".encode())
    f.write(fileSize.to_bytes(4,'little'))
    f.write("WAVE".encode())
    f.write("fmt ".encode())
    f.write(wavHeaderSize.to_bytes(4,'little'))
    f.write(wavTypeFormat.to_bytes(2,"little"))
    f.write(channels.to_bytes(2, "little"))
    f.write(sampleFreq.to_bytes(4, "little"))
    f.write(dataRate.to_bytes(4,"little"))
    f.write(blockAlignment.to_bytes(2,"little"))
    f.write(bitsPerSample.to_bytes(2, "little"))
    f.write("data".encode())
    f.write(dataSize.to_bytes(4,"little"))
    for sample in samples:
        f.write(sample.to_bytes(bitsPerSample//8,'little'))

    

save(os.path.abspath("sound.wav"),generateSawtooth(440,10, 44100, 255))