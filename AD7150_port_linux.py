import serial
#import numpy as np
from matplotlib import pyplot as plt
ser = serial.Serial('/dev/ttyACM1', 115200)
 
plt.ion() # set plot to animated
  
ydata = [0] * 50
ax1=plt.axes()  
   
# make plot
line, = plt.plot(ydata)
plt.ylim([-100,100])

# start data collection
while True:  
    data = ser.readline()
    try:
        data = abs(float(data)) # read data from serial
    except ValueError:
        continue
    # port and strip line endings
    ymin = float(min(ydata))-50
    ymax = float(max(ydata))+50
    plt.ylim([ymin,ymax])
    ydata.append(data)
    del ydata[0]
#    line.set_xdata(np.arange(len(ydata)))
    line.set_xdata(xrange(len(ydata)))
    line.set_ydata(ydata)  # update the data
    plt.draw() # update the plot
