import matplotlib.pyplot as plt
from numpy.fft import rfft, irfft
import wave
import numpy as np
import os
# from Hlib import read_wav, save_wav, create_signal


def read_wav(path): # returns signal & fps
  wav = wave.open(path , 'r')
  signal = np.fromstring(wav.readframes(-1) , np.int16)
  fps = wav.getframerate()
  return signal, fps



path = 'FT_plots/'
os.makedirs(path, exist_ok=True)

filenames = os.listdir()

print(filenames)

filenames = [fn for fn in filenames if '.wav' in fn]
names = []
for filename in filenames:
  names.append(filename.replace('.wav', ''))

lower_freq = 440 - 40
upper_freq = 440 + 40

for name in names:
  s, fps = read_wav(name + '.wav')
  n = s.shape[0]
  local_lower_freq = int(round(lower_freq / fps * n))
  local_upper_freq = int(round(upper_freq / fps * n))
  FT = rfft(s) * 2 / n
  summ = np.sum(np.abs(FT))
  FT = FT[local_lower_freq + 1 : local_upper_freq]

  
  Y_pwr = np.abs(FT)
  X = np.linspace(lower_freq, upper_freq, Y_pwr.shape[0])
  M = np.max(Y_pwr)

  Y_real = FT.real / M
  Y_imag = FT.imag / M
  Y_pwr = Y_pwr / M


  fig = plt.figure(1)
  fig.set_size_inches((n / 50) / fig.dpi, 1200 / fig.dpi)  
  print('01')
  plt.subplot(311)
  lbl = 'Max(|F|) =' + str(M) + '  Sum(|F|) =' + str(summ)
  if upper_freq - lower_freq <= 100: 
    plt.stem(X, Y_pwr, '0.3', label=lbl, markerfmt='k.', basefmt='k')
  else:
    plt.plot(X, Y_pwr, '0.3', label=lbl, linewidth=.5)
  plt.legend()
  plt.ylabel('Power', fontsize=14, color='k')
  plt.axis([lower_freq, upper_freq, 0, 1.05 ])

  print('02')
  plt.subplot(312)
  if upper_freq - lower_freq <= 100: 
    plt.stem(X, Y_real, '0.3', linewidth=.5, markerfmt='k.', basefmt='k')
  else:
    plt.plot(X, Y_real, '0.3', linewidth=.5)
  plt.ylabel('Real', fontsize=14, color='k')
  plt.axis([lower_freq, upper_freq,-1.01, 1.01 ])


  print('03')
  plt.subplot(313)
  if upper_freq - lower_freq <= 100: 
    plt.stem(X, Y_imag, '0.3', linewidth=.5, markerfmt='k.', basefmt='k')
  else:
    plt.plot(X, Y_imag, '0.3', linewidth=.5)
  plt.ylabel('Imaginary', fontsize=14, color='k')
  plt.axis([lower_freq, upper_freq,-1.01, 1.01 ])


  
  plt.savefig(
    path + name.replace('.wav','.png'),
    frameon=False,
    transparent=True,
    bbox_inches="tight",
    pad_inches=0
    )

  plt.close('all')







