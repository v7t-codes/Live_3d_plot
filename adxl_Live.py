import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from mpl_toolkits.mplot3d import Axes3D #import the 3d axes library
import numpy as np
import matplotlib.animation as animation

ser = serial.Serial('com3', 9600)

x=[]
y=[]
z=[]

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1 = plt.axes(projection='3d')

def animate(i):
    try:
        if(ser.inWaiting>0):
            X=ser.readline()
            Y=ser.readline()
            Z=ser.readline()
    
            x.append(float(X))
            y.append(float(Y))
            z.append(float(Z))
            ax1.clear()
            ax1.plot(x,y,z)

    except IndexError:
            print "Ok"                

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()