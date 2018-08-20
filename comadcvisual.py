import serial.tools.list_ports
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
from datetime import datetime as dt
from rx.linq.observable import catch


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
line, = ax1.plot([], [], color='g')
A=[]

def ByteToHex( byteStr ):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    
    # Uses list comprehension which is a fractionally faster implementation than
    # the alternative, more readable, implementation below
    #   
    #    hex = []
    #    for aChar in byteStr:
    #        hex.append( "%02X " % ord( aChar ) )
    #
    #    return ''.join( hex ).strip()        

    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

def animate(i):
    dataArray= ''
    while(len(dataArray)<4):
        time.sleep(0.3)
        while ser.inWaiting() > 0:
            dataArray+=str(ser.read(1).hex())
    print(dataArray)
    xar = []
    yar = []
    data=(list(dataArray))
    print(data)
#     A=[]
    if len(data)>3:
        for i in range(0,len(data)-(len(data)%4),4):
            A.append((int(data[i],16)<<12) + (int(data[i+1],16)<<8) + (int(data[i+2],16)<<4) + (int(data[i+3],16)))
    print(A)
    x=0
    for y in A:
        xar.append(x)
        x+=1
        yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
    line.set_data(x, y)
#     ax1.fill_between(x, -0.5, y, color='lightgrey')
    return line,

not_connected = True
element = ''
while not_connected: 
    lst = serial.tools.list_ports.comports()
    connected = []
    com_num = ''
    for element in lst:
        connected.append(element.device)
    print("Connected COM ports: " + str(connected))
    
    element = input('com port ')
    ser = serial.Serial(element, 9600)
    out = ''
    if ser.is_open:
        print(element + ' connected')
        not_connected = False
        ser.close()


data = []

try:   
    ser = serial.Serial(element, 9600)   
    while True: 
        ani = animation.FuncAnimation(fig, animate, interval=1)
        plt.show()
        
finally:
    ser.close()
    print('ser.close()')



