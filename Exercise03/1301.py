import numpy as np
import matplotlib.pyplot
from pylab import *
from math import *
import mpl_toolkits.mplot3d
k=1000
dx=0.01
c=300.0
dt=dx/c
y=[[0 for i in range(100)]for n in range(3000)]


x=np.linspace(0,1,100)
t=np.linspace(0,0.1,3000)
r=c*dt/dx
for i in range(31):
    y[0][i]=0.8*x[i]
    y[1][i]=0.8*x[i]
for i in range(30,100):
    y[0][i]=-2.4/70*x[i]+24/7
    y[1][i]=-2.4/70*x[i]+24/7



for n in range(3000):
    for i in range(1,99):
        y[n][i]=2*(1-r**2)*y[n-1][i]-y[n-2][i]+r**2*(y[n-1][i+1]+y[n-1][i-1])

y4=[]
for n in range(len(t)):
    y4.append(y[n][30])
figure(figsize=[16,8])
subplot(121)
plot(t,y4)
title('string signal versus time')
xlabel('time(s)')
ylabel('signal')
xlim(0,0.11)
subplot(122)
p=abs(np.fft.rfft(y4))**2
f = np.linspace(0, int(1/dt/2), len(p))
plot(f, p)
xlim(0,3000)
xlabel('Frequency(Hz)')
ylabel('Power')
title('Power spectrum')
show()
