import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import pi
from scipy.fftpack import fft
from scipy.io import wavfile

sample_rate, data = wavfile.read('./input3.wav')
data1=data[:,0]

N = sample_rate//10
p = sample_rate//30

fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(0, 5))
line, = ax.plot([], [], lw=2)
plt.title('Frequency domain Signal')
plt.xlabel('log_2(Frequency/261.63)')
plt.ylabel('Amplitude')

def init():
    line.set_data([], [])
    return line,

def animate(i):
    data1_sample = data1[i*p:i*p+N]
    freq_data = fft(data1_sample)
    y = np.log(2/N * np.abs(freq_data [0:np.int (N/2)])/100)
    frequency = np.log2(np.linspace (0.0001, sample_rate/2, int(N/2))/261.63)
    line.set_data(frequency[0:1000], y[0:1000])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=(len(data))//p-1, interval=1, blit=True)



#print(frequency.shape)
#print(y.shape)
#plt.plot(frequency[0:2000], y[0:2000])
anim.save('bud.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#plt.show()

