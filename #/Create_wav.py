import wave
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft

def create_signal(N, fps, real_frequency, phase = 0, amplitude = 1, decay = 0):
  frequency = real_frequency * N / fps
  f = lambda x: amplitude * np.exp(-decay * x) * np.cos(phase + 2 * np.pi * frequency * x / N)
  X = np.arange(0,N,1)
  return f(X)

f = 1000
p = 0
a = 1
d = 0.0


w1 = create_signal(1000, 44100, 100, 0, 1, 0)
fig = plt.figure()
fig.set_size_inches(8, 2)
plt.axis([0, 1000,-2, 2])
plt.plot(w1, 'k')
plt.axis('off')
plt.savefig(
  '01.png',
  frameon=False,
  transparent=True,
  bbox_inches="tight",
  pad_inches=0
  )
plt.close()


w2 = create_signal(1000, 44100, 800, 1.9, .5, 0)
fig = plt.figure()
fig.set_size_inches(8, 2)
plt.axis([0, 1000,-2, 2])
plt.plot(w2, 'k')
plt.axis('off')
plt.savefig(
  '02.png',
  frameon=False,
  transparent=True,
  bbox_inches="tight",
  pad_inches=0
  )
plt.close()

w3 = create_signal(1000, 44100, 500, 0.9, .3, 0)
fig = plt.figure()
fig.set_size_inches(8, 2)
plt.axis([0, 1000,-2, 2])
plt.plot(w3, 'k')
plt.axis('off')
plt.savefig(
  '03.png',
  frameon=False,
  transparent=True,
  bbox_inches="tight",
  pad_inches=0
  )
plt.close()

fig = plt.figure()
fig.set_size_inches(8, 2)
plt.axis([0, 1000,-2, 2])
plt.plot(w1 + w2 + w3, 'k')
plt.axis('off')
plt.savefig(
  'sum.png',
  frameon=False,
  transparent=True,
  bbox_inches="tight",
  pad_inches=0
  )
plt.close()

FT = np.abs(rfft(w1 + w2 + w3) * 2 / 1000)
fig = plt.figure()
fig.set_size_inches(8, 2)
plt.axis([0, 20, 0, 1])
plt.plot(FT, 'k')
plt.axis('off')
plt.savefig(
  'transf.png',
  frameon=False,
  transparent=True,
  bbox_inches="tight",
  pad_inches=0
  )
plt.close()