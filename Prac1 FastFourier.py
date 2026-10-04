import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
signal = np.sin(2*np.pi*5*t) + 0.5*np.random.randn(1000)

fft = np.fft.fft(signal)

plt.subplot(2,1,1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (s)")

plt.subplot(2,1,2)
plt.plot(abs(fft))
plt.title("FFT (Magnitude)")
plt.xlabel("Frequency (Hz)")

plt.show()