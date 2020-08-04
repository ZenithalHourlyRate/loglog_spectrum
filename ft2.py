import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy import pi
from scipy.fftpack import fft
from scipy.io import wavfile
from multiprocessing import Pool
import functools

from sep import custom1

sample_rate, data = wavfile.read('./input.wav')
print(sample_rate)
data1=data[:,0]

N = sample_rate//10
p = sample_rate//30

fig = plt.figure()
ax = plt.axes(xlim=(-1, 3), ylim=(0, 5))
line, = ax.plot([], [], lw=2, color='#f44336')
x_ax = np.linspace(-1+1/12, 3+1/12, (3+1)*12 )
frequency = np.log2(np.linspace (0.0001, sample_rate/2, int(N/2))/261.63)
init_height = np.zeros(x_ax.shape)
rects = ax.bar(x_ax, init_height, color='#03a9f4', width=1/12*0.8)
plt.title('Frequency domain Signal')
plt.xlabel('log_2(Frequency/261.63)')
plt.ylabel('Amplitude')

#all_freq_data_fun = lambda i: fft(data1[i*p:i*p+N])
data1_sample=[data1[i*p:i*p+N] for i in range((len(data))//p-1)]
all_freq_data = [ fft(data1_sample[i]) for i in range(len(data1_sample))  ]
all_y = [ np.log(2/N * np.abs(all_freq_data[i][0:np.int (N/2)])/100) 
            for i in range(len(all_freq_data)) ]
#all_freq_data = pool.map(all_freq_data_fun, range((len(data)//p-1)))


print('done fft')

pool = Pool(12)

def init():
    line.set_data([], [])
    return line,


def animate(i):
    #data1_sample = data1[i*p:i*p+N]
    y = all_y[i]
    custom2 = functools.partial(custom1, y=y, frequency=frequency)
    line.set_data(frequency[0:1000], y[0:1000])
    hs = pool.map(custom2,x_ax)
    for k, rect in zip(range(len(rects)),rects):
        rect.set_height(np.nanmean(hs[k]))
    print('finished {} frame'.format(i))
    return line,

anim = animation.FuncAnimation(fig, animate,
                               frames=(len(data))//p-1, interval=1, blit=True)



#print(frequency.shape)
#print(y.shape)
#plt.plot(frequency[0:2000], y[0:2000])
anim.save('bar.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#plt.show()
pool.close()
