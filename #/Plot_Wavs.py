import os
import numpy as np
import matplotlib.pyplot as plt
import wave


def read_wav(path): # returns signal & fps
  wav = wave.open(path , 'r')
  signal = np.fromstring(wav.readframes(-1) , np.int16)
  fps = wav.getframerate()
  return signal, fps

os.makedirs('wav_plots', exist_ok=True)

filenames = os.listdir()

print(filenames)

filenames = [fn for fn in filenames if '.wav' in fn]

print(filenames)

for fn in filenames:
  s, _ = read_wav(fn)
  n = s.shape[0]

  fig = plt.figure()
  print(fig.dpi)
  fig.set_size_inches((n / 20) / fig.dpi, 400 / fig.dpi)

  plt.axis([0, n * 1.01,-1.01, 1.01 ]) 
  
  plt.plot(s / np.max(np.abs(s)), 'k', linewidth=1)
  plt.axis('off')
  plt.savefig(
    'wav_plots/' + fn.replace('.wav','.png'),
    frameon=False,
    transparent=True,
    bbox_inches="tight",
    pad_inches=0
    )
  plt.close()
