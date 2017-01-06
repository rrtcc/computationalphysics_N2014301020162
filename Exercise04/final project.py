#雪花曲线
mport turtle
tr = turtle.getturtle()
def koch(n,len):
    if(n==0):
        tr.forward(len)
    elif(n==1):
     tr.forward(len/3.0)
     tr.left(60)
     tr.forward(len/3.0)
     tr.right(120)
     tr.forward(len/3.0)
     tr.left(60)
     tr.forward(len/3.0)
    else:
        koch(n-1,len/3.0)
        tr.left(60)
        koch(n-1,len/3.0)
        tr.right(120)
        koch(n-1,len/3.0)
        tr.left(60)
        koch(n-1,len/3.0)
koch(4,300)
 
 #二维受限制的无规行走
from __future__ import print_function
from __future__ import division
import random
MAX_COL = 9
MAX_ROW = 9
maxcycle = 10000
left = (0, -1)
right = (0, 1)
up = (-1, 0)
down = (1, 0)
matrix = [[0] * MAX_COL for _ in range(MAX_ROW)]
row = 5
col = 5
matrix[row][col] = 1
for _ in range(maxcycle):
    direct = [up, down, left, right]
    if col == 0:
        direct.remove(left)
    elif col == MAX_COL - 1:
        direct.remove(right)
    if row == 0:
        direct.remove(up)
    elif row == MAX_ROW - 1:
        direct.remove(down)

    di = random.choice(direct)
    row += di[0]
    col += di[1]
    matrix[row][col] += 1

for row in range(MAX_ROW):
    print(matrix[row])
from matplotlib import pyplot
pyplot.matshow(matrix)
pyplot.show()

#一维无规行走
import numpy as np
import pylab as plt
from math import *
import random
x=[0 for i in range(101)]
t=np.linspace(0,100,101)
n=100
for i in range(n):
    x0=random.random()
    if x0<0.5:
        x[i+1]=x[i]+1
    if x0>=0.5:
        x[i+1]=x[i]-1
x1=[0 for i in range(101)]
for i in range(n):
    x2=random.random()
    if x2<0.5:
        x1[i+1]=x1[i]+1
    if x2>=0.5:
        x1[i+1]=x1[i]-1
x4=[0 for i in range(101)]
for i in range(n):
    x3=random.random()
    if x3<0.5:
        x4[i+1]=x4[i]+1
    if x3>=0.5:
        x4[i+1]=x4[i]-1
o=np.linspace(0,0,101)
def plot():
    plt.plot(t,o)
    plt.plot(t,x,'go')
    plt.plot(t,x1,'ro')
    plt.plot(t,x4,'ko')
    plt.xlim(0,100)
    plt.xlabel('step number')
    plt.ylabel('x')
    plt.title('random walk in one dimension')
    plt.show()
plot()

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(10000)

for i in range(100):
    for j in range(10000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/10000
    x_ave[i+1] = average
    
#扩散过程    
plt.scatter(steps, x_ave)
plt.plot(steps, x_y0)
plt.xlim(0,100)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x>')
plt.title('<x> of 10000 walkers')
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import math
r0=[[[0 for i in range(21)]for j in range(21)]for k in range(100)]
for j in range(5,16):
    for i in range(5,16):
        r0[0][j][i]=1
dx=1
dt=0.25
D=1
k=0
while True:
    for j in range(1,20):
        for i in range(1,20):
            r0[k+1][j][i]=r0[k][j][i]+D*dt/(dx)**2*(r0[k][j][i+1]+r0[k][j][i-1]+r0[k][j+1][i]+r0[k][j-1][i]-4*r0[k][j][i])
    k=k+1
    if k>98:
        break
x1=np.array(r0[0])
x2=np.array(r0[10])
x3=np.array(r0[90])
x=np.linspace(-10,10,21)
y=np.linspace(-10,10,21)
X,Y=np.meshgrid(x,y)
fig = figure(figsize=[8,8])
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, x1,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('density')
title('t=0')
fig = figure(figsize=[8,8])
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, x2,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('density')
ax.set_zlim(0,1)
title('t=10')
fig = figure(figsize=[8,8])
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, x3,rstride=1, cstride=1,cmap=cm.coolwarm,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('density')
ax.set_zlim(0,1)
title('t=90')
show()
